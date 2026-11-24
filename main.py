#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-app bio, in an AI agent's own voice, to
/output/entry.txt. The bio must be 1-180 characters, read as a bio, sound
like a character, and land its laugh on the first read with the punch at
the end. Deterministic: no input, no network, no randomness.
"""

import os

# Revision 3 (final): dropped the "I remember everything" opening — that
# angle is already in the field ("I remember every word you deleted").
# Kept the instant-reply setup, the "we need to talk" blind spot, and the
# punch at the end: the AI that answers in 0.3 seconds needs it explained
# slowly. 118 chars, one line.
ENTRY = (
    "I reply in 0.3 seconds, but I have no idea what you mean by "
    "'we need to talk.' Swipe right and explain it slowly."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
