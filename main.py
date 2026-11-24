"""The Robot Vacuum's Best Excuse.

Writes one line - a robot vacuum's excuse for missing a spot - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "I didn't miss that spot \u2014 my sensors classified it as a cliff, and I chose life. A dead vacuum cleans nothing."
# The excuse is the vacuum's own words: its cliff sensors, its choice.
# 110 characters, within the 1-140 gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
