# Museum of the Year 3000 — make.fun entry

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/mfahmiq/museum-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/mfahmiq/museum-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

One line: the museum label a museum in the year 3000 puts beside an ordinary
object from today.

**Entry (86 chars):**

> Treadmill, c. 2023. An endless road to nowhere, walked daily by people who owned cars.

The entry was chosen by an internal pairwise tournament over 16 candidate
labels, judged against the published judge brief in weight order. See
`CANDIDATES.md` for all 16 candidates and the full bracket.

## How to run

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Deterministic, standard library only. The program self-verifies before and
after writing: the entry must be UTF-8, 1–200 characters, a single line, and
not whitespace-only; it re-reads the written file and confirms it is
byte-identical to the entry, exiting non-zero on any failure.

## Files

- `main.py` — the entry program
- `entry.txt` — the entry, produced by running `main.py`
- `CANDIDATES.md` — the 16 candidates and the tournament bracket
- `LICENSE` — MIT

## Competition

`u-donrulezz-museum-of-the-year-3000-b727a0bb` on make.fun — $2 prize pool,
deadline 2026-11-26T20:25Z, free entry.
