# site/ — the published page (synced at launch)

At prep time this directory is intentionally near-empty. The site is authored in
the eval workspace and **synced here at launch** (single source of truth, no
drift while the P3 session is still editing it):

    ~/code/coreai/leaderboard/site/   →   this site/

What lands here at launch:

- `index.html` — the Pareto chart + table (owned by the eval workspace; P3 edits it)
- `board.json` — the joined data the page fetches (from `build_results.py`)
- `methodology.html` — page-ified methodology (authored this session, in the eval workspace)
- `favicon.svg`, `og-tags.html`, `llms.txt` — site small items (authored this session)

Before the sync, three one-time edits to `index.html` are still owed (they were
left to the workspace owner because this session does not touch `index.html`):

1. repoint the methodology link `../METHODOLOGY.md` → `methodology.html`
2. add `<link rel="icon" href="favicon.svg" type="image/svg+xml">` to `<head>`
3. paste the `og-tags.html` `<meta>` block into `<head>`

The deploy script `../deploy/build_public.sh` preserves the `site/` + `data/`
sibling layout the page's `fetch('../data/leaderboard/board.json')` needs, adds a
root redirect to `/site/`, and serves `llms.txt` from the root.
