# r/LocalLLaMA — post draft (DO NOT POST; launch-gated)

r/LocalLLaMA is technical and quantization-literate. They will immediately ask:
what quant, what protocol, what's the baseline, is it contaminated. Answer all of
that up front. Understated; no promo.

Numbers checked against the final full596 board (2026-07-13, 8 entries).

---

**Title:** On-device LLM leaderboard (iPhone tier): intelligence × speed × int8 retention, same protocol for every model

**Body:**

I built a small leaderboard for on-device LLMs and wanted to share it here first
since this is the crowd that will poke the hardest holes in it.

The question it answers: *of the models that actually run on an iPhone 17 Pro and
stay usable, which is the smartest?* So it's a Pareto of intelligence vs decode
speed, split by memory tier, and — the part I care about most — each row shows how
much the **shipped int8 loses vs the float model on the same items**.

Protocol (all on the methodology page, but the short version):
- Battery: IFEval (official scorer) + MMLU-Pro (stratified subset) + MATH-500,
  greedy, 0-shot, thinking-off. GPQA-Diamond is excluded from the phone tier — at
  ≤1B it sits at/below chance (floor effect), it moves to the Mac tier.
- Intelligence is measured on Mac and transferred to the device by a parity gate
  (device ≡ Mac ≡ HF greedy token-exact). Only tok/s + memory are device-measured.
  This is what lets me measure smarts at 200 tok/s instead of dying at 20 tok/s on
  the phone, without lying about what the phone does.
- The generation cap is an explicit lever. I report `acc` (no-answer = wrong; the
  "did it deliver on-device in-budget" number) **and** `acc_completed` (only
  answered items; cap-independent). Retention is computed on `acc_completed`.
- Refusals (guardrail/explicit) are a separate column, not counted as wrong.
- 95% CIs on everything (Wilson per bench, item-bootstrap for the composite);
  ties where CIs overlap.

A few findings that might interest you:
- **Quantization loss is NOT monotone with size.** Most ports hold 90–98% on
  MMLU-Pro completed, but the 4B reasoning model takes the biggest hit (78%) —
  and Google's official QAT int4 (Gemma 4 E2B) measures at parity on MMLU/MATH
  (the "zero-loss" claim holds there; IFEval ~90%).
- **Reasoning-heavy ≠ instruction-following.** The 4B is the smartest on MMLU-Pro
  but the *worst* on IFEval, because it prepends a long "thinking" block that
  violates the format constraints outright — and it barely terminates within cap.
- **Apple's built-in Foundation Model** is on the board as a `system` row (via the
  public API, not weight extraction). It tops the composite (76%) but is in a
  statistical tie with the best 1–2B open ports, and a 1.2B open instruct model
  beats it on IFEval (88 vs 82); refusals <1%.

Honest limits: the float baseline for the v0 family is an eager PyTorch reference,
not an independent transformers run (the checkpoint's `model_type` isn't in a
released transformers yet) — so retention folds int8 + eager→engine numerics
together; disclosed on the methodology page. Contamination is a real risk; the set
is versioned and will rotate. v0 is Core AI ports; the schema is runtime-neutral so
GGUF/MLX rows can drop in as data.

Corrections welcome — there's a submit-your-model and an objection template if I
measured the wrong quant or a port lost parity.

[link]

---

### Posting notes
- Do NOT cross-post the same hour as HN; space them.
- Expect and welcome "why not llama.cpp / MLX numbers?" — answer: runtime-neutral
  schema, they're a data drop-in, PRs/issues welcome. That's the Index play, stated plainly.
- Do not argue rank; if someone finds a real error, thank them and file it.
