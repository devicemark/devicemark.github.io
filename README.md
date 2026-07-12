# On-Device LLM Leaderboard (working name: `ondevice-leaderboard`)

The publication vessel for the on-device LLM leaderboard: the static site, the
deploy pipeline, the results dataset, and the receiving surfaces (submit / object).
**Private until the launch gate.** Naming is not final — see [`NAMING.md`](NAMING.md).

> This repo is a thin **deploy shell**. The site and the results are produced in
> the eval workspace (`~/code/coreai/leaderboard/`) and **synced in at launch**;
> they are not duplicated here during prep, because that workspace is still
> actively generating them. See [`LAUNCH_CHECKLIST.md`](LAUNCH_CHECKLIST.md).

## What's here (prep)

```
.github/
  workflows/deploy.yml          # static Pages deploy (does NOT run the scorer)
  ISSUE_TEMPLATE/               # submit-your-model · objection · config
deploy/build_public.sh          # assembles _public/ (site + data siblings + root redirect)
site/                           # populated at launch (index.html, board.json, methodology.html, …)
data/leaderboard/               # populated at launch (*.jsonl); + DATASET_CARD.md, to_parquet.py
drafts/                         # X / HN / r-LocalLLaMA launch posts (unposted)
NAMING.md                       # brand decision material
LAUNCH_CHECKLIST.md             # the one-way launch runbook + 30-day kill review
```

## How it deploys

`site/index.html` fetches `../data/leaderboard/board.json`, so the served tree
keeps `site/` and `data/` as siblings. `deploy/build_public.sh` assembles that
into `_public/`, adds a root redirect to `/site/`, and serves `llms.txt` from the
root. GitHub Actions publishes `_public/` to Pages. `board.json` is built locally
by the eval workspace's `build_results.py` and committed under `data/leaderboard/`
— **CI never runs the scorer** (it needs the scoring venv, gold sets, and raw
results).

## The receiving surface (why it exists before the traffic)

A leaderboard that gets attention needs somewhere for that attention to go, built
*before* the launch, not after (`FAILURE_GUARDS` #2). Here that's: a
**submit-your-model** issue form (which is also the demand-pull hook — to be
listed, a vendor needs a verified port), an **objection** form for model owners
(fairness duty when you publish someone's score), and the maintainer's profile as
the contact. No sales CTA on the board itself.

## Status

Prep only. Nothing is published: no GitHub remote yet, no Pages, no HF upload, no
posts. The launch is a single gated runbook in `LAUNCH_CHECKLIST.md`.
