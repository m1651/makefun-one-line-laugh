#!/usr/bin/env python3
"""The One Line Laugh — make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one original funny line (a single sentence, at most 200
characters) to /output/entry.txt. Deterministic: the same line every run.
Standard library only, no network.
"""

import os
import sys

LINE = (
    "I downloaded a meditation app to calm down, and now the only thing "
    "stressing me out is losing my 47-day streak."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, not only whitespace,
    standing alone as a single sentence. Fail loudly instead of writing
    an entry that can never be judged."""
    if not line or not line.strip():
        print("error: line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} characters, over the {MAX_CHARS} "
            "character limit",
            file=sys.stderr,
        )
        sys.exit(1)
    if line.count(".") != 1 or not line.rstrip().endswith("."):
        print("error: line must be exactly one sentence ending in '.'",
              file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
