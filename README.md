# DeviceMark — On-Device LLM Leaderboard

**Live board: <https://devicemark.github.io/>**

Which LLMs actually run on an iPhone, and which is the smartest that stays usable? Every row
runs the same 596-item battery (IFEval + MMLU-Pro + MATH) under one fixed on-device budget,
with decode speed measured on the phone itself and 95% confidence intervals on every number.
Apple's built-in Foundation Model sits on the board as the baseline.
Maintained by [Daisuke Majima (MLBoy)](https://github.com/john-rocky).

## Want a model on the board?

[**Open a row request with its Hugging Face link.**](https://github.com/devicemark/devicemark.github.io/issues/new?template=add-a-model.yml)
One link is enough. We port it, measure it, and add the row, and we reply on the issue when
it lands. Details, and the path for people who already ship a port, are in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

Is your model on the board and the number wrong? Open an
[objection](https://github.com/devicemark/devicemark.github.io/issues/new?template=objection.yml).

## Use the data

- **Results dataset**: <https://huggingface.co/datasets/devicemark/results> (CC-BY-4.0):
  normalized `artifacts` and `measurements` tables, plus every raw model output under `raw/`.
- **The board as JSON**: <https://devicemark.github.io/data/leaderboard/board.json>.
- **Per-model badge**: `https://devicemark.github.io/badge/<slug>.svg`, where the slug is the
  `artifact_id` in `board.json` up to its first `__` (for example `lfm2.5-1.2b`).
- **Follow changes**: [changelog](https://devicemark.github.io/changelog.html) and
  [RSS](https://devicemark.github.io/feed.xml). Every entry is a board change.
- **For assistants**: <https://devicemark.github.io/llms.txt>.
- **Cite**: the BibTeX block is at the bottom of the board.

## What's in this repo

```
site/                 the static site (index.html, methodology.html, changelog.html, feed.xml, llms.txt)
data/leaderboard/     the committed results (board.json, artifacts.jsonl, measurements.jsonl) + dataset card
deploy/build_public.sh  assembles _public/ for GitHub Pages; gen_badges.py renders the badges
.github/              Pages deploy workflow + issue templates (row request, objection)
```

Rows are produced by the scorer in a separate eval workspace and committed here as data.
CI only packages `site/` and `data/` and publishes them to Pages; it never runs the scorer.
Method, proof strength per row, and known limitations:
[methodology](https://devicemark.github.io/methodology.html).
