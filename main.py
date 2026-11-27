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
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_SIDE = 1024
JPEG_MAGIC = b"\xff\xd8\xff"


def jpeg_dimensions(data):
    """Read width and height from the first SOF marker of a JPEG."""
    pos = 2
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2: precision, h, w
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        pos += 2 + length
    raise ValueError("no SOF marker found in JPEG")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        sys.exit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(JPEG_MAGIC):
        sys.exit("entry.png does not start with JPEG magic bytes")
    width, height = jpeg_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        sys.exit(f"entry.png is {width}x{height}, over the 1024x1024 cap")

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
