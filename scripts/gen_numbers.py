#!/usr/bin/env python3
"""Render the numbers of this repository from data/numbers.json.

The README carries blocks between markers:

    <!-- numbers:begin NAME -->
    ...generated...
    <!-- numbers:end NAME -->

Usage (run from the repository root, or pass --root):
    python scripts/gen_numbers.py            # rewrite the blocks
    python scripts/gen_numbers.py --check    # exit 1 if a block differs from the data
    python scripts/gen_numbers.py --selftest

Exit codes: 0 in sync, 1 out of sync, 2 unreadable input or missing marker.
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

ORANGE = "FF9E00"
BLACK = "000000"
GRAY = "808080"


def n(value: int) -> str:
    return f"{value:,}"


def badge_number(value: int) -> str:
    return f"{value:,}".replace(",", "%2C")


def render_badges(d: dict) -> str:
    r = d["registry"]
    items = [
        ("Data licence", "CC_BY--SA_4.0_%2B_CC_BY--NC_4.0", ORANGE, "LICENSE", "CC BY-SA 4.0 and CC BY-NC 4.0"),
        ("Registry", d["version"] + "_(unreleased)", ORANGE, "CITATION.cff", d["version"] + " (unreleased)"),
        ("Compounds", badge_number(r["compounds"]), ORANGE, "#at-a-glance", n(r["compounds"])),
        ("Sources", str(r["sources"]), GRAY, "docs/SOURCES.md", str(r["sources"])),
    ]
    lines = []
    for label, value, color, link, alt in items:
        label_q = label.replace(" ", "_")
        lines.append(
            f"[![{label}: {alt}]"
            f"(https://img.shields.io/badge/{label_q}-{value}-{color}"
            f"?style=for-the-badge&labelColor={BLACK})]({link})"
        )
    return "\n".join(lines)


def render_glance(d: dict) -> str:
    r = d["registry"]
    rows = [
        ("Compounds in the registry (both areas)", r["compounds"]),
        ("Complete: approved 3D geometry, SDF and PDBQT", r["complete"]),
        ("Incomplete: full identity, no approved 3D geometry", r["incomplete"]),
        ("In the AURORA package (CC BY-SA 4.0)", r["package_aurora"]),
        ("In the AURORA-NC package (CC BY-NC 4.0)", r["package_aurora_nc"]),
        ("Public sources", r["sources"]),
        ("Raw source records read", r["raw_records"]),
        ("Names and synonyms", r["names_and_synonyms"]),
        ("Learned embeddings (768 dimensions)", r["learned_embeddings"]),
        ("Bioactivity measurements", r["bioactivity_measurements"]),
    ]
    out = ["| | |", "|---|---:|"]
    out += [f"| {label} | {n(v)} |" for label, v in rows]
    out.append("")
    out.append(
        f"*Population: the AURORA registry, release {d['version']}, unpublished. Read on {r['asof']}. "
        f"Source: {r['source']}. Complete and incomplete add up to the registry; a compound is in "
        f"exactly one package.*"
    )
    return "\n".join(out)


RENDERERS = {"badges": render_badges, "glance": render_glance}
TARGETS = {"README.md": ("badges", "glance")}


def block_re(name: str) -> re.Pattern:
    return re.compile(
        rf"(<!-- numbers:begin {name} -->\n)(.*?)(\n<!-- numbers:end {name} -->)", re.DOTALL
    )


def process(root: Path, check: bool) -> int:
    try:
        data = json.loads((root / "data" / "numbers.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"ERROR: cannot read data/numbers.json: {exc}", file=sys.stderr)
        return 2
    status = 0
    for rel, names in TARGETS.items():
        path = root / rel
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"ERROR: cannot read {rel}: {exc}", file=sys.stderr)
            return 2
        new = text
        for name in names:
            rx = block_re(name)
            if not rx.search(new):
                print(f"ERROR: {rel} has no block '{name}'", file=sys.stderr)
                return 2
            body = RENDERERS[name](data)
            new = rx.sub(lambda m: m.group(1) + body + m.group(3), new)
        if new != text:
            if check:
                print(f"OUT OF SYNC: {rel}")
                status = 1
            else:
                path.write_text(new, encoding="utf-8", newline="\n")
                print(f"updated {rel}")
        else:
            print(f"in sync {rel}")
    return status


def selftest() -> int:
    sample = {
        "version": "9.9.9",
        "registry": {
            "asof": "2000-01-01", "source": "test", "compounds": 1234, "complete": 1000,
            "incomplete": 234, "package_aurora": 900, "package_aurora_nc": 100, "sources": 3,
            "raw_records": 5000, "names_and_synonyms": 7000, "learned_embeddings": 1200,
            "bioactivity_measurements": 10,
        },
    }
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "data").mkdir()
        (root / "data" / "numbers.json").write_text(json.dumps(sample), encoding="utf-8")
        marker = "<!-- numbers:begin {0} -->\nold\n<!-- numbers:end {0} -->\n"
        (root / "README.md").write_text(marker.format("badges") + marker.format("glance"), encoding="utf-8")
        assert process(root, check=True) == 1, "stale blocks must fail --check"
        assert process(root, check=False) == 0
        assert process(root, check=True) == 0, "regenerated blocks must pass --check"
        assert "1,234" in (root / "README.md").read_text(encoding="utf-8")
        (root / "README.md").write_text("no markers", encoding="utf-8")
        assert process(root, check=True) == 2, "a missing marker must fail with 2"
        (root / "data" / "numbers.json").write_text("{broken", encoding="utf-8")
        assert process(root, check=True) == 2, "unreadable data must fail with 2"
    print("selftest ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return process(Path(args.root), args.check)


if __name__ == "__main__":
    sys.exit(main())
