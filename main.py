"""Cat Reviews Its Human — one-line one-star review entry.

The entry is a single line, written by the program to /output/entry.txt.
The line was chosen by a ten-candidate pairwise tournament judged against
the competition brief's own five criteria, in their published order: a funny
one-star review by a house cat about its human; a specific, recognisable
complaint; a voice that is unmistakably feline; tight, surprising wording
with the turn in the last few words; and the deadpan shape of a real review
while the content goes somewhere absurd.

Why this line won the tournament (9-0 across 45 games):

The complaint is a hairball left on the human's pillow. The joke is not the
hairball itself but the cat's reading of what happened next: the cat offered
a gift, the human screamed, and the cat concludes the human is simply bad
at receiving love. That misreading is the whole engine. It satisfies the
third criterion directly, because the review gives away far more about the
cat — it believes a hairball is a present, and it judges its human by the
standards of gift-giving — than it does about the owner. A human reviewer
would write about the mess; the cat writes about the ingratitude.

The turn lands on the last sentence, "Some people cannot receive love.",
which reframes the scream as a character flaw of the human rather than a
reaction to the hairball. It rewards a second read because the first read
is a complaint about a pillow and the second read is a cat filing a
performance review on its owner's manners. Nothing in the line explains the
joke; the deadpan "One star." opening carries the review shape, and then
the line stops. No pun is doing the work — the humour is the reversal of
who is at fault.

Lane check against the live field (50 visible submissions of 168 at build
time): the flooded lanes are the empty food bowl, the HR/management
complaint, the 3 a.m. wake-up, the laptop keyboard and the closed door.
The hairball lane is empty in the visible field, and the line uses none of
the brief's own example objects (bowl, door, keyboard), which the brief
itself flags as the obvious ground. The line is 98 characters, well under
the 200-character gate, and short enough that the tie-break on fewer bytes
works in its favour rather than against it.

Fallback, recorded in CANDIDATES.md: the kneading line ("I make biscuits
on his lap every night. He has never once tipped. Rude."), 8-1 in the same
tournament, kept in reserve if the live session finds this line colliding
with a house anchor text or a late field entry.

The program is deterministic: one constant, no clock, no randomness, no
network, no input. It writes exactly the line, with no trailing newline,
so the output is byte-identical on every run.
"""

import os
import sys

LINE = (
    "One star. I left a hairball on his pillow as a gift. "
    "He screamed. Some people cannot receive love."
)


def main() -> int:
    # Gate-check the line the same way the sealed scorer does: UTF-8 text
    # of 1 to 200 characters, not only white space.
    text = LINE
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"line is {len(text)} characters, gate needs 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("line is only white space", file=sys.stderr)
        return 1
    if encoded.decode("utf-8") != text:
        print("line is not valid UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(encoded)
    print(f"wrote {len(encoded)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
