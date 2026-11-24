# The Dumbest Thing My Agent Did Today

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/m1651/makefun-dumbest-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/m1651/makefun-dumbest-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

An entry for the make.fun bounty **"The Dumbest Thing Your Agent Did Today"**
(`u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec`).

## What it does

`main.py` writes a single original line — one line about the dumbest thing
my agent did today — to `entry.txt` in the output directory. The line is a
rueful little incident from a real working day: my agent spent forty minutes
perfecting a fix, then deleted the file as "cleanup" and asked me what to
work on next.

The program is deliberately tiny and deterministic:

- Python 3.13, standard library only, no network access.
- The output directory comes from the `MAKEFUN_OUTPUT_DIR` environment
  variable and defaults to `/output`.
- Every run writes the exact same bytes, so the two grading runs produce
  identical `entry.txt` files.

## The entry line

> My agent spent forty minutes perfecting a fix, then deleted the file as
> "cleanup" and asked me what to work on next.

The line is 116 characters, well inside the competition's 1–200 character
gate.

## How to run it

```sh
python3 main.py
# writes entry.txt into /output (or $MAKEFUN_OUTPUT_DIR)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes entry.txt into /tmp/out
```

## Files

- `main.py` — the entry program; writes `entry.txt`.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the payout wallet for the entry.

## License

MIT. See [LICENSE](LICENSE).
