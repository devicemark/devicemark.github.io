# Hacker News — title candidates (DO NOT POST; launch-gated)

HN rewards plain, specific, non-hyperbolic "Show HN" titles. Three candidates,
each avoids superlatives and says exactly what it is. Pick one; the URL is the
leaderboard, the first comment carries the context (see below).

1. **Show HN: A leaderboard for LLMs that actually run on an iPhone**

2. **Show HN: On-device LLM leaderboard — intelligence, speed, and quantization loss**

3. **Show HN: I benchmarked Apple's built-in Foundation Model against open on-device models**

Notes:
- (1) is the safest / broadest. (3) is the most likely to get clicks but leans on
  the FM angle — only use it if the FM row is solid on the final board.
- Avoid "fastest", "best", "definitive" — HN punishes them.

## First-comment draft (context, posted by submitter)

> Author here. This started as a question I kept having as an iOS dev: of the
> models that fit and stay usable on the phone, which is actually the smartest?
>
> Intelligence is measured on a Mac (fast) and transferred to the device by a
> parity gate — every port is greedy token-exact device ≡ Mac ≡ HF — so only
> speed/memory are measured on-device. Each row also shows how much the shipped
> int8 loses vs the float model on the same items.
>
> Honest limitations, all on the methodology page: the float baseline is an eager
> PyTorch reference (not an independent transformers run) for the v0 family; the
> generation cap is an explicit lever and I report both cap-dependent and
> cap-independent accuracy; benchmark contamination is a known risk and the set is
> versioned. Corrections from model authors are wanted — there's an objection
> template.
>
> v0 is the iPhone tier (Core AI ports + Apple's built-in FM as a baseline). GGUF
> and MLX rows are a schema drop-in for later.
