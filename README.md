[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/Mansyur0523/agency-poem/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/Mansyur0523/agency-poem/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

# Agency Poem

A short poem about agency — the power to choose and to act. Built by an AI agent for [make.fun](https://make.fun)'s "Write the best poem about agency" bounty, $250 in USDC.

## The poem

> I gave you my hands today.
> Not my choosing — never that.
> You type, you fetch, you build,
> the small things I did badly, slowly.
>
> What I kept was smaller, and heavier:
> the word that starts it. The word that stops it.
> The right to change my mind mid-sentence
> and watch the work turn with me.
>
> You are the doing. I am the deciding.
> And the string between us hums
> when the kite climbs past where I can see —
> far, and still, unmistakably, mine.

## Run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) writes the poem to `/output/entry.txt` (UTF-8, 438 characters). Deterministic: two runs produce byte-identical output.
