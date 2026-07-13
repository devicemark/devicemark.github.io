#!/usr/bin/env python3
"""Generate shields-style SVG badges per board row: /badge/<slug>.svg

Vendors embed them in READMEs:
  [![DeviceMark](https://devicemark.github.io/badge/<slug>.svg)](https://devicemark.github.io/)

Pure stdlib — runs in CI. Left segment = "DeviceMark", right = "71.9% · 45.5 tok/s iPhone 17 Pro".
"""
import json
import sys
from pathlib import Path

CHAR_W = 6.7          # avg px per char at 11px Verdana-ish
PAD = 8
LEFT_BG, RIGHT_BG, TXT = "#3c3b39", "#2a78d6", "#ffffff"


def badge(label: str, value: str) -> str:
    lw = int(len(label) * CHAR_W) + 2 * PAD
    vw = int(len(value) * CHAR_W) + 2 * PAD
    w = lw + vw
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" role="img" aria-label="{label}: {value}">
<title>{label}: {value}</title>
<clipPath id="r"><rect width="{w}" height="20" rx="3" fill="#fff"/></clipPath>
<g clip-path="url(#r)">
<rect width="{lw}" height="20" fill="{LEFT_BG}"/>
<rect x="{lw}" width="{vw}" height="20" fill="{RIGHT_BG}"/>
</g>
<g fill="{TXT}" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
<text x="{lw / 2}" y="14">{label}</text>
<text x="{lw + vw / 2}" y="14">{value}</text>
</g>
</svg>'''


def main():
    board_path, out_dir = sys.argv[1], Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    board = json.loads(Path(board_path).read_text())
    n = 0
    for d in board:
        if not d.get("composite"):
            continue
        slug = d["artifact_id"].split("__")[0]
        comp = f"{d['composite']['value'] * 100:.1f}%"
        if d.get("iphone_tok_s") is not None:
            value = f"{comp} · {d['iphone_tok_s']:g} tok/s iPhone 17 Pro"
        elif d.get("mac_tok_s") is not None:
            value = f"{comp} · {d['mac_tok_s']:g} tok/s M4 Max"
        else:
            value = f"{comp} intelligence composite"
        (out_dir / f"{slug}.svg").write_text(badge("DeviceMark", value))
        n += 1
    print(f"badges: {n} -> {out_dir}")


if __name__ == "__main__":
    main()
