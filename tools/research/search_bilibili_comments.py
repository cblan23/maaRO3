"""Search public Bilibili comments for RO3 review candidates.

Comments are locator/context material only.  They have no video timestamp and
must never be promoted to UI evidence without reviewing the corresponding
video or another direct visual source.  The script uses public, no-account
endpoints and does not read browser cookies.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import zlib


USER_AGENT = "Mozilla/5.0 maaRO3-public-research/1.0"
BVID_PATTERN = re.compile(r"BV[0-9A-Za-z]{10}")
MIXIN_KEY_ENC_TAB = (
    46, 47, 18, 2, 53, 8, 23, 32, 15, 50, 10, 31, 58, 3, 45, 35,
    27, 43, 5, 49, 33, 9, 42, 19, 29, 28, 14, 39, 12, 38, 41, 13,
    37, 48, 7, 16, 24, 55, 40, 61, 26, 17, 0, 1, 60, 51, 30, 4,
    22, 25, 54, 21, 56, 59, 6, 63, 57, 62, 11, 36, 20, 34, 44, 52,
)
DEFAULT_TERMS = (
    "满包",
    "滿包",
    "背包满",
    "背包滿",
    "背包已满",
    "背包已滿",
    "背包快满",
    "背包快滿",
    "仓库",
    "倉庫",
    "疲劳",
    "疲勞",
    "低倍",
    "不掉东西",
    "不掉東西",
    "不加经验",
    "不加經驗",
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
    aid: int
    video_title: str
    video_owner: str
    rpid: int
    root_rpid: int
    parent_rpid: int
    username: str
    created_at_utc: str
    likes: int
    text: str
    matched_terms: tuple[str, ...]
    root_text: str
    thread_replies: tuple[str, ...]


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
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--page-size", type=int, default=20)
    parser.add_argument("--max-pages", type=int, default=50)
    parser.add_argument("--max-thread-pages", type=int, default=20)
    parser.add_argument(
        "--deep-all-threads",
        action="store_true",
        help=(
            "Fetch every nested reply page. By default only threads whose root "
            "or inline preview matches a term are expanded, reducing rate limits."
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 6:
        parser.error("--workers must be between 1 and 6")
    if args.page_size < 1 or args.page_size > 20:
        parser.error("--page-size must be between 1 and 20")
    if args.max_pages < 1 or args.max_thread_pages < 1:
        parser.error("page limits must be positive")
    for bvid in args.bvid:
        if not BVID_PATTERN.fullmatch(bvid):
            parser.error(f"Invalid BVID: {bvid}")
    return args


def request_json(
    url: str,
    *,
    referer: str,
    attempts: int = 4,
    allowed_codes: tuple[int, ...] = (0,),
) -> dict:
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
                    payload = gzip.decompress(payload)
                elif encoding == "deflate":
                    try:
                        payload = zlib.decompress(payload)
                    except zlib.error:
                        payload = zlib.decompress(payload, -zlib.MAX_WBITS)
            value = json.loads(payload.decode("utf-8"))
            if value.get("code") not in allowed_codes:
                raise RuntimeError(f"Bilibili API: {value.get('message')}")
            return value
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


def fetch_wbi_mixin_key() -> str:
    value = request_json(
        "https://api.bilibili.com/x/web-interface/nav",
        referer="https://www.bilibili.com/",
        allowed_codes=(0, -101),
    )
    wbi = (value.get("data") or {}).get("wbi_img") or {}
    keys: list[str] = []
    for field in ("img_url", "sub_url"):
        url = str(wbi.get(field) or "")
        stem = url.rsplit("/", 1)[-1].split(".", 1)[0]
        if len(stem) != 32:
            raise RuntimeError(f"Invalid WBI {field}: {url!r}")
        keys.append(stem)
    raw = "".join(keys)
    return "".join(raw[index] for index in MIXIN_KEY_ENC_TAB)[:32]


def sign_wbi(params: dict[str, object], mixin_key: str) -> str:
    normalized = {key: str(value) for key, value in params.items()}
    normalized["wts"] = str(int(time.time()))
    for key, value in normalized.items():
        normalized[key] = "".join(char for char in value if char not in "!'()*")
    canonical = urlencode(sorted(normalized.items()))
    normalized["w_rid"] = hashlib.md5(
        (canonical + mixin_key).encode("utf-8")
    ).hexdigest()
    return urlencode(normalized)


def fetch_view(bvid: str) -> dict:
    referer = f"https://www.bilibili.com/video/{bvid}/"
    value = request_json(
        "https://api.bilibili.com/x/web-interface/view?"
        + urlencode({"bvid": bvid}),
        referer=referer,
    )
    return value["data"]


def fetch_reply_cursor(
    aid: int,
    bvid: str,
    pagination_offset: str,
    mixin_key: str,
) -> dict:
    params = {
        "type": 1,
        "oid": aid,
        "mode": 3,
        "plat": 1,
        "seek_rpid": "",
        "web_location": 1315875,
        "pagination_str": json.dumps(
            {"offset": pagination_offset}, ensure_ascii=False, separators=(",", ":")
        ),
    }
    query = sign_wbi(params, mixin_key)
    return request_json(
        f"https://api.bilibili.com/x/v2/reply/wbi/main?{query}",
        referer=f"https://www.bilibili.com/video/{bvid}/",
    ).get("data") or {}


def fetch_thread_page(
    aid: int,
    bvid: str,
    root_rpid: int,
    page: int,
    page_size: int,
) -> dict:
    query = urlencode(
        {
            "type": 1,
            "oid": aid,
            "root": root_rpid,
            "pn": page,
            "ps": page_size,
        }
    )
    return request_json(
        f"https://api.bilibili.com/x/v2/reply/reply?{query}",
        referer=f"https://www.bilibili.com/video/{bvid}/",
    ).get("data") or {}


def normalize_reply(reply: dict) -> dict:
    member = reply.get("member") or {}
    content = reply.get("content") or {}
    return {
        "rpid": int(reply.get("rpid") or 0),
        "root": int(reply.get("root") or 0),
        "parent": int(reply.get("parent") or 0),
        "username": str(member.get("uname") or ""),
        "ctime": int(reply.get("ctime") or 0),
        "likes": int(reply.get("like") or 0),
        "text": str(content.get("message") or ""),
        "rcount": int(reply.get("rcount") or 0),
    }


def fetch_complete_thread(
    aid: int,
    bvid: str,
    root: dict,
    page_size: int,
    max_pages: int,
) -> list[dict]:
    inline = [normalize_reply(item) for item in (root.get("replies") or [])]
    expected = int(root.get("rcount") or 0)
    if expected <= len(inline):
        return inline

    replies: dict[int, dict] = {item["rpid"]: item for item in inline}
    for page in range(1, max_pages + 1):
        data = fetch_thread_page(aid, bvid, int(root["rpid"]), page, page_size)
        rows = data.get("replies") or []
        for item in rows:
            normalized = normalize_reply(item)
            replies[normalized["rpid"]] = normalized
        count = int((data.get("page") or {}).get("count") or expected)
        if not rows or page >= math.ceil(count / page_size):
            break
    return sorted(replies.values(), key=lambda item: (item["ctime"], item["rpid"]))


def iso_utc(timestamp: int) -> str:
    if not timestamp:
        return ""
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()


def scan_video(
    bvid: str,
    terms: tuple[str, ...],
    mixin_key: str,
    page_size: int,
    max_pages: int,
    max_thread_pages: int,
    deep_all_threads: bool,
) -> dict:
    view = fetch_view(bvid)
    aid = int(view["aid"])
    roots: dict[int, dict] = {}
    declared_count = 0
    truncated = False

    pagination_offset = ""
    for request_index in range(max_pages):
        data = fetch_reply_cursor(aid, bvid, pagination_offset, mixin_key)
        cursor_info = data.get("cursor") or {}
        declared_count = int(cursor_info.get("all_count") or declared_count)
        rows = data.get("replies") or []
        for item in rows:
            roots[int(item["rpid"])] = item
        if bool(cursor_info.get("is_end")):
            break
        next_offset = str(
            (cursor_info.get("pagination_reply") or {}).get("next_offset") or ""
        )
        if not next_offset or next_offset == pagination_offset:
            truncated = bool(rows)
            break
        pagination_offset = next_offset
        if request_index + 1 == max_pages:
            truncated = True

    normalized_rows: list[tuple[dict, dict, list[dict]]] = []
    deep_threads_fetched = 0
    nested_replies_declared = 0
    for raw_root in roots.values():
        root = normalize_reply(raw_root)
        inline_children = [
            normalize_reply(item) for item in (raw_root.get("replies") or [])
        ]
        nested_replies_declared += root["rcount"]
        probe = [root, *inline_children]
        probe_matches = any(
            any(term.casefold() in row["text"].casefold() for term in terms)
            for row in probe
        )
        if root["rcount"] > len(inline_children) and (
            deep_all_threads or probe_matches
        ):
            children = fetch_complete_thread(
                aid,
                bvid,
                raw_root,
                page_size,
                max_thread_pages,
            )
            deep_threads_fetched += 1
        else:
            children = inline_children
        normalized_rows.append((root, root, children))
        normalized_rows.extend((child, root, children) for child in children)

    matches: list[Match] = []
    for row, root, children in normalized_rows:
        folded = row["text"].casefold()
        hit = tuple(term for term in terms if term.casefold() in folded)
        if not hit:
            continue
        thread_preview = tuple(
            f"{child['username']}: {child['text']}" for child in children[:40]
        )
        matches.append(
            Match(
                bvid=bvid,
                aid=aid,
                video_title=str(view.get("title") or ""),
                video_owner=str((view.get("owner") or {}).get("name") or ""),
                rpid=row["rpid"],
                root_rpid=root["rpid"],
                parent_rpid=row["parent"],
                username=row["username"],
                created_at_utc=iso_utc(row["ctime"]),
                likes=row["likes"],
                text=row["text"],
                matched_terms=hit,
                root_text=root["text"],
                thread_replies=thread_preview,
            )
        )

    unique_comments = {row[0]["rpid"] for row in normalized_rows}
    return {
        "bvid": bvid,
        "aid": aid,
        "title": view.get("title"),
        "owner": (view.get("owner") or {}).get("name"),
        "duration_seconds": view.get("duration"),
        "declared_comment_count": declared_count,
        "comments_scanned": len(unique_comments),
        "root_comments_scanned": len(roots),
        "nested_replies_declared": nested_replies_declared,
        "nested_replies_observed": len(unique_comments) - len(roots),
        "deep_threads_fetched": deep_threads_fetched,
        "deep_all_threads": deep_all_threads,
        "truncated": truncated,
        "matches": [asdict(item) for item in matches],
    }


def main() -> None:
    args = parse_args()
    terms = tuple(dict.fromkeys(args.term or DEFAULT_TERMS))
    mixin_key = fetch_wbi_mixin_key()
    bvids = discover_catalog_bvids(args.catalog) | set(args.bvid)
    if not bvids:
        raise SystemExit("No BVIDs discovered; provide --catalog or --bvid")

    results: list[dict] = []
    errors: list[dict] = []

    def guarded_scan(bvid: str) -> tuple[str, dict | None, str | None]:
        try:
            result = scan_video(
                bvid,
                terms,
                mixin_key,
                args.page_size,
                args.max_pages,
                args.max_thread_pages,
                args.deep_all_threads,
            )
            return bvid, result, None
        except Exception as error:  # retain partial public-endpoint audit results
            return bvid, None, f"{type(error).__name__}: {error}"

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for bvid, result, error in executor.map(guarded_scan, sorted(bvids)):
            if result is not None:
                results.append(result)
            else:
                errors.append({"bvid": bvid, "error": error})

    matches = [item for result in results for item in result["matches"]]
    matches.sort(key=lambda item: (item["bvid"], item["created_at_utc"], item["rpid"]))
    report = {
        "terms": terms,
        "videos_discovered": len(bvids),
        "videos_scanned": len(results),
        "videos_failed": len(errors),
        "comments_scanned": sum(item["comments_scanned"] for item in results),
        "match_count": len(matches),
        "matches": matches,
        "videos": [
            {key: value for key, value in item.items() if key != "matches"}
            for item in sorted(results, key=lambda row: row["bvid"])
        ],
        "errors": errors,
        "warning": (
            "Comments have no reliable video timestamp and are locator/context "
            "material only; they are not visual evidence."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"Scanned {report['videos_scanned']}/{report['videos_discovered']} videos, "
        f"{report['comments_scanned']} comments, {report['match_count']} matches; "
        f"report: {args.output}"
    )


if __name__ == "__main__":
    main()
