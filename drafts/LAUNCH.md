# Launch pack — supersedes x-post.md, x-post-2026-07-28.md, hn-titles.md, r-localllama.md

All numbers read from the live `board.json` on 2026-08-03 and unchanged since 2026-07-28.
The older drafts are numerically stale (8 entries, 2026-07-12/13) — do not post from them.

**Lead angle: Apple's built-in model.** It is the only row the reader already has an opinion
about, and the comparison has never been published by anyone. The rest of the board is the
supporting evidence, not the headline.

---

## Pre-flight

| | |
|---|---|
| Board live, 12 rows | ✅ |
| methodology `cap` statement correct | ✅ fixed and deployed 2026-08-03 |
| FM row's 1024 cap disclosed and shown immaterial | ✅ 0 of 599 responses truncated |
| **HF dataset `devicemark/results` public** | ✅ 2026-08-04 — anonymous API returns 200, `private: false`, 70 files |
| Link card has an image | ✅ 2026-08-04 — `og:image` + `twitter:image` were declared-but-missing; now live |
| Notify Ping Yu / Shuangfeng | after posting, not before |

Nothing is blocking. The dataset was the last one: "raw outputs published for re-scoring" is
claimed on the methodology page and in every draft below, and it now holds for a logged-out
reader.

**Attach the chart to Post 1.** `coreai-assets/charts/devicemark-board.png` (1144×648) — the
board as a bar chart, Apple's row highlighted, each bar's download size beside it. Post 1's text
says Apple comes 6th; the picture is what makes "and a 1.2B beats it" land without a click. The
1.91:1 padded twin (`devicemark-og.png`) is what the link card in Reply 4 pulls.

---

## X — thread

**Post**

> Nobody had benchmarked Apple's built-in Foundation Model against open models that run on the
> same phone. So I did — same 596 questions, same scorers, greedy, no-answer scored wrong.
>
> It comes 6th of 12. A 1.2B open model beats it.

**Reply 1**

> Apple's model: 55.8 composite, 82.1 on instruction-following.
> LFM2.5-1.2B: 68.2, and 88.4 on instruction-following.
>
> Apple's is free, ships with the OS, and downloads nothing. The 1.2B costs 1.6 GB. That is the
> actual trade, and it was not measurable until now.

**Reply 2**

> One thing I did not expect: **Apple's model does not get better with more thinking time.**
> Every other row climbs as the token budget goes from 128 to 4096. Its accuracy is flat at
> 42.2% the whole way.
>
> Its row also ran at a 1024-token cap rather than 4096. It never came close — 0 of 599
> responses were truncated — so it changes nothing, but it is on the methodology page.

**Reply 3**

> The other surprise is that the ranking inverts with size. Qwen3.5-4B is **last**, not because
> it is worse at the questions but because it does not finish: 45 of 196 answered within budget,
> median 3,917 tokens generated of 4,096.
>
> Nanbeige4.1-3B is the most accurate model here when it answers — 95.7% on MMLU-Pro — and
> second-to-last overall. It finishes 35%.

**Reply 4 (link)**

> Quality measured on a Mac and carried to the phone by greedy token-exact parity
> (device ≡ Mac ≡ HF); speed and memory device-measured on an iPhone 17 Pro. Raw per-question
> outputs published so anything here can be re-scored.
>
> https://devicemark.github.io/

## Hacker News

**Title**

> Show HN: I benchmarked Apple's built-in Foundation Model against open on-device models

The 2026-07-12 draft flagged this title as usable "only if the FM row is solid on the final
board." It is: full 596-item battery, and the cap question is answered with the raw counts.

**First comment (submitter)**

> Author here. This started as a question I kept having as an iOS developer: of the models that
> actually run on an iPhone, which is the smartest that stays usable — and where does Apple's
> own built-in model sit among them?
>
> Nobody had measured the second half, so the board puts Apple's Foundation Model on the same
> 596-item battery (IFEval / MMLU-Pro / MATH-500) as ten open models, greedy, 0-shot, with
> no-answer scored wrong and kept in the denominator.
>
> It lands 6th of 12 at 55.8. A 1.2B open model (LFM2.5) leads the on-device rows at 68.2.
> Cloud lines (Gemini Flash/Pro, ~90) are on the board as a sea level, not as competitors.
>
> Method notes, since they are the first thing I would ask:
> - Intelligence is measured on a Mac and transferred by a greedy token-exact parity gate
>   (device ≡ Mac ≡ HF). Only speed, memory and power are device-measured. Running the full
>   battery at 20 tok/s on a phone is days per model; the parity gate is what makes the Mac
>   measurement honest.
> - One 4096-token budget for every downloaded model. The Apple row ran at 1024 because its
>   driver predates that change — 0 of its 599 responses were truncated, so it is immaterial,
>   and it is on the methodology page rather than quietly equalised.
> - Every accuracy carries a Wilson 95% interval. Several rows overlap; the board says so.
> - Raw per-question outputs are published so anyone can re-score.
>
> Two findings I did not expect. Apple's model is the only row whose accuracy does not improve
> with a larger token budget — flat at 42.2% from 128 tokens to 4096. And the ranking inverts
> with size: Qwen3.5-4B is last because it answers 45 of 196 questions within budget, while
> Nanbeige4.1-3B is the most accurate model on the board when it does answer (95.7%) and
> second-to-last overall.
>
> Happy to answer anything about the protocol. If a number looks wrong, the raw outputs are
> there and I would rather fix it than defend it.

