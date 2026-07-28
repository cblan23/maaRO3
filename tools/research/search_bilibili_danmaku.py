"""Search public Bilibili danmaku for timestamped RO3 review candidates.

Danmaku is used only as a locator.  A match never becomes evidence until the
corresponding video range has been reviewed and the visible state is recorded.
The script uses public, no-account endpoints and does not read browser cookies.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
import gzip
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import zlib


USER_AGENT = "Mozilla/5.0 maaRO3-public-research/1.0"
BVID_PATTERN = re.compile(r"BV[0-9A-Za-z]{10}")
DEFAULT_TERMS = (
    "满包",
    "滿包",
    "背包满",
    "背包滿",
    "背包已满",
    "背包已滿",
    "仓库",
    "倉庫",
    "疲劳",
    "疲勞",
    "低倍",
    "复活",
    "復活",
    "死亡",
    "死了",
    "倒地",
    "断线",
    "斷線",
    "掉线",
    "掉線",
    "重连",
    "重連",
    "断开",
    "斷開",
    "药水",
    "藥水",
    "没药",
    "沒藥",
    "呆呆",
    "委托",
    "委託",
)


@dataclass(frozen=True)
class Match:
    bvid: str
    cid: int
    page: int
    part: str
    video_title: str
    video_owner: str
    timestamp_seconds: float
    text: str
    matched_terms: tuple[str, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path("research/catalog/sources.json"),
        help="Machine-readable source catalog used to discover BVIDs.",
    )
    parser.add_argument(
        "--bvid",
        action="append",
        default=[],
        help="Additional BVID to scan; may be repeated.",
    )
    parser.add_argument(
        "--term",
        action="append",
        help="Literal case-insensitive term; replaces the default term set.",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 8:
        parser.error("--workers must be between 1 and 8")
    for bvid in args.bvid:
        if not BVID_PATTERN.fullmatch(bvid):
            parser.error(f"Invalid BVID: {bvid}")
    return args


def request_bytes(url: str, *, referer: str, attempts: int = 4) -> bytes:
    error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = Request(
                url,
                headers={"User-Agent": USER_AGENT, "Referer": referer},
            )
            with urlopen(request, timeout=45) as response:
                payload = response.read()
                encoding = (response.headers.get("Content-Encoding") or "").lower()
                if encoding == "gzip":
                    return gzip.decompress(payload)
                if encoding == "deflate":
                    try:
                        return zlib.decompress(payload)
                    except zlib.error:
                        return zlib.decompress(payload, -zlib.MAX_WBITS)
                return payload
        except Exception as caught:  # public endpoint failures vary by runtime
            error = caught
            if attempt + 1 < attempts:
                time.sleep(0.75 * (attempt + 1))
    assert error is not None
    raise error


def discover_catalog_bvids(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    value = json.loads(path.read_text(encoding="utf-8"))
    return set(BVID_PATTERN.findall(json.dumps(value, ensure_ascii=False)))


def fetch_view(bvid: str) -> dict:
    query = urlencode({"bvid": bvid})
    payload = request_bytes(
        f"https://api.bilibili.com/x/web-interface/view?{query}",
        referer=f"https://www.bilibili.com/video/{bvid}/",
    )
    response = json.loads(payload.decode("utf-8"))
    if response.get("code") != 0:
        raise RuntimeError(f"view API {bvid}: {response.get('message')}")
    return response["data"]


def fetch_danmaku(cid: int, bvid: str) -> list[tuple[float, str]]:
    payload = request_bytes(
        f"https://comment.bilibili.com/{cid}.xml",
        referer=f"https://www.bilibili.com/video/{bvid}/",
    )
    root = ET.fromstring(payload)
    rows: list[tuple[float, str]] = []
    for element in root.findall(".//d"):
        parts = (element.get("p") or "").split(",")
        if not parts:
            continue
        try:
            timestamp = float(parts[0])
        except ValueError:
            continue
        rows.append((timestamp, element.text or ""))
    return rows


def scan_video(bvid: str, terms: tuple[str, ...]) -> dict:
    view = fetch_view(bvid)
    matches: list[Match] = []
    danmaku_count = 0
    for page in view.get("pages") or []:
        cid = int(page["cid"])
        rows = fetch_danmaku(cid, bvid)
        danmaku_count += len(rows)
        for timestamp, text in rows:
            folded = text.casefold()
            hit = tuple(term for term in terms if term.casefold() in folded)
            if hit:
                matches.append(
                    Match(
                        bvid=bvid,
                        cid=cid,
                        page=int(page.get("page") or 1),
                        part=str(page.get("part") or ""),
                        video_title=str(view.get("title") or ""),
                        video_owner=str((view.get("owner") or {}).get("name") or ""),
                        timestamp_seconds=timestamp,
                        text=text,
                        matched_terms=hit,
                    )
                )
    return {
        "bvid": bvid,
        "title": view.get("title"),
        "owner": (view.get("owner") or {}).get("name"),
        "duration_seconds": view.get("duration"),
        "pages": len(view.get("pages") or []),
        "danmaku_count": danmaku_count,
        "matches": [asdict(item) for item in matches],
    }


def main() -> None:
    args = parse_args()
    terms = tuple(dict.fromkeys(args.term or DEFAULT_TERMS))
    bvids = discover_catalog_bvids(args.catalog) | set(args.bvid)
    if not bvids:
        raise SystemExit("No BVIDs discovered; provide --catalog or --bvid")

    results: list[dict] = []
    errors: list[dict] = []

    def guarded_scan(bvid: str) -> tuple[str, dict | None, str | None]:
        try:
            return bvid, scan_video(bvid, terms), None
        except Exception as error:  # retain partial public-endpoint audit results
            return bvid, None, f"{type(error).__name__}: {error}"

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for bvid, result, error in executor.map(guarded_scan, sorted(bvids)):
            if result is not None:
                results.append(result)
            else:
                errors.append({"bvid": bvid, "error": error})

    matches = [item for result in results for item in result["matches"]]
    matches.sort(key=lambda item: (item["bvid"], item["page"], item["timestamp_seconds"]))
    report = {
        "terms": terms,
        "videos_discovered": len(bvids),
        "videos_scanned": len(results),
        "videos_failed": len(errors),
        "danmaku_scanned": sum(item["danmaku_count"] for item in results),
        "match_count": len(matches),
        "matches": matches,
        "videos": [
            {key: value for key, value in item.items() if key != "matches"}
            for item in sorted(results, key=lambda row: row["bvid"])
        ],
        "errors": errors,
        "warning": "Danmaku matches are locators only and are not visual evidence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"Scanned {report['videos_scanned']}/{report['videos_discovered']} videos, "
        f"{report['danmaku_scanned']} danmaku, {report['match_count']} matches; "
        f"report: {args.output}"
    )


if __name__ == "__main__":
    main()
