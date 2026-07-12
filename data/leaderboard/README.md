# data/leaderboard/ — synced results (populated at launch)

At prep time this directory holds only the dataset tooling:

- `DATASET_CARD.md` — the Hugging Face dataset card (draft; upload is gated)
- `to_parquet.py` — JSONL → Parquet converter for the HF upload

The actual result files — `artifacts.jsonl`, `measurements.jsonl`, `board.json` —
are produced **locally** by the eval workspace's `build_results.py`
(`~/code/coreai/leaderboard/`) and are **synced in at launch**, not committed here
during prep, because that workspace is still actively producing them (the P3 full
battery run). See `../../LAUNCH_CHECKLIST.md` for the sync step.

CI reads whatever `*.jsonl` / `board.json` are present here and deploys them; it
does not run `build_results.py`.
