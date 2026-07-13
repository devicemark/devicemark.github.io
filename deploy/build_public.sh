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
mkdir -p "$OUT/data/leaderboard" "$OUT/site"

# 1. the site lives at the ROOT (index.html fetches data/leaderboard/board.json)
cp -R site/. "$OUT/"

# 2. the data the site fetches
if compgen -G "data/leaderboard/*.json*" > /dev/null; then
  cp data/leaderboard/*.json  "$OUT/data/leaderboard/" 2>/dev/null || true
  cp data/leaderboard/*.jsonl "$OUT/data/leaderboard/" 2>/dev/null || true
fi

# 3. legacy /site/ links (early shares, HF card revisions) redirect to the root
cat > "$OUT/site/index.html" <<'HTML'
<!doctype html><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=../">
<link rel="canonical" href="https://devicemark.github.io/">
<title>On-Device LLM Leaderboard</title>
<a href="../">On-Device LLM Leaderboard &rarr;</a>
HTML
cat > "$OUT/site/methodology.html" <<'HTML'
<!doctype html><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=../methodology.html">
<link rel="canonical" href="https://devicemark.github.io/methodology.html">
<title>Methodology — On-Device LLM Leaderboard</title>
<a href="../methodology.html">Methodology &rarr;</a>
HTML

# 4. llms.txt is served from the site root by convention (/llms.txt) — already at root via step 1

# 5. courtesy: keep the old ../METHODOLOGY.md link from hard-404ing until the
#    index.html link is repointed to methodology.html (renders as plaintext).
[ -f METHODOLOGY.md ] && cp METHODOLOGY.md "$OUT/METHODOLOGY.md" || true

echo "assembled $OUT:"
find "$OUT" -type f | sort
