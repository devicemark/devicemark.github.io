#!/usr/bin/env bash
# Assemble the public Pages artifact into ./_public.
#
# The published site preserves the site/ + data/ sibling layout that
# site/index.html expects: it does `fetch('../data/leaderboard/board.json')`,
# so `data/` must be a sibling of `site/` in the served tree.
#
# board.json / artifacts.jsonl / measurements.jsonl are produced LOCALLY by the
# eval workspace's build_results.py and synced into data/leaderboard/ before a
# launch (see LAUNCH_CHECKLIST.md). CI does NOT run build_results.py — it only
# packages what is already committed here.
#
# Usage: deploy/build_public.sh   (run from repo root)
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="_public"
rm -rf "$OUT"
mkdir -p "$OUT/site" "$OUT/data/leaderboard"

# 1. the site itself (index.html, methodology.html, favicon.svg, og-tags note, etc.)
cp -R site/. "$OUT/site/"

# 2. the data the site fetches (kept as a sibling of site/)
if compgen -G "data/leaderboard/*.json*" > /dev/null; then
  cp data/leaderboard/*.json  "$OUT/data/leaderboard/" 2>/dev/null || true
  cp data/leaderboard/*.jsonl "$OUT/data/leaderboard/" 2>/dev/null || true
fi

# 3. root landing -> redirect to /site/ so the bare domain resolves
cat > "$OUT/index.html" <<'HTML'
<!doctype html><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=site/">
<link rel="canonical" href="site/">
<title>On-Device LLM Leaderboard</title>
<a href="site/">On-Device LLM Leaderboard &rarr;</a>
HTML

# 4. llms.txt is served from the site root by convention (/llms.txt)
[ -f site/llms.txt ] && cp site/llms.txt "$OUT/llms.txt" || true

# 5. courtesy: keep the old ../METHODOLOGY.md link from hard-404ing until the
#    index.html link is repointed to methodology.html (renders as plaintext).
[ -f METHODOLOGY.md ] && cp METHODOLOGY.md "$OUT/METHODOLOGY.md" || true

echo "assembled $OUT:"
find "$OUT" -type f | sort
