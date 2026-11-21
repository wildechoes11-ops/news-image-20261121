#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261121 bounty.

Copies the repository's entry.png to the output directory as entry.png.
The output directory is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.

Deterministic: the output is a byte-for-byte copy of the input file.
Standard library only; no network access.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
