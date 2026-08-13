# Launch pack (tanbun rewrite of LAUNCH.md, 2026-08-05)

Posts only. Pre-flight checklist and the facts-for-replies table stay in
LAUNCH.md — they are internal, the compression rules don't apply to them.
Numbers verified against live `board.json` on 2026-08-13.

Attach `coreai-assets/charts/devicemark-board.png` to Post 1.

> ⚠️ **This file and LAUNCH.md both carry the full post text.** They drifted once
> already: this one was written from a copy that predated the rank fix, and shipped
> "6th of 12" in four places plus "10 open models" in the Reddit title. Both are
> corrected as of 2026-08-13 and now agree. **Before posting, pick one file and delete
> the posts from the other** — two copies of the same paragraphs will drift again.
>
> Two counts to keep straight, both read from `board.json`: the board has **12 rows =
> 2 cloud + 10 on-device**, and the 10 on-device are **9 open models + Apple's**.
> Apple is **4th of those 10**; "6th of 12" only holds if the cloud rows count as
> competitors, which every draft here explicitly says they do not.

---

## X — thread

**Post** *(rank phrasing corrected 2026-08-13 — see LAUNCH.md)* — attach `devicemark-board.png`

> Nobody had benchmarked Apple's built-in Foundation Model against the open
> models that run on the same phone. So I did — same 596 questions, same
> scorers, greedy, no answer scored wrong.
>
> Three of them beat it. The best is 1.2B and downloads 1.6 GB. Apple's
> ships with the OS and downloads nothing.

**Reply 1** *(unchanged)*

> Apple's model: 55.8 composite, 82.1 on instruction-following.
> LFM2.5-1.2B: 68.2, and 88.4 on instruction-following.
>
> Apple's is free, ships with the OS, and downloads nothing. The 1.2B costs
> 1.6 GB. That is the actual trade, and it was not measurable until now.

**Reply 2**

> One thing I did not expect: **Apple's model does not get better with more
> thinking time.** Every other row climbs as the token budget goes from 128 to
> 4096. Its accuracy is flat at 42.2% the whole way.
>
> (Its row ran at a 1024-token cap — 0 of 599 responses truncated, so it
> changes nothing; details on the methodology page.)

**Reply 3** *(unchanged)*

> The other surprise is that the ranking inverts with size. Qwen3.5-4B is
> **last**, not because it is worse at the questions but because it does not
> finish: 45 of 196 answered within budget, median 3,917 tokens generated
> of 4,096.
>
> Nanbeige4.1-3B is the most accurate model here when it answers — 95.7% on
> MMLU-Pro — and second-to-last overall. It finishes 35%.

**Reply 4 (link)** *(unchanged)*

> Quality measured on a Mac and carried to the phone by greedy token-exact
> parity (device ≡ Mac ≡ HF); speed and memory device-measured on an
> iPhone 17 Pro. Raw per-question outputs published so anything here can be
> re-scored.
>
> https://devicemark.github.io/

## Hacker News

**Title** *(unchanged)*

> Show HN: I benchmarked Apple's built-in Foundation Model against open
> on-device models

**First comment (submitter)**

> Author here. As an iOS developer I kept wondering: of the models that
> actually run on an iPhone, which is the smartest that stays usable — and
> where does Apple's own built-in model sit among them?
>
> Answer: 4th of the ten that run on the phone, at 55.8. Three open models beat it.
> Same 596-item battery for every row
> (IFEval / MMLU-Pro / MATH-500), greedy, 0-shot, no-answer scored wrong and
> kept in the denominator. A 1.2B open model (LFM2.5) leads the on-device
> rows at 68.2. Cloud lines (~90) are on the board as sea level, not
> competitors, so they are not in that count.
>
> Method notes:
> - Intelligence is measured on a Mac and carried to the phone by a greedy
>   token-exact parity gate (device ≡ Mac ≡ HF). Only speed, memory and power
>   are device-measured — the full battery at 20 tok/s would be days per model.
> - One 4096-token budget for every downloaded model. The Apple row ran at
>   1024 (its driver predates that change) — 0 of 599 responses truncated, so
>   immaterial; on the methodology page rather than quietly equalised.
> - Every accuracy carries a Wilson 95% interval. Several rows overlap; the
>   board says so.
> - Raw per-question outputs are published so anyone can re-score.
>
> Two findings I did not expect: Apple's model is the only row whose accuracy
> does not improve with a larger token budget — flat at 42.2% from 128 to
> 4096. And the ranking inverts with size: Qwen3.5-4B is last because it
> answers 45 of 196 within budget; Nanbeige4.1-3B is the most accurate model
> on the board when it answers (95.7%) and second-to-last overall.
>
> If a number looks wrong, the raw outputs are there — I would rather fix it
> than defend it.

## r/LocalLLaMA

**Title** *(unchanged)*

> On-device LLM leaderboard (iPhone tier): 9 open models + Apple's built-in
> Foundation Model, same 596-item battery, int8 retention reported

**Body**

> Protocol and quant first, since that's what gets asked here.
>
> **Protocol.** IFEval (300) + MMLU-Pro (196, stratified over 14 categories) +
> MATH-500 (100), 0-shot, greedy, thinking off. No-answer is scored wrong and
> stays in the denominator. 4096-token budget on every downloaded model.
> Official google-research IFEval checkers, vendored and seeded (upstream
> items 1122/1129 make the official scorer non-deterministic — disclosed on
> the methodology page).
>
> **Quant.** Each entry is the shipped bundle's own recipe default, mostly
> int8 with a block-32 symmetric head; int8 and int4 are separate entries.
> Retention (③) is the shipped bundle vs the same model pre-quantization on
> identical answered items.
>
> **Baseline.** Column ② is coreai_models' own eager PyTorch reference, not an
> independent transformers run — so retention captures quantization *and*
> eager→engine numerics together. The methodology page says this outright.
>
> **Where measured.** Quality on a Mac, carried to the device by a greedy
> token-exact parity gate (device ≡ Mac ≡ HF). Speed and memory on an
> iPhone 17 Pro.
>
> **Results worth arguing about:**
> - A 1.2B (LFM2.5) leads the on-device rows at 68.2. Qwen3.5-4B is **last**
>   at 26.1 — it answers 45 of 196 MMLU-Pro items within budget, median 3,917
>   tokens generated.
> - Nanbeige4.1-3B has the highest accuracy-when-answered on the board (95.7%
>   MMLU-Pro) and is second-to-last overall, finishing 35%.
> - Apple's built-in Foundation Model is 4th of the ten on-device rows at
>   55.8, and is the only row that does not improve with a larger budget — flat at 42.2% from 128 tokens up.
>
> Raw per-question outputs are published (no questions or gold, so it is
> re-scorable without redistributing the datasets).
> Board: https://devicemark.github.io/
