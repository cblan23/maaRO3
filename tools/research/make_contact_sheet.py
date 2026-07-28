"""Create a labelled contact sheet for manual video-frame triage."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--width", type=int, default=480)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    files = sorted(
        path
        for path in args.input.iterdir()
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        and not path.stem.startswith("sheet-")
    )
    files = files[args.start :]
    if args.limit is not None:
        files = files[: args.limit]
    if not files:
        raise SystemExit(f"No image frames found in {args.input}")

    label_height = 28
    first = Image.open(files[0])
    thumbnail_height = round(args.width * first.height / first.width)
    rows = math.ceil(len(files) / args.columns)
    sheet = Image.new(
        "RGB",
        (args.columns * args.width, rows * (thumbnail_height + label_height)),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)

    for index, path in enumerate(files):
        image = Image.open(path).convert("RGB")
        image.thumbnail((args.width, thumbnail_height))
        x = (index % args.columns) * args.width
        y = (index // args.columns) * (thumbnail_height + label_height)
        sheet.paste(image, (x, y + label_height))
        draw.text((x + 8, y + 4), path.stem, fill="black", font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output, quality=90)
    print(args.output)


if __name__ == "__main__":
    main()
