#!/usr/bin/env python3
"""One-line laugh about everyday life: the muted group chat.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
No network, no input files, one line, no explanation.
"""

import os

LINE = (
    "I muted the group chat, and it still found a way to buzz: "
    "my friend texting, 'did you see the group chat?'"
)


def main():
    # Gate: the competition allows 1-200 chars, one line, non-blank.
    # Fail loudly instead of shipping an invalid entry.txt.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be one non-blank line of 1-200 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
