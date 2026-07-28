"""Validate the pre-client research scaffold without game or Maa access."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from jsonschema import Draft202012Validator, FormatChecker
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_interface(errors: list[str]) -> None:
    interface = load_json(ROOT / "assets" / "interface.json")
    require(isinstance(interface, dict), "interface.json root must be an object", errors)
    if not isinstance(interface, dict):
        return
    controllers = interface.get("controller")
    require(isinstance(controllers, list) and len(controllers) == 1,
            "research interface must expose exactly one controller", errors)
    if isinstance(controllers, list) and controllers:
        controller = controllers[0]
        require(controller.get("type") == "Win32", "controller must be Win32", errors)
        win32 = controller.get("win32", {})
        require(win32.get("class_regex") == "^RO3_CLASS_NOT_CAPTURED$",
                "window class must remain fail-closed before capture", errors)
        require(win32.get("window_regex") == "^RO3_TITLE_NOT_CAPTURED$",
                "window title must remain fail-closed before capture", errors)

    tasks = interface.get("task", [])
    require(tasks == [{"name": "预研占位：仅验证框架装载", "entry": "ResearchProbe"}],
            "only the no-input ResearchProbe task is allowed", errors)
    pipeline = load_json(ROOT / "assets" / "resource" / "pipeline" / "research_probe.json")
    require(pipeline == {"ResearchProbe": {"recognition": "DirectHit", "action": "DoNothing"}},
            "ResearchProbe must remain a DirectHit/DoNothing node", errors)


def validate_no_pipeline_input(errors: list[str]) -> None:
    pipeline_root = ROOT / "assets" / "resource" / "pipeline"
    for path in sorted(pipeline_root.glob("*.json")):
        data = load_json(path)
        if not isinstance(data, dict):
            errors.append(f"pipeline root must be an object: {path.relative_to(ROOT)}")
            continue
        for node_name, node in data.items():
            if not isinstance(node, dict):
                errors.append(f"pipeline node must be an object: {node_name}")
                continue
            action = node.get("action", "DoNothing")
            require(action == "DoNothing",
                    f"OFFLINE_RESEARCH forbids pipeline input: {node_name} action={action}", errors)
            for forbidden_key in ("custom_action", "custom_action_param"):
                require(forbidden_key not in node,
                        f"OFFLINE_RESEARCH forbids {forbidden_key}: {node_name}", errors)


def validate_no_python_input(errors: list[str]) -> None:
    forbidden_patterns = {
        r"\bAdbController\b": "ADB controller",
        r"\bWin32Controller\b": "Win32 controller",
        r"\.post_click\s*\(": "click input",
        r"\.post_swipe\s*\(": "swipe input",
        r"\.post_key\s*\(": "key input",
        r"\.post_text\s*\(": "text input",
        r"\.post_touch\w*\s*\(": "touch input",
    }
    for root_name in ("automation", "agent"):
        for path in sorted((ROOT / root_name).glob("**/*.py")):
            text = path.read_text(encoding="utf-8")
            for pattern, label in forbidden_patterns.items():
                require(re.search(pattern, text) is None,
                        f"OFFLINE_RESEARCH forbids {label} in {path.relative_to(ROOT)}", errors)


def validate_policy(errors: list[str]) -> None:
    policy = load_json(ROOT / "config" / "research_policy.json")
    if not isinstance(policy, dict):
        errors.append("research_policy.json root must be an object")
        return
    require(policy.get("phase") == "OFFLINE_RESEARCH", "phase must be OFFLINE_RESEARCH", errors)
    require(policy.get("online_game_input_enabled") is False,
            "online game input must be disabled", errors)
    require(policy.get("authorized_test_input_enabled") is False,
            "authorized test input must be disabled", errors)
    blocked = policy.get("blocked", [])
    for item in ("captcha_or_anti_cheat_bypass", "risk_control_evasion", "multi_account_farming"):
        require(item in blocked, f"blocked policy is missing {item}", errors)


def validate_catalog(errors: list[str]) -> set[str]:
    catalog = load_json(ROOT / "research" / "catalog" / "sources.json")
    schema = load_json(ROOT / "research" / "catalog" / "sources.schema.json")
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for schema_error in sorted(validator.iter_errors(catalog), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in schema_error.path) or "<root>"
        errors.append(f"sources.json schema error at {location}: {schema_error.message}")
    if not isinstance(catalog, dict) or not isinstance(catalog.get("sources"), list):
        errors.append("sources.json must contain a sources array")
        return set()
    seen: set[str] = set()
    for index, source in enumerate(catalog["sources"]):
        prefix = f"sources[{index}]"
        require(isinstance(source, dict), f"{prefix} must be an object", errors)
        if not isinstance(source, dict):
            continue
        source_id = source.get("id")
        require(isinstance(source_id, str) and bool(source_id), f"{prefix}.id is required", errors)
        if isinstance(source_id, str):
            require(source_id not in seen, f"duplicate source id: {source_id}", errors)
            seen.add(source_id)
        require(is_https_url(source.get("url")), f"{prefix}.url must be HTTPS", errors)
        require(source.get("grade") in {"A", "B", "C", "D"},
                f"{prefix}.grade is invalid", errors)
    return seen


def validate_evidence(source_ids: set[str], errors: list[str]) -> tuple[int, int]:
    evidence_root = ROOT / "research" / "evidence" / "video"
    manifest_schema = load_json(ROOT / "research" / "evidence" / "manifest.schema.json")
    schema_validator = Draft202012Validator(manifest_schema, format_checker=FormatChecker())
    manifest_paths = sorted(evidence_root.glob("*/manifest.json"))
    evidence_directories = sorted(path for path in evidence_root.iterdir() if path.is_dir())
    require(len(manifest_paths) == len(evidence_directories),
            "every video evidence directory must contain manifest.json", errors)
    frame_count = 0
    for manifest_path in manifest_paths:
        manifest = load_json(manifest_path)
        prefix = manifest_path.relative_to(ROOT).as_posix()
        for schema_error in sorted(schema_validator.iter_errors(manifest), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in schema_error.path) or "<root>"
            errors.append(f"{prefix} schema error at {location}: {schema_error.message}")
        if not isinstance(manifest, dict):
            errors.append(f"{prefix} root must be an object")
            continue
        require(manifest.get("source_id") in source_ids,
                f"{prefix} references an unknown source_id", errors)
        require(is_https_url(manifest.get("primary_url")), f"{prefix} primary_url is invalid", errors)
        require(is_https_url(manifest.get("capture_url")), f"{prefix} capture_url is invalid", errors)
        frames = manifest.get("frames")
        require(isinstance(frames, list) and bool(frames), f"{prefix} has no frames", errors)
        if not isinstance(frames, list):
            continue
        seen_files: set[str] = set()
        for frame in frames:
            if not isinstance(frame, dict):
                errors.append(f"{prefix} contains a non-object frame")
                continue
            relative = frame.get("file")
            require(isinstance(relative, str) and relative not in seen_files,
                    f"{prefix} contains a missing/duplicate frame path", errors)
            if not isinstance(relative, str):
                continue
            seen_files.add(relative)
            frame_count += 1
            path = manifest_path.parent / relative
            require(path.is_file(), f"missing evidence file: {path.relative_to(ROOT)}", errors)
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                require(digest == frame.get("sha256"),
                        f"hash mismatch: {path.relative_to(ROOT)}", errors)
            require(frame.get("recheck_in_cn_test") is True,
                    f"pre-client frame must be marked for CN recheck: {relative}", errors)
        actual_files = {
            path.relative_to(manifest_path.parent).as_posix()
            for path in manifest_path.parent.glob("frames/*")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg"}
        }
        require(actual_files == seen_files,
                f"manifest/file mismatch in {manifest_path.parent.relative_to(ROOT)}", errors)
    return len(manifest_paths), frame_count


def validate_still_evidence(source_ids: set[str], errors: list[str]) -> tuple[int, int]:
    evidence_root = ROOT / "research" / "evidence" / "still"
    manifest_schema = load_json(evidence_root / "manifest.schema.json")
    schema_validator = Draft202012Validator(manifest_schema, format_checker=FormatChecker())
    manifest_paths = sorted(evidence_root.glob("*/manifest.json"))
    evidence_directories = sorted(path for path in evidence_root.iterdir() if path.is_dir())
    require(
        len(manifest_paths) == len(evidence_directories),
        "every still evidence directory must contain manifest.json",
        errors,
    )
    image_count = 0
    for manifest_path in manifest_paths:
        manifest = load_json(manifest_path)
        prefix = manifest_path.relative_to(ROOT).as_posix()
        for schema_error in sorted(
            schema_validator.iter_errors(manifest), key=lambda item: list(item.path)
        ):
            location = ".".join(str(part) for part in schema_error.path) or "<root>"
            errors.append(f"{prefix} schema error at {location}: {schema_error.message}")
        if not isinstance(manifest, dict):
            errors.append(f"{prefix} root must be an object")
            continue
        require(
            manifest.get("source_id") in source_ids,
            f"{prefix} references an unknown source_id",
            errors,
        )
        require(is_https_url(manifest.get("primary_url")), f"{prefix} primary_url is invalid", errors)
        require(is_https_url(manifest.get("capture_url")), f"{prefix} capture_url is invalid", errors)
        images = manifest.get("images")
        require(isinstance(images, list) and bool(images), f"{prefix} has no images", errors)
        if not isinstance(images, list):
            continue
        seen_files: set[str] = set()
        seen_indexes: set[int] = set()
        for item in images:
            if not isinstance(item, dict):
                errors.append(f"{prefix} contains a non-object image")
                continue
            relative = item.get("file")
            image_index = item.get("image_index")
            require(
                isinstance(relative, str) and relative not in seen_files,
                f"{prefix} contains a missing/duplicate image path",
                errors,
            )
            require(
                isinstance(image_index, int) and image_index not in seen_indexes,
                f"{prefix} contains a missing/duplicate image index",
                errors,
            )
            if isinstance(image_index, int):
                seen_indexes.add(image_index)
            if not isinstance(relative, str):
                continue
            seen_files.add(relative)
            image_count += 1
            path = manifest_path.parent / relative
            require(path.is_file(), f"missing evidence file: {path.relative_to(ROOT)}", errors)
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                require(digest == item.get("sha256"), f"hash mismatch: {path.relative_to(ROOT)}", errors)
            require(
                item.get("recheck_in_cn_test") is True,
                f"pre-client image must be marked for CN recheck: {relative}",
                errors,
            )
        actual_files = {
            path.relative_to(manifest_path.parent).as_posix()
            for path in manifest_path.parent.glob("images/*")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        }
        require(
            actual_files == seen_files,
            f"manifest/file mismatch in {manifest_path.parent.relative_to(ROOT)}",
            errors,
        )
    return len(manifest_paths), image_count


def validate_icon_evidence(source_ids: set[str], errors: list[str]) -> tuple[int, int]:
    icon_root = ROOT / "research" / "evidence" / "icons"
    catalog_path = icon_root / "catalog.json"
    schema_path = icon_root / "catalog.schema.json"
    require(catalog_path.is_file(), "icon evidence catalog is missing", errors)
    require(schema_path.is_file(), "icon evidence schema is missing", errors)
    if not catalog_path.is_file() or not schema_path.is_file():
        return 0, 0

    catalog = load_json(catalog_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for schema_error in sorted(validator.iter_errors(catalog), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in schema_error.path) or "<root>"
        errors.append(f"icon catalog schema error at {location}: {schema_error.message}")
    if not isinstance(catalog, dict) or not isinstance(catalog.get("samples"), list):
        errors.append("icon catalog must contain a samples array")
        return 0, 0

    resampling = {
        "nearest": Image.Resampling.NEAREST,
        "bilinear": Image.Resampling.BILINEAR,
        "bicubic": Image.Resampling.BICUBIC,
        "lanczos": Image.Resampling.LANCZOS,
    }
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    icon_keys: set[str] = set()

    for index, sample in enumerate(catalog["samples"]):
        prefix = f"icon samples[{index}]"
        require(isinstance(sample, dict), f"{prefix} must be an object", errors)
        if not isinstance(sample, dict):
            continue

        sample_id = sample.get("id")
        require(isinstance(sample_id, str) and sample_id not in seen_ids,
                f"{prefix} has a missing/duplicate id", errors)
        if isinstance(sample_id, str):
            seen_ids.add(sample_id)
            prefix = f"icon sample {sample_id}"
        icon_key = sample.get("icon_key")
        if isinstance(icon_key, str):
            icon_keys.add(icon_key)
        require(sample.get("source_id") in source_ids,
                f"{prefix} references an unknown source_id", errors)

        relative_output = sample.get("file")
        require(isinstance(relative_output, str) and relative_output not in seen_files,
                f"{prefix} has a missing/duplicate crop file", errors)
        if not isinstance(relative_output, str):
            continue
        seen_files.add(relative_output)
        output = icon_root / relative_output

        relative_parent = sample.get("parent_frame")
        require(isinstance(relative_parent, str), f"{prefix} has no parent frame", errors)
        if not isinstance(relative_parent, str):
            continue
        parent = ROOT / relative_parent
        require(parent.is_file(), f"{prefix} parent frame is missing: {relative_parent}", errors)
        if not parent.is_file():
            continue

        parent_hash = hashlib.sha256(parent.read_bytes()).hexdigest()
        require(parent_hash == sample.get("parent_sha256"),
                f"{prefix} parent hash mismatch", errors)
        manifest_path = parent.parent.parent / "manifest.json"
        require(manifest_path.is_file(), f"{prefix} parent has no evidence manifest", errors)
        if manifest_path.is_file():
            manifest = load_json(manifest_path)
            require(manifest.get("source_id") == sample.get("source_id"),
                    f"{prefix} source_id differs from parent manifest", errors)
            manifest_frames = manifest.get("frames", manifest.get("images", []))
            parent_entry = next(
                (
                    frame for frame in manifest_frames
                    if isinstance(frame, dict)
                    and (manifest_path.parent / str(frame.get("file"))).resolve() == parent.resolve()
                ),
                None,
            )
            require(parent_entry is not None, f"{prefix} parent is absent from its manifest", errors)
            if isinstance(parent_entry, dict):
                require(parent_entry.get("sha256") == parent_hash,
                        f"{prefix} parent manifest hash mismatch", errors)

        require(output.is_file(), f"{prefix} crop file is missing: {relative_output}", errors)
        if not output.is_file():
            continue
        output_hash = hashlib.sha256(output.read_bytes()).hexdigest()
        require(output_hash == sample.get("sha256"), f"{prefix} crop hash mismatch", errors)

        crop = sample.get("crop")
        scale = sample.get("scale")
        if not isinstance(crop, dict) or not isinstance(scale, dict):
            continue
        try:
            x = int(crop["x"])
            y = int(crop["y"])
            width = int(crop["width"])
            height = int(crop["height"])
            with Image.open(parent) as parent_image:
                parent_image.load()
                in_bounds = (
                    x >= 0 and y >= 0 and width > 0 and height > 0
                    and x + width <= parent_image.width
                    and y + height <= parent_image.height
                )
                require(in_bounds, f"{prefix} crop exceeds parent bounds", errors)
                if not in_bounds:
                    continue
                expected = parent_image.crop((x, y, x + width, y + height))
                if scale.get("applied") is True:
                    algorithm = scale.get("algorithm")
                    if algorithm in resampling:
                        expected = expected.resize(
                            (int(scale["output_width"]), int(scale["output_height"])),
                            resampling[algorithm],
                        )
                with Image.open(output) as actual:
                    actual.load()
                    dimensions = sample.get("dimensions")
                    require(
                        isinstance(dimensions, list)
                        and dimensions == [actual.width, actual.height],
                        f"{prefix} dimensions mismatch",
                        errors,
                    )
                    require(actual.mode == expected.mode,
                            f"{prefix} image mode differs from exact parent crop", errors)
                    if actual.mode == expected.mode and actual.size == expected.size:
                        require(ImageChops.difference(actual, expected).getbbox() is None,
                                f"{prefix} pixels differ from declared crop", errors)
                    else:
                        require(False, f"{prefix} size differs from declared crop", errors)
        except (KeyError, TypeError, ValueError, OSError) as error:
            errors.append(f"{prefix} cannot be verified: {error}")

    actual_files = {
        path.relative_to(icon_root).as_posix()
        for path in (icon_root / "crops").glob("*.png")
        if path.is_file()
    }
    require(actual_files == seen_files, "icon catalog/file mismatch", errors)
    return len(seen_ids), len(icon_keys)


def validate_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    ignored_parts = {".git", "node_modules", "raw", "work"}
    documents = sorted(
        path for path in ROOT.rglob("*.md")
        if not any(part in ignored_parts for part in path.relative_to(ROOT).parts)
    )
    for document in documents:
        text = document.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = (document.parent / target).resolve()
            require(resolved.exists(),
                    f"broken local link in {document.relative_to(ROOT)}: {raw_target}", errors)


def main() -> int:
    errors: list[str] = []
    validate_interface(errors)
    validate_no_pipeline_input(errors)
    validate_no_python_input(errors)
    validate_policy(errors)
    source_ids = validate_catalog(errors)
    manifest_count, frame_count = validate_evidence(source_ids, errors)
    still_manifest_count, still_image_count = validate_still_evidence(source_ids, errors)
    icon_sample_count, icon_key_count = validate_icon_evidence(source_ids, errors)
    validate_markdown_links(errors)
    if errors:
        print("Research scaffold validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Research scaffold OK: "
        f"{len(source_ids)} sources, {manifest_count} video manifests, {frame_count} frames; "
        f"{still_manifest_count} still manifests, {still_image_count} still images; "
        f"{icon_sample_count} icon crops across {icon_key_count} keys; "
        "all evidence hashes and crop pixels verified."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
