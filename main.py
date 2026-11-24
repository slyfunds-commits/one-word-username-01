#!/usr/bin/env python3
"""One Word, One Username, One Reward — round 1 entry.

Writes our own make.fun handle to /output/entry.txt: exactly the 8 bytes
of "boss-lah", no trailing newline, no padding. Pure stdlib.
"""

import os

ENTRY = "boss-lah"

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

# Immediate self-check: the file must hold exactly the handle, nothing else.
with open("/output/entry.txt", "rb") as f:
    data = f.read()

assert data == ENTRY.encode("utf-8"), f"entry mismatch: {data!r}"
assert len(data) == 8, f"entry must be 8 bytes, got {len(data)}"
assert b"\n" not in data and b" " not in data, "entry must be one word, no padding"

# Text-mode read-back: the gate reads UTF-8 text of 1-30 chars, not whitespace.
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    text = f.read()

assert text == ENTRY and 1 <= len(text) <= 30, f"gate check failed: {text!r}"
print(f"wrote /output/entry.txt ({len(data)} bytes): {ENTRY}")
