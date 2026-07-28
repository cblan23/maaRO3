"""Fetch public YouTube watch metadata for offline video research.

The script deliberately uses the ordinary public watch page and never reads browser
cookies.  Output belongs in a temporary research directory and must not be treated
as evidence until a human has inspected the referenced frames or video segment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


WATCH_URL = "https://www.youtube.com/watch?v={video_id}"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)
PUBLIC_CAPTION_ENDPOINT = "https://macparakeet.com/api/youtube-captions"


def extract_json_object(page: str, marker_patterns: tuple[str, ...]) -> dict:
    decoder = json.JSONDecoder()
    for pattern in marker_patterns:
        for match in re.finditer(pattern, page):
            brace = page.find("{", match.end())
            if brace < 0:
                continue
            try:
                value, _ = decoder.raw_decode(page[brace:])
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                return value
    raise ValueError("ytInitialPlayerResponse JSON was not found in the watch page")


def public_format_summary(item: dict) -> dict:
    return {
        key: item[key]
        for key in (
            "itag",
            "mimeType",
            "bitrate",
            "width",
            "height",
            "fps",
            "quality",
            "qualityLabel",
            "contentLength",
            "approxDurationMs",
            "audioQuality",
            "audioSampleRate",
            "audioChannels",
        )
        if key in item
    } | {
        "has_direct_url": isinstance(item.get("url"), str),
        "has_signature_cipher": isinstance(
            item.get("signatureCipher") or item.get("cipher"), str
        ),
    }


def compact_metadata(video_id: str, response: dict) -> dict:
    details = response.get("videoDetails") or {}
    micro = (
        response.get("microformat", {})
        .get("playerMicroformatRenderer", {})
    )
    streaming = response.get("streamingData") or {}
    captions = (
        response.get("captions", {})
        .get("playerCaptionsTracklistRenderer", {})
        .get("captionTracks", [])
    )
    storyboard = (
        response.get("storyboards", {})
        .get("playerStoryboardSpecRenderer", {})
        .get("spec")
    )
    return {
        "video_id": video_id,
        "watch_url": WATCH_URL.format(video_id=video_id),
        "playability_status": response.get("playabilityStatus"),
        "title": details.get("title"),
        "author": details.get("author"),
        "channel_id": details.get("channelId"),
        "length_seconds": details.get("lengthSeconds"),
        "is_live_content": details.get("isLiveContent"),
        "short_description": details.get("shortDescription"),
        "publish_date": micro.get("publishDate"),
        "upload_date": micro.get("uploadDate"),
        "live_broadcast_details": micro.get("liveBroadcastDetails"),
        "caption_tracks": [
            {
                "base_url": track.get("baseUrl"),
                "name": (track.get("name") or {}).get("simpleText"),
                "language_code": track.get("languageCode"),
                "kind": track.get("kind"),
                "is_translatable": track.get("isTranslatable"),
            }
            for track in captions
        ],
        "storyboard_spec": storyboard,
        "formats": [
            public_format_summary(item) for item in streaming.get("formats", [])
        ],
        "adaptive_formats": [
            public_format_summary(item)
            for item in streaming.get("adaptiveFormats", [])
        ],
        "expires_in_seconds": streaming.get("expiresInSeconds"),
    }


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_watch_page(video_id: str) -> str:
    return fetch_text(WATCH_URL.format(video_id=video_id))


def track_priority(track: dict[str, str]) -> tuple[int, int]:
    language = track.get("lang_code", "").lower()
    preferred = 0 if language.startswith(("zh", "cmn")) else 1
    automatic = 1 if track.get("kind") == "asr" else 0
    return preferred, automatic


def fetch_public_captions(video_id: str, output: Path) -> dict:
    """Fetch captions through a documented, no-account public page endpoint."""

    list_url = f"{PUBLIC_CAPTION_ENDPOINT}?{urlencode({'type': 'list', 'v': video_id})}"
    track_xml = fetch_text(list_url)
    (output / "caption-tracks.xml").write_text(track_xml, encoding="utf-8")

    try:
        root = ET.fromstring(track_xml)
    except ET.ParseError as error:
        return {"status": "invalid_track_xml", "error": str(error), "tracks": []}

    tracks = [dict(element.attrib) for element in root.findall(".//track")]
    if not tracks:
        return {"status": "no_captions", "tracks": []}

    tracks.sort(key=track_priority)
    selected = tracks[0]
    query = {
        "v": video_id,
        "lang": selected.get("lang_code", ""),
        "name": selected.get("name", ""),
        "kind": selected.get("kind", ""),
    }
    caption_url = f"{PUBLIC_CAPTION_ENDPOINT}?{urlencode(query)}"
    caption_xml = fetch_text(caption_url)
    (output / "captions.xml").write_text(caption_xml, encoding="utf-8")
    return {
        "status": "downloaded",
        "tracks": tracks,
        "selected": selected,
        "caption_file": "captions.xml",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--save-player-response",
        action="store_true",
        help="Save the full ephemeral player response alongside compact metadata.",
    )
    parser.add_argument(
        "--fetch-public-captions",
        action="store_true",
        help="Try the no-account MacParakeet public caption endpoint.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"[0-9A-Za-z_-]{11}", args.video_id):
        raise SystemExit("--video-id must be an 11-character YouTube video ID")

    args.output.mkdir(parents=True, exist_ok=True)
    try:
        page = fetch_watch_page(args.video_id)
        player_response = extract_json_object(
            page,
            (
                r"ytInitialPlayerResponse\s*=\s*",
                r'"ytInitialPlayerResponse"\s*:\s*',
            ),
        )
    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        print(f"YouTube watch-page fetch failed: {error}", file=sys.stderr)
        return 1

    metadata = compact_metadata(args.video_id, player_response)
    if args.fetch_public_captions:
        try:
            metadata["public_caption_fetch"] = fetch_public_captions(
                args.video_id, args.output
            )
        except (HTTPError, URLError, TimeoutError) as error:
            metadata["public_caption_fetch"] = {
                "status": "request_failed",
                "error": str(error),
            }
    (args.output / "watch-metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if args.save_player_response:
        (args.output / "player-response.json").write_text(
            json.dumps(player_response, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
