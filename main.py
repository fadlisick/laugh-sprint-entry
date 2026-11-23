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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
