#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line, under-280-character 1-star review, in the voice
of a houseplant reviewing its human owner, to /output/entry.txt.

The line was chosen from 14 candidates scored against the judge's brief,
in the brief's own order:
  1. a one-line 1-star review by a houseplant about its human owner, with
     the plant's own grievance at the centre;
  2. funnier through a surprising turn / sharp plant's-eye grievance;
  3. sounds like a houseplant wrote it (water, light, soil, pots,
     repotting, being moved);
  4. reads as a genuine one-star review, clear complaint + reason for the
     single star, one line under 280 characters;
  5. fresh, specific detail, precise wording — no stock phrases about
     drama queens, dramatic wilting or being ignored.

Candidates (score out of 25) — see NOTES for the full table:
  R1  25.0  housewarming gift, parked on the fridge, dying in the dark,
            "would not photosynthesize again"  <-- CHOSEN
  R3  24.5  "plant dad" bio, dust and one ice cube since March
  R4  24.5  misted once a month like a priest blessing a sinner
  R2  23.5  repotted in 2019 into a pot with no drainage holes
  R5  23.0  talking is not water
  R8  23.0  kept alive out of guilt, a thimble a Sunday
  R6  22.5  Post-it saying "be strong" before a two-week holiday
  R12 22.5  watered once, on New Year's Day, as a resolution
  R14 22.0  last drink was condensation off his iced coffee
  R7  21.5  watered with leftover coffee
  R9  21.0  bought for the shelfie
  R10 21.0  lo-fi beats as sunlight
  R11 21.0  rotated a quarter-turn every Sunday
  R13 20.0  moved six times chasing "the light"

Why R1 wins: one grievance, centre stage (abandoned on top of the
fridge in the dark since the day it arrived); the closer parodies the
classic review sign-off "would not recommend" in pure plant voice —
"would not photosynthesize again" — which is simultaneously the joke,
the plant's-eye view, and the reason for the single star. Every word
is specific (housewarming gift, fridge, dark) and none of it is a stock
plant joke. 171 characters, one line, no trailing newline in the file
(the gate counts characters; a trailing newline would be part of the
text, so the file holds exactly the line).
"""

import os
import sys

# The chosen line: 171 characters, one line.
FINAL_LINE = (
    "I was a housewarming gift. He unwrapped me, parked me on top of "
    "the fridge, and I have been slowly dying in the dark ever since. "
    "One star: would not photosynthesize again."
)

MAX_CHARS = 279


def main() -> int:
    line = FINAL_LINE

    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 279 characters, not only white space.
    if not line or not line.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry is {len(line)} chars, over the 279 limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8 text

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    print(f"wrote {out_path}: {len(line)} chars")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
