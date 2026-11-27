#!/usr/bin/env python3
"""Entry for make.fun news-image-20261127: copy the poster to the output dir.

The poster (1024x1024, JPEG bytes under the entry.png name, under the
1 MiB cap) sits next to this file. The program just copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png) and checks the
copy is byte-identical, the right size, and really a JPEG. No network,
no randomness: every run writes the same bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
JPEG_MAGIC = b"\xff\xd8\xff"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        sys.exit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(JPEG_MAGIC):
        sys.exit("entry.png does not start with JPEG magic bytes")

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, target)

    with open(target, "rb") as fh:
        copied = fh.read()
    if copied != data:
        sys.exit("copy differs from the source image")
    digest = hashlib.sha256(copied).hexdigest()
    print(f"wrote {target}: {len(copied)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
