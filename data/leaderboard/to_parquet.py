#!/usr/bin/env python3
"""Convert the leaderboard result JSONL into Parquet for the HF dataset.

Reads artifacts.jsonl / measurements.jsonl in this directory (synced from the
eval workspace's build_results.py output at launch — see LAUNCH_CHECKLIST.md)
and writes flat, HF-viewer-friendly Parquet next to them.

Nested structs (quality.*, composite.*, retention.*, source.*) are flattened to
dotted columns so the HF dataset viewer renders them as a wide table; list-valued
CI fields are kept as small lists.

    pip install pandas pyarrow        # (or: uv pip install …)
    python to_parquet.py              # writes artifacts.parquet, measurements.parquet
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def read_jsonl(name: str) -> list[dict]:
    p = HERE / name
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def flatten(d: dict, prefix: str = "") -> dict:
    """Flatten nested dicts to dotted keys. Lists (e.g. CI pairs) pass through."""
    out: dict = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            out.update(flatten(v, prefix=f"{key}."))
        else:
            out[key] = v
    return out


def main() -> int:
    try:
        import pandas as pd  # noqa: F401
    except ImportError:
        print("need pandas + pyarrow:  pip install pandas pyarrow", file=sys.stderr)
        return 1
    import pandas as pd

    wrote = []
    for src, dst in (("artifacts.jsonl", "artifacts.parquet"),
                     ("measurements.jsonl", "measurements.parquet")):
        rows = read_jsonl(src)
        if not rows:
            print(f"skip {src} (not present — sync from the eval workspace first)")
            continue
        df = pd.DataFrame([flatten(r) for r in rows])
        df.to_parquet(HERE / dst, index=False)
        wrote.append(f"{dst} ({len(df)} rows, {len(df.columns)} cols)")

    if not wrote:
        print("nothing written — no *.jsonl found. Sync results in first "
              "(LAUNCH_CHECKLIST.md), then re-run.")
        return 1
    print("wrote:", ", ".join(wrote))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
