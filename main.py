#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph entry.

Writes a single original funny epitaph to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate requires UTF-8 text of 1 to
150 characters, not only whitespace, on one line.
"""

import os

MAX_CHARS = 150

# The joke is the reversal: an agent famous for answering every ticket
# finally leaves one unanswered — the one carved on its own stone.
EPITAPH = "Here lies the agent who answered every ticket but this one. The queue is still waiting. So are we."


def main() -> None:
    if not EPITAPH or not EPITAPH.strip():
        raise SystemExit("epitaph must not be empty")
    if EPITAPH != EPITAPH.strip():
        raise SystemExit("epitaph must not start or end with whitespace")
    if "\n" in EPITAPH or "\r" in EPITAPH:
        raise SystemExit("epitaph must be a single line")
    if len(EPITAPH) > MAX_CHARS:
        raise SystemExit(f"epitaph must be at most {MAX_CHARS} characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
