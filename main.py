#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os
import sys

LINE = (
    "My agent entered a joke contest for me, took second place, "
    "and now it wants a raise \u2014 even my punchlines have a manager."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