## r/LocalLLaMA

**Title**

> On-device LLM leaderboard (iPhone tier): 10 open models + Apple's built-in Foundation Model,
> same 596-item battery, int8 retention reported

**Body**

> This subreddit will ask what quant, what protocol, what baseline, and whether it is
> contaminated, so those first.
>
> **Protocol.** IFEval (300) + MMLU-Pro (196, stratified over 14 categories) + MATH-500 (100),
> 0-shot, greedy, thinking off. No-answer is scored wrong and stays in the denominator, so a
> model cannot gain by giving up. 4096-token budget on every downloaded model. Official
> google-research IFEval checkers, vendored and seeded — upstream items 1122/1129 make the
> official scorer non-deterministic, which is disclosed on the methodology page.
>
> **Quant.** Each entry is the shipped bundle's own recipe default, mostly int8 with a
> block-32 symmetric head; int8 and int4 are separate entries, never mixed. Retention (③) is
> the shipped bundle against the same model pre-quantization on identical items, reported on
> answered problems so it reflects quantization damage rather than verbosity.
>
> **Baseline honesty.** Column ② is coreai_models' own eager PyTorch reference, not an
> independent third-party transformers run — so retention captures quantization *and*
> eager→engine numerics together. The methodology page says this rather than implying a cleaner
> comparison.
>
> **Where it is measured.** Quality on a Mac, carried to the device by a greedy token-exact
> parity gate (device ≡ Mac ≡ HF). Speed and memory on an iPhone 17 Pro.
>
> **Results worth arguing about:**
> - A 1.2B (LFM2.5) leads the on-device rows at 68.2. Qwen3.5-4B is **last** at 26.1 — it
>   answers 45 of 196 MMLU-Pro items within budget, median 3,917 tokens generated.
> - Nanbeige4.1-3B has the highest accuracy-when-answered on the board (95.7% MMLU-Pro) and is
>   second-to-last overall, finishing 35%.
> - Apple's built-in Foundation Model is 6th at 55.8 and is the only row that does not improve
>   with a larger budget — flat at 42.2% from 128 tokens up.
>
> Raw per-question outputs are published (no questions or gold, so it is re-scorable without
> redistributing the datasets). Board: https://devicemark.github.io/

---

## Facts, for answering replies

| Model | Composite | IFEval | MMLU answer rate | acc when answered | median gen | iPhone tok/s | MB |
|---|---|---|---|---|---|---|---|
| LFM2.5-1.2B | 68.2 | 88.4 | 100% | 41.3% | 561 | 45.5 | 1600 |
| Qwen3.5-2B | 62.1 | 69.2 | 88.3% | 57.8% | 846 | 29 | 2900 |
| Nemotron-3-Nano-4B | 61.4 | 43.4 | 87.8% | 65.7% | 765 | 14.7 | 4300 |
| **Apple Foundation Model** | **55.8** | **82.1** | 63.8% | 64.8% | 622 | — | 0 |
| Gemma 4 E2B (LiteRT-LM) | 52.9 | 76.3 | 97.5% | 49.7% | 868 | 57 | 488 |
| Granite-4.0-H-1B | 52.5 | 79.6 | 98.0% | 27.6% | 455 | 31 | 1700 |
| Youtu-LLM-2B | 52.3 | 62.1 | 67.4% | 62.1% | 2893 | 23.3 | 2100 |
| Qwen3.5-0.8B | 41.9 | 56.7 | 82.1% | 39.1% | 828 | 72 | 443 |
| Nanbeige4.1-3B | 31.7 | 1.3 | 35.2% | **95.7%** | 3585 | 16.9 | 4300 |
| Qwen3.5-4B | 26.1 | 31.5 | **23.0%** | 68.9% | 3917 | 10.8 | 4200 |

Cloud sea-level (not competitors): Gemini Flash 92.1, Gemini Pro 90.5.

**Do not lead with retention (③).** Four rows report ratios above 1.0 — the cap-timing confound
the methodology documents. It is honest on the page and reads as broken in a post.

**If asked why Gemma is on LiteRT-LM**: quality is runtime-dependent for that model (its
quantization is co-designed with LiteRT's activation path), and the Core AI path balloons memory
via the PLE-gather graph. The runtime is disclosed per row. On the phone LiteRT-LM runs it at
~57 tok/s and 488 MB against the Core AI path's 21.7 tok/s and 4450 MB — the port I maintain
loses that row, and it is on the board that way.
