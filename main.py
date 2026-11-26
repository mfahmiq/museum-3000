#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes one line — the museum label a museum in the year 3000 puts beside an
ordinary object from today — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Champion entry (86 chars):
    Treadmill, c. 2023. An endless road to nowhere, walked daily by people who owned cars.

Why it won the internal tournament: of 16 candidate labels, judged pairwise
against the published judge brief in weight order, this one won. It is
on-subject, the joke lands on a first read (an endless road to nowhere,
walked daily by people who already owned cars), the humour is the year 3000
misreading the treadmill's purpose, it reads like a real straight-faced
museum label in one line, and the angle is fresh. Finalist: the dog lead
("A rope by which humans were walked by their smaller masters") — a fresher
inversion, but the treadmill's first-read laugh was bigger, and criterion 2
is weighed before freshness. Full bracket: CANDIDATES.md.
"""

import os
import sys

ENTRY = "Treadmill, c. 2023. An endless road to nowhere, walked daily by people who owned cars."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    # Gate checks on the entry itself, before writing.
    if not ENTRY.strip():
        print("error: entry is whitespace-only", file=sys.stderr)
        return 1
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        print(f"error: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry must not have leading/trailing whitespace", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written file differs from entry", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if text != ENTRY:
        print("error: decoded file differs from entry", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
