# X / post drafts (EN) — DO NOT POST (launch-gated)

Tone: understated, feature/technique-first, a link at the end, no sales CTA.
⚠️ Numbers below are the P2 v0 board — **re-check against the final `board.json`
after the full-battery run before posting** (composite/IFEval may shift).

---

## Option A — the built-in FM angle (recommended headline)

> I put Apple's built-in Foundation Model on a standard benchmark protocol
> (MMLU-Pro / MATH / IFEval, greedy, 0-shot) — next to open models that actually
> run on an iPhone, scored the same way.
>
> It tops the knowledge/math composite, but lands mid-pack on instruction-following
> — a small open 1–2B instruct model beats it there. Same battery, same cap,
> refusals counted separately.
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

> Small on-device models: how much does the shipped int8 actually cost you vs the
> float model? Measured it on the same items, same protocol, for a handful of
> iPhone-tier ports.
>
> Short version: at ~0.8B the int8 hit is real (~7% on MMLU-Pro); by 2–4B it's in
> the noise. Quality × speed × memory × retention, one table.
>
> [link]

---

### Notes for whoever posts
- Lead with the finding, not the project. Link once, at the end.
- No "DM me / hire me / try my app". The receiving surface is the board's own
  submit/objection issues + the maintainer's profile.
- If a thread: post 2–3 concrete rows as a follow-up (e.g. the 4B "smartest on
  MMLU, worst on IFEval because it won't stop thinking" result reads well).
- Reply-ready line if asked "why trust Mac-measured intelligence for a phone?":
  every port passes device ≡ Mac ≡ HF greedy token-exact; only speed/mem are
  device-measured. Link the methodology page.
