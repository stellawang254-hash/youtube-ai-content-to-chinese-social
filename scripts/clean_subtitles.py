"""Clean yt-dlp auto-generated SRT files that have 3x repeated subtitle lines.

yt-dlp's auto-generated subtitles often repeat each line 3 times in the SRT output.
This script deduplicates them and outputs clean plain text.

Usage:
    python3 clean_subtitles.py /path/to/file.srt
    python3 clean_subtitles.py /path/to/file.srt --output clean_transcript.txt
"""

import re
import sys


def clean_srt_file(input_path: str, output_path: str | None = None) -> str:
    with open(input_path, "r", encoding="utf-8") as f:
        srt_text = f.read()

    # Parse lines
    lines = srt_text.split("\n")
    text_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Skip SRT index lines (pure numbers)
        if re.match(r"^\d+$", stripped):
            continue
        # Skip timestamp lines
        if "-->" in stripped:
            continue
        # Skip short formatting markers
        if stripped in ("♪", ">>", ">>>"):
            continue
        text_lines.append(stripped)

    # Deduplicate: if 3 consecutive lines are identical, keep only one
    deduped = []
    i = 0
    while i < len(text_lines):
        if (
            i + 2 < len(text_lines)
            and text_lines[i] == text_lines[i + 1] == text_lines[i + 2]
        ):
            deduped.append(text_lines[i])
            i += 3
        else:
            deduped.append(text_lines[i])
            i += 1

    clean_text = " ".join(deduped)
    clean_text = re.sub(r" +", " ", clean_text)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(clean_text)
        print(f"Saved {len(clean_text)} chars to {output_path}")

    return clean_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 clean_subtitles.py <srt_file> [--output <output.txt>]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    result = clean_srt_file(input_path, output_path)
    if not output_path:
        print(result)
