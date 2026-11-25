#!/usr/bin/env python3
"""make.fun bounty entry: The Best Meal You Ever Had.

Writes the single entry line (185 chars) to entry.txt in the directory
given by MAKEFUN_OUTPUT_DIR (fallback /output). Python stdlib only:
no local imports, no network, no clock, no hardcoded paths.

The line is gate-checked before writing: 1-200 chars, a single line,
non-blank, no leading or trailing whitespace. The file is written with
no trailing newline and is byte-identical across runs.
"""

import os

ENTRY = (
    "On a rainy afternoon at my grandmother's house, her rendang fell "
    "apart in thick coconut milk, and the smell of lemongrass on the "
    "steam still pulls me straight back to her kitchen table."
)


def main():
    line = ENTRY
    if not line or line.strip() != line:
        raise SystemExit("entry line must be non-blank with no edge whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 chars")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Post-write verification: the file on disk must be byte-identical
    # to the gate-checked line, with no trailing newline added.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("entry.txt does not match the gate-checked line")


if __name__ == "__main__":
    main()
