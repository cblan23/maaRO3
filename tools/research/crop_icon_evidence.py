"""Generate exact, traceable icon/UI-state crops from reviewed evidence frames."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CATALOG = ROOT / "research" / "evidence" / "icons" / "catalog.json"
RESAMPLING = {
    "nearest": Image.Resampling.NEAREST,
    "bilinear": Image.Resampling.BILINEAR,
    "bicubic": Image.Resampling.BICUBIC,
    "lanczos": Image.Resampling.LANCZOS,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument(
        "--update-derived",
        action="store_true",
        help="write generated dimensions and SHA-256 values back to the catalog",
    )
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    args = parse_args()
    catalog_path = args.catalog.resolve()
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    output_root = catalog_path.parent
    expected_files: set[Path] = set()

    for sample in catalog["samples"]:
        parent = ROOT / sample["parent_frame"]
        if not parent.is_file():
            raise SystemExit(f"missing parent frame for {sample['id']}: {parent}")
        actual_parent_hash = sha256(parent)
        if actual_parent_hash != sample["parent_sha256"]:
            raise SystemExit(f"parent hash mismatch for {sample['id']}: {parent}")

        crop = sample["crop"]
        with Image.open(parent) as source:
            source.load()
            x, y = crop["x"], crop["y"]
            width, height = crop["width"], crop["height"]
            if x + width > source.width or y + height > source.height:
                raise SystemExit(
                    f"crop exceeds parent for {sample['id']}: "
                    f"{x},{y},{width},{height} vs {source.width}x{source.height}"
                )
            result = source.crop((x, y, x + width, y + height))
            scale = sample["scale"]
            if scale["applied"]:
                algorithm = scale["algorithm"]
                result = result.resize(
                    (scale["output_width"], scale["output_height"]),
                    RESAMPLING[algorithm],
                )

            destination = output_root / sample["file"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            result.save(destination, format="PNG")

        expected_files.add(destination.resolve())
        sample["dimensions"] = [result.width, result.height]
        sample["sha256"] = sha256(destination)
        print(f"{sample['id']}: {result.width}x{result.height} {sample['sha256']}")

    crop_root = output_root / "crops"
    actual_files = {path.resolve() for path in crop_root.glob("*.png")}
    unexpected = sorted(actual_files - expected_files)
    if unexpected:
        names = ", ".join(path.name for path in unexpected)
        raise SystemExit(f"untracked crop files: {names}")

    if args.update_derived:
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"updated {catalog_path}")


if __name__ == "__main__":
    main()
