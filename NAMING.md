# Naming — decision material (user decides; this file does not decide)

The repo/dir is `ondevice-leaderboard` as a **working name only**. Rename before
launch. Below is what to weigh; the pick is the user's.

## Constraint from the strategy

- **"Arena" is out.** This is *measurement*, not voting — calling it an arena
  invites the LMSYS comparison it doesn't earn and misleads on method. (KICKOFF.)
- **The descriptive self-description is the SEO/AIO asset, not the brand.** Per
  the discoverability finding (`project_aio_llm_discoverability`): an LLM or a
  search recommends by matching a plain description of what the thing *is*. So the
  `<h1>` / `<title>` / one-line bio should stay literally descriptive —
  **"On-Device LLM Leaderboard"** — regardless of the brand name. The brand is the
  repo, the domain, the social handle; the descriptive string is what gets you
  recommended. Keep both; don't let a cute brand replace the descriptive H1.

## Brand-name candidates (availability confirmed 2026-07-11)

| candidate | read | for | against |
|-----------|------|-----|---------|
| **PocketBench** | "benchmarks for what's in your pocket" | concrete, memorable, matches the iPhone-tier flagship framing; "bench" signals measurement (good) | slightly toy-sounding; "pocket" narrows to phones just as the roadmap expands to Mac/audio/VLM tiers |
| **DeviceMark** | "the mark/score for on-device" | broader than "pocket" — survives the Mac/audio/camera tier expansion; "mark" reads as a standard (Geekbench-adjacent) | a touch generic; less vivid than PocketBench |

Both had domain + GitHub org free as of 2026-07-11 (re-verify at launch — names
rot). Neither implies voting/arena. Both pair fine with a descriptive tagline.

## Recommended policy (not a decision)

1. **H1 / title / bio stays descriptive**: "On-Device LLM Leaderboard —
   intelligence × speed under real device limits." This is the discoverability
   surface; do not swap it for the brand.
2. **Brand = repo + domain + handle**, used as the short label and in the logo/OG.
   If the roadmap (Mac tier, audio, VLM, camera) is taken seriously, **DeviceMark**
   ages better than **PocketBench**; if the iPhone-tier flagship stays the whole
   story, **PocketBench** is punchier.
3. Whatever is chosen: grab the GitHub org, the domain, and the matching HF
   dataset namespace **in the same sitting** (single-flow, before announcing) so
   distribution isn't tied to one platform (`FAILURE_GUARDS` #4).

## What renaming touches (so it's a 10-minute job, not a scavenger hunt)

- repo/dir name and GitHub remote
- `site/index.html` `<title>` / `<h1>` (owned by the eval workspace — descriptive string, likely unchanged)
- `og-tags.html` (`og:site_name`, `og:title`, URLs)
- `llms.txt` (title line + URLs)
- `DATASET_CARD.md` (`pretty_name`, citation, URLs)
- issue-template `config.yml` + objection template URL (the `example.invalid` placeholders)
- `LAUNCH_CHECKLIST.md` (URLs)
