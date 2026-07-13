# Methodology — On-Device LLM Leaderboard (v0, iPhone tier)

*Draft, P2 (2026-07-11). Proof strength is disclosed honestly per the KICKOFF —
where a column rests on a proxy, it says so.*

## What the leaderboard measures

"Of the models that actually run on this phone, which is the smartest that stays
usable?" — the intelligence × decode-speed Pareto front under real device limits.
Intelligence is measured on **Mac** (fast) and transferred to the device by the
zoo **parity gate** (device ≡ Mac ≡ HF greedy token-exact); only tok/s, memory,
and power are measured on the device itself.

## The three columns per entry

| # | column | what it is | how measured |
|---|--------|-----------|--------------|
| ① | shipped int8 | the on-device quantized bundle | Core AI engine, Mac GPU, S=1 pipelined |
| ② | baseline | the same model **before quantization** | eager PyTorch reference, float |
| ③ | retention | ② → ① | accuracy(①) / accuracy(②) on identical items |

Quantization variants (int8 vs int4) are **separate entries**, never mixed.

### ② baseline — implementation decision (the P2 risk-1 call)

Target model family for v0 is **Qwen3.5** (0.8B / 2B). Its checkpoint is a
**vision-language model with a hybrid linear-attention (gated-delta / SSM) + sparse
full-attention text backbone** (`model_type: qwen3_5`, `layer_types` mostly
`linear_attention` with `full_attention` every 4th layer, MTP head, mrope).

Three candidate baselines were considered:

- **(a) third-party HF transformers (bf16)** — the most authoritative baseline, but
  **not available**: `transformers 4.57.6` (both venvs on this box) has no `qwen3_5`
  model_type (only `qwen3`, `qwen3_moe`, `qwen3_next`, `qwen3_vl*`). It existed only in
  the unreleased `4.57.0.dev0` the checkpoint was saved with, and the HF repo ships no
  custom modeling code. Chasing a transformers fork for a VL+SSM hybrid is fragile and
  out of scope for v0.
- **(b) coreai_models eager reference (float)** — **CHOSEN**. `Qwen3_5StatefulForCausalLM`
  is coreai_models' own PyTorch implementation of this exact architecture — the same
  definition that is quantized+exported for ①. Run **unquantized (fp16)**, greedy, it is
  a genuine pre-quantization reference. Weight-loading is already solved
  (`from_hf_memory_efficient`). Harness = `ref_eval.py`.
- **(c) fp16-on-engine proxy** — the fp16 Core AI bundle. Fast (175 tok/s) but still
  engine-compiled, so it isolates only int8-vs-fp16 *weights on the same engine*, not
  "vs the float original". Kept as a **secondary** cross-check (see below).

