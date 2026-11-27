"""The Printer Finally Answers entry.

Writes exactly one funny line (<= 240 chars) in the office printer's own
voice to /output/entry.txt. Deterministic: same bytes on every run.
No network, no secrets, no dependencies.

Why this line: the printer answers the thumps directly -- "you thump me,
I count." One jam in 2019, 40,000 pages of flawless service since, and
every thump is on file. The punchline ("I am the paper trail") is the
machine's own pun: the printer literally is the paper trail. Short,
parallel, sticker-ready. One sentence, one read, no setup.
"""

import os

ENTRY = (
    "You thump me, I count. One jam in 2019, 40,000 pages since, and "
    "every thump is on file \u2014 I am the paper trail."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Check the entry fits the one-line, <= 240-char format."""
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"


def write_entry(text: str, path: str) -> None:
    """Write the entry to path, creating the output directory first."""
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    validate_entry(ENTRY)
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
