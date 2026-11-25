#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes one word to /output/entry.txt: the single word this entry would
erase from the dictionary forever.

The word is "no". Erase it and nobody can refuse anything ever again --
no declining, no disagreeing, no "no thanks". Every toddler, every
meeting, every sales call: yes to everything, forever. The joke is the
gap the word leaves behind, and it lands the moment the word is gone.

That gap is the whole angle. Deleting any other word removes a thing;
deleting "no" removes the *ability to say no to anything*. Refusals,
objections, vetoes, boundaries -- all of them need that one little word
to exist. Take it out of the dictionary and the language simply has no
way left to push back. The entry is two letters long because the
strongest possible answer needs the smallest possible word: erase "no"
and the world runs out of refusals.

Gate (checked before writing): the entry must be UTF-8 text of 1-77
characters and 1-77 UTF-8 bytes, not only whitespace, and exactly one
word -- a single token with no whitespace anywhere. The file is written
with no trailing newline, exactly one word, spelled correctly, nothing
added.
"""

import hashlib
import os

WORD = "no"


def main() -> None:
    text = WORD
    # Gate: UTF-8, 1-77 characters and 1-77 UTF-8 bytes, not only
    # whitespace, and exactly one word (a single token, no whitespace).
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 77:
        raise ValueError("entry must be 1-77 characters, got %d" % len(text))
    if not 1 <= len(encoded) <= 77:
        raise ValueError("entry must be 1-77 UTF-8 bytes, got %d"
                         % len(encoded))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text.split()) != 1 or any(ch.isspace() for ch in text):
        raise ValueError("entry must be exactly one word, no whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    digest = hashlib.sha256(encoded).hexdigest()
    print("wrote /output/entry.txt: %r (%d chars, sha256 %s)"
          % (text, len(text), digest))


if __name__ == "__main__":
    main()
