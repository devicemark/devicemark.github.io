# Contributing

## Want a model on the board? Paste a link.

Open a [row request](https://github.com/devicemark/devicemark.github.io/issues/new?template=add-a-model.yml)
with the model's Hugging Face URL. That is the whole ask. You do not need to port it,
run anything, or open a PR.

What happens next: we port the model, run it through the same 596-item battery every row
gets, gate it on a real iPhone, and add the row. We reply on the issue when the row lands,
or with the reason it could not.

What gets a row: open weights, and small enough for a phone. The board currently tops out
around 4–5B parameters. Requests are batched into measurement runs, so an open issue is
normal, not forgotten.

## Something on the board is wrong

If we scored your model and the number is unfair, open an
[objection](https://github.com/devicemark/devicemark.github.io/issues/new?template=objection.yml).
Typical valid objections: we measured a quant you do not ship, the port lost parity, the
chat template is wrong, or the token cap truncated your model's reasoning. We re-run or
annotate where the objection holds. The rules are in the
[methodology](https://devicemark.github.io/methodology.html).

## PRs to this repo

Welcome for the site, the deploy script, and the docs. Please do not hand-edit anything under
`data/leaderboard/`: those files are written by the scorer, and a row only enters the board
through it. A PR that adds or edits a row by hand will be closed with a pointer to the row
request above.

## Bringing your own port (power users)

If you already ship an on-device port and want it measured as-is, say so in the row request
and add:

- **Format and runtime**: `aimodel` / Core AI, `gguf` / llama.cpp, `litertlm`, `mlx`.
- **Quantization**: each quant is its own row.
- **Parity evidence**: device ≡ Mac ≡ Hugging Face greedy, token-exact, on at least 16
  prompts, with the device and OS build. Our own gate runs 24 prompts on an iPhone 17 Pro over
  the native and oracle paths; per-row results, including rows gated on fewer, are in the
  [proofs table](https://devicemark.github.io/methodology.html#proofs).
- **Export recipe**: a link to how the bundle was built. For Core AI ports the zoo's
  [PORTING.md](https://github.com/john-rocky/coreai-model-zoo/blob/main/PORTING.md) is the
  reference.

We still run the battery ourselves. Every row goes through one scorer on one machine, which is
what keeps the rows comparable, so we do not accept self-reported scores.

## Checking our numbers

Every raw model output is published under `raw/` in the
[results dataset](https://huggingface.co/datasets/devicemark/results), one JSONL per model
per benchmark. IFEval is scored with the official checkers, MMLU-Pro by the letter inside
`\boxed{}`, and MATH by sympy symbolic equality of the `\boxed{}` answer. The
[methodology](https://devicemark.github.io/methodology.html) describes the battery, the cap,
and the confidence intervals. If a re-score disagrees with a published number, open an
objection with the item ids.
