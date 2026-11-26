#!/usr/bin/env python3
"""One Line, One Laugh - u-deysumbrella-one-line-one-laugh-e0cdcda9.

Writes a single funny one-liner (68 chars) to /output/entry.txt.
The line was chosen by a pairwise arena (10-20 candidates, shortlist 6,
two-way A/B vs the 3 gold-set lines) and beat the gold set consistently.
"""

import os
import sys

LINE = "My doctor told me to drink more water, so I cry eight glasses a day."


def main() -> int:
    if not (1 <= len(LINE) <= 140):
        print(f"line length {len(LINE)} out of gate 1-140", file=sys.stderr)
        return 1
    if "\n" in LINE.strip():
        print("line must be a single line", file=sys.stderr)
        return 1
    # No trailing newline: the gate counts characters, so write exactly the line.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
