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

Exit codes: 0 in sync, 1 out of sync, 2 unreadable input, missing field or missing marker.
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


def val(r: dict, key: str) -> int:
    return r[key]["value"]


def render_badges(d: dict) -> str:
    r = d["registry"]
    release_value = "Release_" + d["version"] + "_loaded%2C_not_published"
    items = [
        ("Data licences", "CC_BY--SA_4.0_%2B_CC_BY--NC_4.0", ORANGE, "LICENSE",
         "CC BY-SA 4.0 and CC BY-NC 4.0"),
        ("Status", release_value, ORANGE, "CHANGELOG.md", "release " + d["version"] + " loaded, not published"),
        ("Complete, both packages", badge_number(val(r, "complete")), ORANGE, "#at-a-glance",
         n(val(r, "complete"))),
    ]
    lines = []
    for label, value, color, link, alt in items:
        label_q = label.replace(" ", "_").replace(",", "%2C")
        lines.append(
            f"[![{label}: {alt}]"
            f"(https://img.shields.io/badge/{label_q}-{value}-{color}"
            f"?style=for-the-badge&labelColor={BLACK})]({link})"
        )
    return "\n".join(lines)


def render_glance(d: dict) -> str:
    r = d["registry"]
    rows = [
        ("Complete compounds of the release: approved 3D geometry, SDF and PDBQT", "complete"),
        ("Incomplete compounds, kept apart, in no package and not in the API", "incomplete"),
        ("Complete and incomplete, both areas", "total_both_areas"),
        ("Package AURORA (licence CC BY-SA 4.0)", "package_aurora"),
        ("Package AURORA-NC (licence CC BY-NC 4.0), in addition", "package_aurora_nc"),
        ("Learned embeddings, across both packages", "learned_embeddings"),
        ("Name rows (rows, not distinct names)", "name_rows"),
    ]
    out = ["| | | Read on |", "|---|---:|---|"]
    for label, k in rows:
        out.append(f"| {label} | {n(val(r, k))} | {r[k]['asof']} |")
    out.append("")
    out.append(
        f"*Population: {r['population']}. Status: {d['status']}. The two packages add up to the complete set: "
        f"{n(val(r, 'package_aurora'))} + {n(val(r, 'package_aurora_nc'))} = {n(val(r, 'complete'))}. "
        f"The release as a whole has {n(val(r, 'complete'))} complete compounds, in two packages. "
        f"The embeddings and name rows are row counts of their tables, read in that database; the content of the tables was not compared. "
        f"Each figure carries the date it was read.*"
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
            try:
                body = RENDERERS[name](data)
            except (KeyError, TypeError) as exc:
                print(f"ERROR: data/numbers.json lacks or malforms a field used by '{name}': {exc!r}", file=sys.stderr)
                return 2
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
    def f(v: int) -> dict:
        return {"value": v, "asof": "2000-01-01", "id": "t"}

    sample = {
        "version": "9.9.9",
        "status": "test status",
        "registry": {
            "population": "test population", "total_both_areas": f(1234), "complete": f(1000),
            "incomplete": f(234), "package_aurora": f(900), "package_aurora_nc": f(100),
            "learned_embeddings": f(1000), "name_rows": f(5678),
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
        text = (root / "README.md").read_text(encoding="utf-8")
        assert "1,234" in text and "900 + 100 = 1,000" in text and "5,678" in text
        sample["registry"]["package_aurora"] = f(901)
        (root / "data" / "numbers.json").write_text(json.dumps(sample), encoding="utf-8")
        assert process(root, check=True) == 1, "a changed value must fail --check"
        (root / "data" / "numbers.json").write_text(json.dumps({**sample, "registry": {}}), encoding="utf-8")
        assert process(root, check=True) == 2, "a missing field must fail with 2, not crash"
        (root / "data" / "numbers.json").write_text(json.dumps(sample), encoding="utf-8")
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
