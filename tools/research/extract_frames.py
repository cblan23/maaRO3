"""Extract exact research frames from a local video stream.

The script deliberately has no downloader. Keep acquisition, review, and
evidence selection as separate, auditable steps.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import av


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--times", type=float, nargs="+", required=True)
    return parser.parse_args()


def extract_frame(source: Path, output: Path, timestamp: float) -> Path:
    container = av.open(source)
    stream = container.streams.video[0]
    container.seek(
        int(timestamp / float(stream.time_base)),
        stream=stream,
        any_frame=False,
        backward=True,
    )

    destination = output / f"{timestamp:08.2f}.png"
    for frame in container.decode(stream):
        frame_time = float(frame.pts * stream.time_base)
        if frame_time >= timestamp:
            frame.to_image().save(destination)
            break
    else:
        raise RuntimeError(f"No frame found at {timestamp:.2f}s")

    container.close()
    return destination


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    for timestamp in args.times:
        print(extract_frame(args.input, args.output, timestamp))


if __name__ == "__main__":
    main()
