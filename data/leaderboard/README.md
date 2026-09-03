# data/leaderboard/

The committed results behind the board, plus the dataset tooling.

- `board.json` — the ranked board the site renders (also served at
  `https://devicemark.github.io/data/leaderboard/board.json`)
- `artifacts.jsonl`, `measurements.jsonl` — the normalized tables published to the
  [Hugging Face dataset](https://huggingface.co/datasets/devicemark/results)
- `codec_preview.json` — the Anchored-ops preview track
- `DATASET_CARD.md` — the dataset card; `to_parquet.py` — JSONL → Parquet for the upload

These files are written by the scorer in the eval workspace and committed here as data.
CI deploys whatever is present; it does not run the scorer. Please do not hand-edit rows;
to get a model on the board, open a
[row request](https://github.com/devicemark/devicemark.github.io/issues/new?template=submit-your-model.yml).
