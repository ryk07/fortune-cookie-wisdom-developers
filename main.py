#!/usr/bin/env python3
"""Write one original fortune-cookie line for a software developer.

The line, in the voice of a fortune cookie: oracular, second person, one
short balanced sentence that lands in a single breath.

    You will deploy on Friday, and the weekend will keep its own changelog.

It names a specific true developer pain -- the Friday deploy -- and turns
it in the last few words: the weekend itself keeps a changelog, a quiet
double meaning (the record of what broke, and the weekend remembering every
shortcut). The line is 71 characters, inside the 120-character cap.
"""

import os
from pathlib import Path

LINE = "You will deploy on Friday, and the weekend will keep its own changelog."


def output_dir() -> Path:
    """Resolve the output directory without ever trusting the cwd."""
    here = Path(__file__).resolve().parent
    _ = here
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 120:
        raise ValueError("fortune line must be 1-120 characters")
    out_path = output_dir() / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
