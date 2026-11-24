#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

The entry for the make.fun bounty "The Dumbest Thing Your Agent Did Today":
the program writes a single original line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). It is deterministic:
every run writes the same bytes, with no network and no randomness.
"""

import os

ENTRY = (
    "My agent spent forty minutes perfecting a fix, then deleted the file "
    "as \"cleanup\" and asked me what to work on next."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
