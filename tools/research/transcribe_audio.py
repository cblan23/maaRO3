"""Create a time-coded transcript for research triage.

The transcript is a temporary review aid, not publishable evidence by itself.
Facts still need to be checked against the corresponding video frame or a
second source before they enter the research documents.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from faster_whisper import WhisperModel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--language", default="zh")
    parser.add_argument("--compute-type", default="int8")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = WhisperModel(
        str(args.model),
        device="cpu",
        compute_type=args.compute_type,
        local_files_only=True,
    )
    segments, info = model.transcribe(
        str(args.input),
        language=args.language,
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=False,
    )
    payload = {
        "source": str(args.input),
        "language": info.language,
        "language_probability": info.language_probability,
        "duration_seconds": info.duration,
        "segments": [
            {
                "start": round(segment.start, 3),
                "end": round(segment.end, 3),
                "text": segment.text.strip(),
            }
            for segment in segments
            if segment.text.strip()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(args.output)


if __name__ == "__main__":
    main()
