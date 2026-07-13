---
# Hugging Face dataset card front-matter (draft — do not upload until the launch gate)
license: cc-by-4.0
language:
  - en
pretty_name: On-Device LLM Leaderboard — Results
tags:
  - leaderboard
  - on-device
  - core-ml
  - core-ai
  - quantization
  - benchmark-results
size_categories:
  - n<1K
configs:
  - config_name: artifacts
    data_files: artifacts.parquet
  - config_name: measurements
    data_files: measurements.parquet
---

# On-Device LLM Leaderboard — Results

Systematic quality + speed + memory data for **verified on-device LLM ports**,
under a single protocol, with **retention vs the float baseline** on the same
row. This is the results table behind the [On-Device LLM Leaderboard](https://john-rocky.github.io/devicemark)
(swap for the real URL at launch). v0 covers the iPhone tier (Core AI / `aimodel`
ports + Apple's built-in Foundation Model as a `system` row).

> **What is and isn't here.** This dataset contains **our generated results**
> (accuracy, decode tok/s, memory, retention). It does **not** redistribute any
> benchmark's questions or gold answers — those stay under their own licenses
> (IFEval: Apache-2.0; MMLU-Pro: MIT; MATH-500: MIT). The results here are
> released under **CC-BY-4.0**.

## Why it exists

The novel contribution is not "quality of a quantized model" (retention has a long
history in the GGUF world). It is the **join**: intelligence × on-device decode
speed × memory × *verified* parity × float-retention, for many artifacts, in one
table, under one protocol — the first systematic quality dataset for Core AI
artifacts, with quantized and float rows measured apples-to-apples.

## Files / configs

| config | file | grain | one row = |
|--------|------|-------|-----------|
| `artifacts` | `artifacts.parquet` (from `artifacts.jsonl`) | model × quant × format | a scored artifact + its retention |
| `measurements` | `measurements.parquet` (from `measurements.jsonl`) | runtime × device | one speed/memory measurement |

`board.json` is the pre-joined view the website consumes; the two parquet tables
are the normalized source. Regenerate parquet with `to_parquet.py`.

### `artifacts` schema

| field | type | notes |
|-------|------|-------|
| `artifact_id` | string | `<slug>__<quant>__<format>`, the join key |
| `model`, `vendor`, `params_b` | string / float | `params_b` null for the system model |
| `quant`, `format`, `native_runtime` | string | e.g. `int8hu` / `aimodel` / `coreai`; or `system` / `system` / `foundation-models` |
| `quality.*` | struct | per-bench accuracy + CIs, see below |
| `quality.cap_tokens`, `quality.shots` | int | generation cap (explicit lever) and shot count |
| `quality.source` | struct | per-bench `full596` or `subset` provenance |
| `quality.<bench>_completed` | float | accuracy on items that produced an answer (**cap-independent**) |
| `quality.<bench>_acc` | float | accuracy counting no-answer as wrong (the on-device "usable" number) |
| `quality.<bench>_ci` | [float,float] | Wilson 95% CI on `_completed` |
| `quality.<bench>_n/_answered/_noans` | int | counts (`noans` = ran out of budget before a boxed answer) |
| `quality.ifeval_mean4` / `ifeval_ci` | float / [float,float] | official IFEval prompt/inst strict+loose, mean-of-4 |
| `quality.refusal_rate`, `refused_n` | float / int | guardrail/explicit refusals, **separated from wrong answers** |
| `composite.value`, `composite.ci` | float / [float,float] | item-bootstrap mean of the three benches, 95% CI |
| `retention` | struct or null | `{baseline, metric:"completed-only", mmlu, math, ifeval}`; null for the system model |

### `measurements` schema

| field | type | notes |
|-------|------|-------|
| `artifact_id` | string | join back to `artifacts` |
| `runtime`, `device` | string | e.g. `coreai` / `iPhone 17 Pro` or `M4 Max` |
| `decode_tok_s` | float | S=1 pipelined decode |
| `peak_mem_mb` | float | footprint |
| `mem_measured` | bool | false = estimated, not yet device-measured |
| `power_w` | float or null | reserved (tokens/joule axis, v0.5) |

## Runtime-neutral by design

Quality is an attribute of the **artifact** (model × quant × `format`) measured on
its native `runtime`; speed/memory/power are attributes of **runtime × device**.
GGUF/`llama.cpp` and MLX/`mlx-lm` rows drop in as pure data additions — the schema
already carries `format`/`runtime`, so v0.5 cross-runtime rows need no migration.

## Proof strength (honest disclosure)

Intelligence is measured on Mac (fast) and transferred to the device by the zoo
**parity gate** (device ≡ Mac ≡ HF greedy token-exact); only tok/s, memory, power
are device-measured. The float baseline for retention is currently the
`coreai_models` **eager PyTorch** reference (not an independent third-party
transformers run), so retention folds *(int8 weight quant) + (eager→engine
numerics)* together — arguably the more product-relevant number, but disclosed as
such. Full detail: the leaderboard's methodology page.

## Versioning

`quality.battery_version` tags the eval set (v0 = IFEval + MMLU-Pro stratified +
MATH-500, cap 1024 / 4096 for reasoning models, 0-shot, greedy, thinking-off).
The battery is rotated to fight contamination; each rotation bumps the version.

## Citation

```bibtex
@misc{ondevice_llm_leaderboard,
  title  = {On-Device LLM Leaderboard: quality, speed, memory, and retention for verified on-device ports},
  author = {rockyshikoku},
  year   = {2026},
  howpublished = {\url{https://john-rocky.github.io/devicemark}},
  note   = {Results under CC-BY-4.0; benchmark questions under their own licenses}
}
```

*(Fill the real URL and final project name at launch — see `../../LAUNCH_CHECKLIST.md`.)*
