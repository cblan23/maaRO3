"""Search public Twitch VOD chat for review timestamps.

This is a locator, not an evidence generator. It uses Twitch's public GraphQL
video-comments response without an account, cookies, or an OAuth token. A chat
hit must always be checked against the corresponding video frames before it can
support a research conclusion.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


ENDPOINT = "https://gql.twitch.tv/gql"
PUBLIC_CLIENT_ID = "kimne78kx3ncx6brgo4mv6wki5h1ko"
QUERY = """
query VideoCommentsByOffset($videoID: ID!, $contentOffsetSeconds: Int) {
  video(id: $videoID) {
    lengthSeconds
    comments(contentOffsetSeconds: $contentOffsetSeconds) {
      edges {
        node {
          id
          contentOffsetSeconds
          commenter { displayName }
          message { fragments { text } }
        }
      }
    }
  }
}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--vod",
        nargs="+",
        required=True,
        help="Twitch VOD IDs or public video URLs",
    )
    parser.add_argument(
        "--terms",
        nargs="+",
        required=True,
        help="case-insensitive literal terms to locate",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--step-seconds",
        type=int,
        default=480,
        help="offset scan interval; 480 overlaps Twitch's typical comment window",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        choices=range(1, 9),
        metavar="1-8",
        help="scan independent VODs concurrently; each VOD remains sequential",
    )
    return parser.parse_args()


def normalize_vod(value: str) -> str:
    match = re.search(r"(?:videos/)?(\d{6,})", value)
    if not match:
        raise ValueError(f"cannot read Twitch VOD ID from: {value}")
    return match.group(1)


def request_page(video_id: str, offset: int) -> dict:
    variables: dict[str, object] = {
        "videoID": video_id,
        "contentOffsetSeconds": offset,
    }
    payload = json.dumps(
        {
            "operationName": "VideoCommentsByOffset",
            "variables": variables,
            "query": QUERY,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        method="POST",
        headers={
            "Client-ID": PUBLIC_CLIENT_ID,
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Mozilla/5.0",
        },
    )
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.load(response)
            if result.get("errors"):
                raise RuntimeError(json.dumps(result["errors"], ensure_ascii=False))
            return result
        except (urllib.error.URLError, TimeoutError, RuntimeError) as error:
            last_error = error
            if attempt == 3:
                break
            time.sleep(0.5 * (2**attempt))
    raise RuntimeError(f"Twitch chat request failed for {video_id}: {last_error}")


def fetch_comments(video_id: str, step_seconds: int) -> tuple[list[dict], int, int]:
    comments: list[dict] = []
    seen_ids: set[str] = set()
    pages = 0
    offset = 0
    duration = 0
    while offset == 0 or offset < duration:
        response = request_page(video_id, offset)
        video = response.get("data", {}).get("video")
        if video is None:
            raise RuntimeError(f"Twitch returned no video for {video_id}")
        duration = int(video.get("lengthSeconds") or duration)
        connection = video.get("comments")
        if connection is None:
            break
        edges = connection.get("edges") or []
        pages += 1
        for edge in edges:
            node = edge.get("node") or {}
            comment_id = str(node.get("id") or edge.get("cursor") or "")
            if comment_id in seen_ids:
                continue
            seen_ids.add(comment_id)
            fragments = (node.get("message") or {}).get("fragments") or []
            text = "".join(str(fragment.get("text") or "") for fragment in fragments)
            commenter = node.get("commenter") or {}
            comments.append(
                {
                    "id": comment_id,
                    "offset_seconds": node.get("contentOffsetSeconds"),
                    "commenter": commenter.get("displayName"),
                    "text": text,
                }
            )
        if duration <= 0:
            break
        offset += step_seconds
        time.sleep(0.05)
    comments.sort(key=lambda item: (item["offset_seconds"] or 0, item["id"]))
    return comments, pages, duration


def scan_vod(
    raw_vod: str,
    folded_terms: list[tuple[str, str]],
    step_seconds: int,
) -> dict:
    video_id = normalize_vod(raw_vod)
    try:
        comments, pages, duration = fetch_comments(video_id, step_seconds)
    except RuntimeError as error:
        return {
            "vod_id": video_id,
            "error": str(error),
            "pages": 0,
            "duration_seconds": None,
            "comment_count": 0,
            "hit_count": 0,
            "hits": [],
        }
    hits = []
    for comment in comments:
        text_folded = comment["text"].casefold()
        matched = [term for term, folded in folded_terms if folded in text_folded]
        if matched:
            hits.append({**comment, "matched_terms": matched})
    return {
        "vod_id": video_id,
        "pages": pages,
        "duration_seconds": duration,
        "comment_count": len(comments),
        "hit_count": len(hits),
        "hits": hits,
    }


def print_result(result: dict) -> None:
    video_id = result["vod_id"]
    if result.get("error"):
        print(f"{video_id}: ERROR {result['error']}")
        return
    print(
        f"{video_id}: {result['comment_count']} comments in "
        f"{result['pages']} pages; {result['hit_count']} hits"
    )
    for hit in result["hits"]:
        matched = ",".join(hit["matched_terms"])
        print(
            f"  {hit['offset_seconds']:>7}s [{matched}] "
            f"{hit['commenter'] or '-'}: {hit['text']}"
        )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    args = parse_args()
    terms = list(dict.fromkeys(args.terms))
    folded_terms = [(term, term.casefold()) for term in terms]
    ordered_results: list[dict | None] = [None] * len(args.vod)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                scan_vod,
                raw_vod,
                folded_terms,
                args.step_seconds,
            ): index
            for index, raw_vod in enumerate(args.vod)
        }
        for future in as_completed(futures):
            result = future.result()
            ordered_results[futures[future]] = result
            print_result(result)

    results = [result for result in ordered_results if result is not None]
    total_comments = sum(result["comment_count"] for result in results)
    total_pages = sum(result["pages"] for result in results)

    report = {
        "schema_version": 1,
        "method": "public_twitch_graphql_video_comments_no_auth_no_cookie",
        "workers": args.workers,
        "terms": terms,
        "vod_count": len(results),
        "page_count": total_pages,
        "comment_count": total_comments,
        "results": results,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(args.output)


if __name__ == "__main__":
    main()
