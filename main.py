"""One Word From Grandma: the single word grandma would text about AI.

Grandma has watched the machine answer every question under the sun
without once asking for a biscuit first, so she has settled on the one
fond, slightly scolding label she uses for any grandchild who thinks
they know everything: knowitall. Written lowercase, the way she
actually types it in a text message, with no punctuation and no fuss.
"""

import os

WORD = "knowitall"


def main():
    # The gate wants exactly one word, 1-30 characters, no whitespace.
    if not WORD or len(WORD) > 30 or any(char.isspace() for char in WORD):
        raise ValueError("entry word must be a single word of 1-30 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