**Proof-strength disclosure:** column ② is the coreai_models **eager PyTorch**
reference, **not** an independent third-party transformers run. Therefore retention ③
captures *(int8 weight quantization) + (eager→Core AI engine numerics)* **together**.
This is arguably the more product-relevant number ("what the shipped on-device model
loses vs the float model"), but it is not an independent re-implementation, and the
methodology says so. When a `qwen3_5`-capable transformers becomes available, (a) can be
added as a stronger anchor.

**Two-tier cost design.** The eager reference decodes at **~11 tok/s** on the Mac GPU
(MPS, fp16) — 18× slower than the 223 tok/s engine — so it is **not** run on the full
battery. Column ① (engine) runs the **full** battery; column ② (eager) runs a
**stratified subset** (`ref_subset` in the battery manifest), and retention ③ is
computed on those shared keys. Subset size is disclosed per entry.

## Evaluation battery v0

Greedy (deterministic), **cap = 1024 tokens**, **0-shot**, chat template with
**thinking OFF** (verified: on-device `ChatSession` runs thinking-off — P1
`thinking_chars == 0`). Prompts instruct step-by-step reasoning in the visible answer.

| bench | source | metric | scorer |
|-------|--------|--------|--------|
| **IFEval** | google/IFEval (541) | prompt/inst strict+loose, mean-of-4 | **official** google-research checkers (vendored `scoring/ifeval/`) |
| **MMLU-Pro** | TIGER-Lab/MMLU-Pro | accuracy, **stratified across 14 categories** | `\boxed{letter}` extraction |
| **MATH-500** | HuggingFaceH4/MATH-500 | accuracy, stratified across 7 subjects | `\boxed{}` + **sympy** symbolic equality |

**GPQA-Diamond is excluded** from the iPhone tier: at ≤1B it sits at/below chance
(P1: 13.3% vs 25% chance, 60% never converge within cap) = floor effect, and it is
gated (ToS). It moves to the Mac / v1 tier.

### The cap lever + the retention confound (documented, not hidden)

`max-tokens` is an explicit design lever. Verbose small models spend the whole budget
reasoning: qwen3.5-0.8B int8 at cap-1024 on MMLU-Pro **caps 27/50** and produces **no
boxed answer in 26/50** — those score as wrong (a fair "couldn't deliver a usable answer
on-device in-budget" signal). Larger/less-verbose models cap far less.

**Finding (P2, surfaced by the ② eager run):** ① and ② cap at *different* points (greedy
paths diverge — int8 vs float weights, engine vs eager), so their no-answer rates differ
and the **retention ratio ③ can be dominated by cap-timing, not quantization quality** —
it can even exceed 100% at small n (early read: math n=9, float-ref 55.6% vs int8 66.7%,
driven by 4 vs 2 no-answers, not by either being "smarter"; on shared *answered* problems
the two emit identical boxed answers). Mitigations, both reported:

1. **Two accuracies per bench**: `acc` (no-answer = wrong; the on-device "usable" number)
   and `acc_completed` (only problems that produced an answer; cap-independent quality).
   **Retention ③ is reported on `acc_completed`** so it reflects quantization damage, not
   verbosity; `acc` + no-answer rate carry the usability story.
2. **Larger n + a per-tier cap**: raise the cap when no-answer is the dominant term.

This is exactly the design bug the risk-ordered P2 was meant to catch before the fleet run.

## Speed / memory / power

PipelinedBench (`STATS prefill/decode`) on iPhone 17 Pro / M4 Max. tok/s + peak
footprint for v0; power later. (This box ≈ M4 Max: 0.8B int8 = 207 tok/s decode,
matching the published 204.)

## Runtime-neutral schema (day-1 multi-runtime)

Quality is an attribute of the **artifact** (model × quant × `format`), measured on its
native `runtime` + bf16 retention. Speed/memory/power are attributes of **runtime ×
device**. Two normalized, HF-dataset-ready tables (`data/leaderboard/`):
`artifacts.jsonl` (quality + retention, tagged `format`/`native_runtime`) and
`measurements.jsonl` (`runtime`/`device`/tok-s/mem). v0 data is Core AI only
(`format=aimodel`, `runtime=coreai`), but GGUF/`llama.cpp` and MLX/`mlx-lm` rows drop
in as pure data additions — the cross-runtime judge, defensive against single-ecosystem
clones. `build_results.py` assembles both from the raw eval JSONL.

## Apple's built-in Foundation Model as a board row

Apple's on-device system model (`SystemLanguageModel` via `LanguageModelSession()`) runs
the same battery through `fm-driver/` (`runtime=foundation-models`, `format=system`,
DL size 0, OS-resident, `retention=null` — it is not a quantized port). It is the natural
anchor for the small-model group. v0 result: strong on knowledge/math (MMLU-Pro 73%,
MATH 93% completed) but **weak on IFEval (67%)** vs the small instruct ports (LFM2.5/
Granite ~84%); refusal <1%, rateLimited 0.

## Refusal rate (a column for all, decisive for the built-in)

`guardrailViolation` and explicit textual refusals are **separated from wrong answers**
(`quality.refusal_rate`; accuracy is computed over non-refused items). `rateLimited`
errors are handled with exponential-backoff pacing and their rate recorded. Near-zero on
the general battery for every model including the built-in FM, but the column matters the
moment a bench probes guarded topics.

## Finding: reasoning-heavy ≠ instruction-following, ≠ on-device-practical

Reasoning-heavy models (Qwen3.5-4B, the built-in FM) top MMLU-Pro but **crater IFEval**:
Qwen3.5-4B is the smartest on MMLU (77.7% completed) yet scores 27% on IFEval because it
prepends a "Thinking Process:" meta-analysis that uses commas and isn't the requested
output — violating the format constraints outright. It also generates ~4000 tokens even
at cap-4096 (barely terminating), so it is slower and less battery-practical on device.
The intelligence composite (which includes IFEval) surfaces this trade-off deliberately:
raw knowledge is not the same as being useful in your pocket.

## Environment note (why bundles are re-exported locally)

This box is on **macOS 27 beta3**, which requires **b2-versioned IR**; all pre-2026-07-09
(b1-era) HF bundles are un-loadable (`Failed to convert to versioned IR`). Every entry's
① bundle is re-exported locally with the b2 toolchain via the zoo's own recipe
(`zoo_convert.py` / `export_qwen3_5_decode_pipelined.py`) — bit-identical weights, just
re-emitted IR. See `reference_coreai_env`.
