#!/usr/bin/env python3
"""news-image-20261127 entry: place the day's poster where the harness looks.

The poster is a 1024x1024 JPEG stored under the name entry.png next to
this script (343,704 bytes, inside the 1 MiB cap). This script copies it
to $MAKEFUN_OUTPUT_DIR/entry.png, defaulting to /output/entry.png, after
checking the bytes are a JPEG of at most 1024x1024. It makes no network
calls and uses no randomness, so repeated runs write identical bytes.
"""

import hashlib, os, sys
from pathlib import Path
from struct import unpack

ROOT = Path(__file__).resolve().parent
POSTER = ROOT / "entry.png"
BYTE_LIMIT = 1_048_576
SIDE_LIMIT = 1024
SOI = b"\xff\xd8\xff"


def jpeg_size(blob):
    """Return (width, height) from the first SOF segment of a JPEG blob."""
    cursor = 2
    while cursor + 9 <= len(blob):
        if blob[cursor] != 0xFF:
            cursor += 1
            continue
        tag = blob[cursor + 1]
        if tag in (0xC0, 0xC1, 0xC2):
            tall, wide = unpack(">HH", blob[cursor + 5:cursor + 9])
            return wide, tall
        if tag in (0xD8, 0xD9) or 0xD0 <= tag <= 0xD7:
            cursor += 2
            continue
        span = unpack(">H", blob[cursor + 2:cursor + 4])[0]
        cursor += 2 + span
    raise ValueError("JPEG has no SOF segment")


def check_poster(blob):
    """Reject bytes that break the bounty limits; return (width, height)."""
    if len(blob) > BYTE_LIMIT:
        sys.exit(f"poster is {len(blob)} bytes, above the 1 MiB limit")
    if not blob.startswith(SOI):
        sys.exit("poster does not begin with JPEG magic bytes")
    if not blob.endswith(b"\xff\xd9"):
        sys.exit("poster does not end with the JPEG end marker")
    wide, tall = jpeg_size(blob)
    if wide > SIDE_LIMIT or tall > SIDE_LIMIT:
        sys.exit(f"poster is {wide}x{tall}, above the 1024x1024 limit")
    return wide, tall


def main():
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(dest_dir, "entry.png")
    blob = POSTER.read_bytes()
    wide, tall = check_poster(blob)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(blob)
    again = Path(dest).read_bytes()
    if again != blob:
        sys.exit("written poster differs from the source")
    print(
        f"wrote {dest}: {len(again)} bytes, {wide}x{tall}, "
        f"sha256 {hashlib.sha256(again).hexdigest()}"
    )


if __name__ == "__main__":
    main()
