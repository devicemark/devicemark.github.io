# LAUNCH CHECKLIST — on-device LLM leaderboard v0

A one-way runbook. Everything above the **PUBLISH LINE** is reversible prep;
everything below is a public act. Do the whole thing in one sitting so
distribution isn't half-wired. Nothing here has been done yet — this session
built the vessel only.

Guarding references: `strategy/FAILURE_GUARDS.md` (#1 Cydoc / #2 receiving surface
/ #3 TOS-fairness / #4 single-distribution), `LEADERBOARD_KICKOFF.md` (kill condition).

---

## 0. Decide the name (blocks everything downstream)

- [ ] Pick the brand from `NAMING.md` (or keep the working name).
- [ ] Keep the descriptive `<h1>`/`<title>` ("On-Device LLM Leaderboard") — that's
      the discoverability string, not the brand.
- [ ] In one sitting, claim: GitHub org/repo name, the domain, the HF dataset
      namespace. (`FAILURE_GUARDS` #4 — don't tie distribution to one platform.)

## 1. Freeze the data + sync the site (from the eval workspace)

The eval workspace `~/code/coreai/leaderboard/` is the source of truth. Wait until
the P3 full-battery run is done and `build_results.py` has been run once more.

- [ ] In the eval workspace: `coreai-models/.venv/bin/python build_results.py`
      (regenerates `data/leaderboard/{artifacts,measurements}.jsonl`, `board.json`
      and `site/board.json`). Confirm every intended row is present and `source`
      is `full596` where expected.
- [ ] Sync site → this repo:
      `rsync -a --delete ~/code/coreai/leaderboard/site/ ./site/`
      (brings index.html, board.json, methodology.html, favicon.svg, og-tags.html,
      llms.txt). Keep this repo's `site/README.md` out of the deploy or leave it;
      it's harmless.
- [ ] Sync data → this repo:
      `cp ~/code/coreai/leaderboard/data/leaderboard/*.jsonl ./data/leaderboard/`
      `cp ~/code/coreai/leaderboard/data/leaderboard/board.json ./data/leaderboard/`
- [ ] Apply the three `index.html` edits still owed (this prep session did not
      touch index.html — see `site/README.md` and `PREP_STATE.md` in the workspace):
      1. link `../METHODOLOGY.md` → `methodology.html`
      2. add `<link rel="icon" href="favicon.svg" type="image/svg+xml">` to `<head>`
      3. paste the `og-tags.html` `<meta>` block into `<head>` (fill real URLs)
- [ ] Fill the real URL into every `example.invalid` placeholder:
      `og-tags.html`, `llms.txt`, `.github/ISSUE_TEMPLATE/*.yml`, `DATASET_CARD.md`.
- [ ] `bash deploy/build_public.sh` and open `_public/index.html` locally — chart
      renders, table renders, methodology link resolves, favicon shows, no console 404.

## 2. Pre-launch safety review (FAILURE_GUARDS #3 — do NOT skip)

- [ ] **Eval-data licenses**: methodology page names each benchmark's license; the
      dataset ships **results only**, no questions/gold. GPQA stays excluded from
      the phone tier (gated ToS) — confirm it isn't in any shipped file.
- [ ] **Fairness on third-party scores**: every entry links its parity proof; the
      **objection** template is live and linked from the methodology page.
- [ ] **Open-weights only**: the only `system` row is Apple's built-in FM via its
      **public API** — no extracted weights (Apple FM / Gemini Nano). Confirm.
- [ ] **Numbers match the drafts**: re-read `drafts/*` against the final
      `board.json`; fix any stale figure (the drafts warn about this).

---

## ===================== PUBLISH LINE =====================
Belowここから is public / hard to reverse. Get an explicit go before crossing.

## 3. GitHub repo (private first)

- [ ] `gh repo create <name> --private --source=. --remote=origin --push`
      (or create empty private on github.com, then `git remote add origin … && git push -u origin main`).
- [ ] Settings → Pages → Source = **GitHub Actions**. Add the custom domain +
      DNS (`FAILURE_GUARDS` #4); wait for the cert.
- [ ] Push triggers `deploy.yml`; confirm the Pages URL renders end-to-end.
- [ ] **Flip the repo to public** (this is the real "go live").

## 4. Hugging Face results dataset

- [ ] `python data/leaderboard/to_parquet.py` (writes `artifacts.parquet`,
      `measurements.parquet`).
- [ ] Create the HF dataset under the chosen namespace; upload the two parquet
      files + `DATASET_CARD.md` (as `README.md`). License **CC-BY-4.0**.
- [ ] Link the dataset from the site footer and the methodology page.

## 5. Announce (space them out — don't fire all at once)

- [ ] X: pick one option from `drafts/x-post.md`. Lead with the finding, one link.
- [ ] Hacker News: one title from `drafts/hn-titles.md`; post the first-comment
      context immediately.
- [ ] r/LocalLLaMA: `drafts/r-localllama.md`. **Not** the same hour as HN.
- [ ] One-line heads-up to the platform folks already in contact (Apple/Google/
      MLX threads) — a leaderboard their model is *on*. This is the demand-pull
      surface, not a cold pitch. (`FAILURE_GUARDS` #7 — treat as商談 framing.)

## 6. Arm the kill condition (the discipline that makes this honest)

- [ ] **Put a calendar event at launch + 30 days** (先送り不能に固定, `FAILURE_GUARDS` #1a).
- [ ] Kill review (KICKOFF): if in 30 days there is **zero** citation/pushback from
      a platform insider **and** zero vendor "list ours too" → **fold it**. Building
      more instead of facing that verdict is the Cydoc failure mode by name.
- [ ] Success signal is not "I'm happy with it" — it's "one of the ~10 orgs
      reacted." Watch `coreai-stats` (referrers / issue alerts) + the submit/
      objection issues.

## 7. Post-launch receiving (already built — just triage)

- [ ] Triage **submission** issues (a vendor submitting = demand-pull flipping on).
- [ ] Triage **objection** issues fast and fairly; re-run or annotate where they hold.
