# X / post drafts (EN) — DO NOT POST (launch-gated)

Tone: understated, feature/technique-first, a link at the end, no sales CTA.
Numbers below are checked against the **final full596 board (2026-07-13, 8 entries)**.

---

## Option A — the built-in FM angle (recommended headline)

> I put Apple's built-in Foundation Model on a standard benchmark protocol
> (MMLU-Pro / MATH / IFEval, greedy, 0-shot) — next to open models that actually
> run on an iPhone, scored the same way.
>
> It tops the composite (76%), but it's a statistical tie with the best 1–2B open
> ports (LFM2.5-1.2B, Qwen3.5-2B, Youtu-2B, Gemma 4 E2B — all CIs overlap), and a
> 1.2B open instruct model still beats it on instruction-following (IFEval 88 vs 82).
> Same battery, same cap, refusals counted separately.
>
> [link]

## Option B — the "smartest thing in your pocket" angle

> A leaderboard for the question I actually have as an iOS dev: of the models that
> *fit and stay usable* on an iPhone 17 Pro, which is the smartest?
>
> Intelligence × decode speed, memory tier, and — on the same row — how much
> quality the shipped quantization loses vs the float model. Apple's built-in FM
> is on it as a baseline "sea level".
>
> [link]

## Option C — the retention angle (technique-first)

> Small on-device models: how much does the shipped int8/int4 actually cost vs the
> float model? Measured on the same items, same protocol, for the iPhone-tier ports.
>
> Short version: it's not monotone with size — most ports hold 90–98% on MMLU-Pro,
> but the 4B reasoning model takes the biggest hit (78%). And Google's official QAT
> int4 (Gemma 4 E2B) measures at parity on MMLU/MATH — the "zero-loss" claim
> holds there, with IFEval at ~90%.
>
> [link]

## Option D — the QAT angle (Gemma-specific)

> Google ships Gemma 4 E2B with official QAT int4 weights and the claim that int4
> ≈ bf16. Measured it: on MMLU-Pro and MATH (completed-only, same items) the QAT
> int4 is at parity with its bf16 checkpoint; IFEval retains ~90%. Full protocol +
> CIs on the board.
>
> [link]

---

### Notes for whoever posts
- Lead with the finding, not the project. Link once, at the end.
- No "DM me / hire me / try my app". The receiving surface is the board's own
  submit/objection issues + the maintainer's profile.
- If a thread: post 2–3 concrete rows as a follow-up (e.g. the 4B "smartest on
  MMLU, worst on IFEval because it won't stop thinking" result reads well; the
  top-5 statistical tie incl. the built-in FM is the honest headline).
- Reply-ready line if asked "why trust Mac-measured intelligence for a phone?":
  every port passes device ≡ Mac ≡ HF greedy token-exact; only speed/mem are
  device-measured. Link the methodology page.
