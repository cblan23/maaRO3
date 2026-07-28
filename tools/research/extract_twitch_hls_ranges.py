"""Download selected public Twitch VOD ranges or sparse review points.

The script intentionally downloads only explicitly requested HLS segments.  Full
VOD files remain outside the repository, while the emitted frames can be
reviewed and, if justified, copied into the evidence store with a Manifest.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import time
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import av
import yt_dlp


USER_AGENT = "Mozilla/5.0 maaRO3-public-research/1.0"


@dataclass(frozen=True)
class Segment:
    index: int
    start: float
    duration: float
    url: str

    @property
    def end(self) -> float:
        return self.start + self.duration


def parse_time(value: str) -> float:
    parts = value.split(":")
    if len(parts) > 3 or not parts:
        raise argparse.ArgumentTypeError(f"Invalid timestamp: {value}")
    try:
        numbers = [float(part) for part in parts]
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"Invalid timestamp: {value}") from error
    seconds = 0.0
    for number in numbers:
        seconds = seconds * 60 + number
    if seconds < 0:
        raise argparse.ArgumentTypeError("Timestamps must be non-negative")
    return seconds


def parse_range(value: str) -> tuple[float, float]:
    try:
        start_text, end_text = value.split("-", 1)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "Ranges must use START-END, for example 00:15:00-00:18:00"
        ) from error
    start = parse_time(start_text)
    end = parse_time(end_text)
    if end <= start:
        raise argparse.ArgumentTypeError(f"Range end must exceed start: {value}")
    return start, end


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--format", default="360p")
    parser.add_argument("--output", type=Path, required=True)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--ranges", type=parse_range, nargs="+")
    selection.add_argument(
        "--points",
        type=parse_time,
        nargs="+",
        help=(
            "Sparse source timestamps. Only the HLS segments containing these "
            "points are downloaded."
        ),
    )
    parser.add_argument("--interval", type=float, default=3.0)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    if args.interval <= 0:
        parser.error("--interval must be positive")
    if args.workers <= 0:
        parser.error("--workers must be positive")
    return args


def request_bytes(url: str, attempts: int = 4) -> bytes:
    error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=45) as response:
                return response.read()
        except Exception as caught:  # network failures vary by Python runtime
            error = caught
            if attempt + 1 < attempts:
                time.sleep(1.5 * (attempt + 1))
    assert error is not None
    raise error


def extract_format(video_url: str, format_id: str) -> tuple[dict, dict]:
    options = {"quiet": True, "no_warnings": True, "skip_download": True}
    with yt_dlp.YoutubeDL(options) as downloader:
        info = downloader.extract_info(video_url, download=False)
    formats = info.get("formats") or []
    matches = [item for item in formats if item.get("format_id") == format_id]
    if not matches:
        available = ", ".join(str(item.get("format_id")) for item in formats)
        raise SystemExit(f"Format {format_id!r} unavailable; choose from: {available}")
    return info, matches[-1]


def parse_media_playlist(url: str) -> list[Segment]:
    text = request_bytes(url).decode("utf-8", errors="strict")
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if any(line.startswith("#EXT-X-STREAM-INF") for line in lines):
        for index, line in enumerate(lines[:-1]):
            if line.startswith("#EXT-X-STREAM-INF"):
                return parse_media_playlist(urljoin(url, lines[index + 1]))
        raise SystemExit("Master HLS playlist did not contain a child URI")

    segments: list[Segment] = []
    elapsed = 0.0
    pending_duration: float | None = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            pending_duration = float(line.removeprefix("#EXTINF:").split(",", 1)[0])
        elif not line.startswith("#") and pending_duration is not None:
            segments.append(
                Segment(
                    index=len(segments),
                    start=elapsed,
                    duration=pending_duration,
                    url=urljoin(url, line),
                )
            )
            elapsed += pending_duration
            pending_duration = None
    if not segments:
        raise SystemExit("No media segments found in HLS playlist")
    return segments


def download_segment(item: tuple[Segment, Path]) -> Path:
    segment, destination = item
    if destination.is_file() and destination.stat().st_size > 0:
        return destination
    destination.write_bytes(request_bytes(segment.url))
    return destination


def extract_review_frames(
    video: Path,
    output: Path,
    source_start: float,
    requested_start: float,
    requested_end: float,
    interval: float,
) -> list[dict]:
    output.mkdir(parents=True, exist_ok=True)
    container = av.open(video)
    stream = container.streams.video[0]
    first_time: float | None = None
    next_source_time = requested_start
    written: list[dict] = []

    for frame in container.decode(stream):
        if frame.pts is None:
            continue
        frame_time = float(frame.pts * stream.time_base)
        if first_time is None:
            first_time = frame_time
        source_time = source_start + (frame_time - first_time)
        if source_time + 0.05 < next_source_time:
            continue
        while source_time >= next_source_time and next_source_time < requested_end:
            name = f"{next_source_time:010.2f}.jpg"
            destination = output / name
            frame.to_image().save(destination, quality=95)
            written.append(
                {
                    "file": destination.name,
                    "source_timestamp_seconds": round(source_time, 3),
                    "requested_timestamp_seconds": round(next_source_time, 3),
                }
            )
            next_source_time += interval
        if next_source_time >= requested_end:
            break

    container.close()
    if not written:
        raise RuntimeError(f"No review frames decoded from {video}")
    return written


def extract_sparse_frames(
    video: Path,
    output: Path,
    source_start: float,
    requested_points: list[float],
) -> list[dict]:
    """Decode one HLS segment once and save frames at requested source points."""

    output.mkdir(parents=True, exist_ok=True)
    points = sorted(requested_points)
    container = av.open(video)
    stream = container.streams.video[0]
    first_time: float | None = None
    point_index = 0
    written: list[dict] = []

    for frame in container.decode(stream):
        if frame.pts is None:
            continue
        frame_time = float(frame.pts * stream.time_base)
        if first_time is None:
            first_time = frame_time
        source_time = source_start + (frame_time - first_time)
        while point_index < len(points) and source_time + 0.05 >= points[point_index]:
            requested = points[point_index]
            destination = output / f"{requested:010.2f}.jpg"
            frame.to_image().save(destination, quality=95)
            written.append(
                {
                    "file": destination.name,
                    "source_timestamp_seconds": round(source_time, 3),
                    "requested_timestamp_seconds": round(requested, 3),
                }
            )
            point_index += 1
        if point_index >= len(points):
            break

    container.close()
    if point_index != len(points):
        missing = ", ".join(f"{point:.2f}" for point in points[point_index:])
        raise RuntimeError(f"No frames decoded for sparse points: {missing}")
    return written


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    info, selected_format = extract_format(args.url, args.format)
    playlist_url = selected_format.get("url")
    if not playlist_url:
        raise SystemExit(f"Selected format {args.format!r} has no media URL")
    segments = parse_media_playlist(playlist_url)

    review_ranges: list[dict] = []
    for range_index, (requested_start, requested_end) in enumerate(args.ranges or []):
        selected = [
            segment
            for segment in segments
            if segment.end > requested_start and segment.start < requested_end
        ]
        if not selected:
            raise SystemExit(
                f"No segments overlap {requested_start:.2f}-{requested_end:.2f}s"
            )

        range_root = args.output / f"range-{range_index:02d}"
        segment_root = range_root / "segments"
        frame_root = range_root / "frames"
        segment_root.mkdir(parents=True, exist_ok=True)
        destinations = [
            segment_root / f"{segment.index:06d}.ts" for segment in selected
        ]
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            list(executor.map(download_segment, zip(selected, destinations)))

        joined = range_root / "range.ts"
        with joined.open("wb") as output_stream:
            for destination in destinations:
                output_stream.write(destination.read_bytes())

        frames = extract_review_frames(
            joined,
            frame_root,
            source_start=selected[0].start,
            requested_start=requested_start,
            requested_end=requested_end,
            interval=args.interval,
        )
        review_ranges.append(
            {
                "requested_start": requested_start,
                "requested_end": requested_end,
                "segment_start": selected[0].start,
                "segment_end": selected[-1].end,
                "segments": len(selected),
                "frames": frames,
            }
        )
        print(
            f"range {range_index:02d}: {len(selected)} segments, "
            f"{len(frames)} frames"
        )

    sparse_report: dict | None = None
    if args.points:
        requested_points = sorted(set(args.points))
        point_segments: list[tuple[float, Segment]] = []
        for point in requested_points:
            match = next(
                (
                    segment
                    for segment in segments
                    if segment.start <= point < segment.end
                ),
                None,
            )
            if match is None:
                raise SystemExit(f"No segment contains sparse point {point:.2f}s")
            point_segments.append((point, match))

        segment_root = args.output / "segments"
        frame_root = args.output / "frames"
        segment_root.mkdir(parents=True, exist_ok=True)
        selected_by_index = {
            segment.index: segment for _, segment in point_segments
        }
        destinations = {
            index: segment_root / f"{index:06d}.ts"
            for index in selected_by_index
        }
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            list(
                executor.map(
                    download_segment,
                    (
                        (segment, destinations[index])
                        for index, segment in selected_by_index.items()
                    ),
                )
            )

        frames: list[dict] = []
        for index, segment in sorted(selected_by_index.items()):
            points = [
                point
                for point, selected_segment in point_segments
                if selected_segment.index == index
            ]
            frames.extend(
                extract_sparse_frames(
                    destinations[index],
                    frame_root,
                    source_start=segment.start,
                    requested_points=points,
                )
            )
        frames.sort(key=lambda item: item["requested_timestamp_seconds"])
        sparse_report = {
            "requested_points": requested_points,
            "segments": len(selected_by_index),
            "frames": frames,
        }
        print(
            f"sparse points: {len(selected_by_index)} segments, "
            f"{len(frames)} frames"
        )

    report = {
        "video": {
            "id": info.get("id"),
            "title": info.get("title"),
            "uploader": info.get("uploader"),
            "timestamp": info.get("timestamp"),
            "duration": info.get("duration"),
            "webpage_url": info.get("webpage_url") or args.url,
        },
        "format": {
            key: selected_format.get(key)
            for key in ("format_id", "width", "height", "fps", "tbr")
        },
        "playlist": {
            "segment_count": len(segments),
            "duration": round(segments[-1].end, 3),
        },
        "interval": args.interval,
        "ranges": review_ranges,
        "sparse": sparse_report,
    }
    (args.output / "review.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(args.output / "review.json")


if __name__ == "__main__":
    main()
