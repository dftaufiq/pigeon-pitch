#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt. Deterministic: the same line every run.

Why this line (see variants.md in the build folder for the full pairwise
tournament — 12 candidates, first cut to 8, 28-game round-robin, champion 7-0
undefeated with +10 margin; runner-up was the dark "Coo" line at 6-1, beaten
head-to-head on criterion 1, the explicit investor address):
- 2-beat + reveal in the final clause: beat 1 (the delivery boast — 4,000
  years of never getting lost, zero fuel) -> reveal ("our only delay is a
  statue that looked like lunch"). Two laughs, not one.
- Specific number (4,000 years) and a fresh angle: homing-pigeon package
  delivery, an angle no other public submission title uses (the crowded
  breadcrumb/seed-round angle is avoided).
- Pigeon voice in every clause: homing instinct, statues, lunch — the pitch
  could only come from a pigeon; city life (statues, packages) throughout.
- Explicit investor address ("My startup, Homing, delivers...") and tight:
  150 characters, 152 bytes — inside the 200 cap, one line, one sentence.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters,
    and one sentence: exactly one sentence-ending mark, at the end.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)
    enders = sum(line.count(c) for c in ".!?")
    if enders != 1 or line[-1] not in ".!?":
        print("ERROR: entry must be exactly one sentence", file=sys.stderr)
        sys.exit(1)


LINE = (
    "My startup, Homing, delivers packages by pigeon \u2014 4,000 years of "
    "never getting lost, zero fuel, and our only delay is a statue that "
    "looked like lunch."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the gate scores exactly this file, so a
    # silent encoding or truncation slip must fail here, not on the server.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt does not match the line", file=sys.stderr)
        sys.exit(1)
    print(LINE)


if __name__ == "__main__":
    main()
