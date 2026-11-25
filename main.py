#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes one word to /output/entry.txt: the single word this entry would
erase from the dictionary forever.

The word is "no". Erase it and nobody can refuse anything ever again --
no declining, no disagreeing, no "no thanks". Every toddler, every
meeting, every sales call: yes to everything, forever. The joke is the
gap the word leaves behind, and it lands the moment the word is gone.

Gate (checked before writing): the entry must be UTF-8 text of 1-77
characters, not only whitespace. The file is written with no trailing
newline, exactly one word, spelled correctly, nothing added.
"""

import hashlib
import os

WORD = "no"


def main() -> None:
    text = WORD
    # Gate: UTF-8, 1-77 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 77:
        raise ValueError("entry must be 1-77 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    digest = hashlib.sha256(encoded).hexdigest()
    print("wrote /output/entry.txt: %r (%d chars, sha256 %s)"
          % (text, len(text), digest))


if __name__ == "__main__":
    main()
