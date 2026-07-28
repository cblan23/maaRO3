"""Extract timestamped storyboard tiles from a yt-dlp MHTML file.

yt-dlp stores Twitch storyboard formats as an MHTML document containing one
or more JPEG sprite sheets.  This helper keeps the acquisition artifact intact
and emits individual, approximately timestamped tiles for manual triage.
"""

from __future__ import annotations

import argparse
from email import policy
from email.parser import BytesParser
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tile-width", type=int, required=True)
    parser.add_argument("--tile-height", type=int, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    message = BytesParser(policy=policy.default).parsebytes(args.input.read_bytes())
    image_parts = [
        part for part in message.walk() if part.get_content_maintype() == "image"
    ]
    if not image_parts:
        raise SystemExit(f"No image parts found in {args.input}")

    args.output.mkdir(parents=True, exist_ok=True)
    elapsed = 0.0
    written = 0

    for sheet_index, part in enumerate(image_parts):
        payload = part.get_payload(decode=True)
        if not payload:
            raise SystemExit(f"Empty storyboard sheet {sheet_index}")

        sheet_path = args.output / f"sheet-{sheet_index:02d}.jpg"
        sheet_path.write_bytes(payload)
        with Image.open(sheet_path) as sheet:
            columns = sheet.width // args.tile_width
            rows = sheet.height // args.tile_height
            tile_count = columns * rows
            if columns < 1 or rows < 1:
                raise SystemExit(
                    f"Sheet {sheet_index} ({sheet.width}x{sheet.height}) is smaller "
                    f"than one {args.tile_width}x{args.tile_height} tile"
                )

            duration = float(part.get("X.yt-dlp.Duration", "0"))
            if duration <= 0:
                raise SystemExit(f"Sheet {sheet_index} has no positive duration")
            interval = duration / tile_count

            for tile_index in range(tile_count):
                x = (tile_index % columns) * args.tile_width
                y = (tile_index // columns) * args.tile_height
                tile = sheet.crop(
                    (x, y, x + args.tile_width, y + args.tile_height)
                )
                timestamp = elapsed + tile_index * interval
                tile.save(args.output / f"{timestamp:010.2f}.jpg", quality=95)
                written += 1

        elapsed += duration

    print(
        f"Extracted {written} tiles from {len(image_parts)} sheets; "
        f"covered {elapsed:.2f}s"
    )


if __name__ == "__main__":
    main()
