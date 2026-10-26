#!/usr/bin/env python3
"""Check the links of this repository without calling the network.

  * relative links and images must point to a file or folder that exists;
  * an anchor (#section) must match a heading of the target Markdown file (GitHub rules);
  * every link to the AURORA platform must be listed in data/site-links.json, the one list to check when the
    platform release changes;
  * external links are listed, never called.

Fenced code blocks are skipped. Usage (from the repository root, or pass --root):
    python scripts/check_links.py
    python scripts/check_links.py --selftest

Exit codes: 0 clean, 1 broken link or unlisted platform link, 2 unreadable input or no file read.
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

SKIP_DIRS = {".git"}
TEXT_EXT = {".md", ".yml", ".yaml", ".cff"}
LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_ATTR = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""")
BARE_URL = re.compile(r"""https?://[^\s)>"'`\]]+""")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")
PLATFORM_HOST = "aurora.alchemia.solutions"


def slug(heading: str) -> str:
    text = re.sub(r"`|\*|_|\[|\]|\([^)]*\)", lambda m: "" if m.group(0) in "`*_[]" else "", heading)
    text = re.sub(r"[^\w\- ]", "", text.lower())
    return text.strip().replace(" ", "-")


def strip_fences(text: str) -> str:
    out, fenced = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else line)
    return "\n".join(out)


def anchors_of(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    result = set()
    for line in strip_fences(path.read_text(encoding="utf-8")).split("\n"):
        m = HEADING.match(line)
        if not m:
            continue
        s = slug(m.group(1))
        n = seen.get(s, 0)
        seen[s] = n + 1
        result.add(s if n == 0 else f"{s}-{n}")
    return result


def load_listed(root: Path) -> set[str]:
    data = json.loads((root / "data" / "site-links.json").read_text(encoding="utf-8"))
    return {item["url"].rstrip("/") for item in data["links"]} | {data["base"].rstrip("/")}


def check(root: Path) -> int:
    try:
        listed = load_listed(root)
    except (OSError, ValueError, KeyError) as exc:
        print(f"ERROR: data/site-links.json unreadable or malformed: {exc}", file=sys.stderr)
        return 2
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.suffix in TEXT_EXT and not (set(p.relative_to(root).parts) & SKIP_DIRS)
    )
    if not files:
        print("ERROR: no file to check", file=sys.stderr)
        return 2
    broken: list[str] = []
    external: dict[str, list[str]] = {}
    for f in files:
        rel = f.relative_to(root).as_posix()
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"ERROR: cannot read {rel}: {exc}", file=sys.stderr)
            return 2
        body = strip_fences(text) if f.suffix == ".md" else text
        targets = [(m.group(1), body.count("\n", 0, m.start()) + 1) for m in LINK.finditer(body)]
        targets += [(m.group(1), body.count("\n", 0, m.start()) + 1) for m in HTML_ATTR.finditer(body)]
        targets += [(m.group(0).rstrip(".,;:"), body.count("\n", 0, m.start()) + 1) for m in BARE_URL.finditer(body)]
        for target, line in targets:
            if target.startswith("mailto:"):
                continue
            parsed = urlparse(target)
            if parsed.scheme in ("http", "https"):
                url = target.split("#")[0].split("?")[0].rstrip("/")
                external.setdefault(url, []).append(f"{rel}:{line}")
                if parsed.netloc == PLATFORM_HOST and url not in listed:
                    broken.append(f"{rel}:{line}: platform link not in data/site-links.json: {url}")
                continue
            if parsed.scheme:
                continue
            path_part, _, frag = target.partition("#")
            dest = f if not path_part else (f.parent / unquote(path_part)).resolve()
            if path_part and not dest.exists():
                broken.append(f"{rel}:{line}: missing target {path_part}")
                continue
            if frag and dest.is_file() and dest.suffix == ".md":
                if frag.lower() not in anchors_of(dest):
                    broken.append(f"{rel}:{line}: no heading for anchor #{frag} in {dest.name}")
    for b in broken:
        print(f"BROKEN {b}")
    print(f"external links, not called ({len(external)}):")
    for url in sorted(external):
        print(f"  {url}  <- {', '.join(external[url][:3])}")
    print(f"checked {len(files)} files, {len(broken)} broken")
    return 1 if broken else 0


def selftest() -> int:
    sample_links = {"base": "https://aurora.alchemia.solutions",
                    "links": [{"key": "home", "url": "https://aurora.alchemia.solutions/home"}]}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "data").mkdir()
        (root / "docs").mkdir()
        (root / "data" / "site-links.json").write_text(json.dumps(sample_links), encoding="utf-8")
        (root / "docs" / "A.md").write_text("# Title\n\n## Second part\n", encoding="utf-8")
        (root / "README.md").write_text(
            "# Home\n[a](docs/A.md#second-part) [b](#home) [site](https://aurora.alchemia.solutions/home)\n"
            "```\n[ignored](nowhere.md)\n```\n", encoding="utf-8")
        assert check(root) == 0, "a clean tree must pass"
        (root / "README.md").write_text("# Home\n[x](docs/missing.md)\n", encoding="utf-8")
        assert check(root) == 1, "a missing file must fail"
        (root / "README.md").write_text("# Home\n[x](docs/A.md#nope)\n", encoding="utf-8")
        assert check(root) == 1, "a missing anchor must fail"
        (root / "README.md").write_text("# Home\n[x](https://aurora.alchemia.solutions/other)\n", encoding="utf-8")
        assert check(root) == 1, "an unlisted platform link must fail"
        (root / "README.md").write_bytes(b"\xff\xfe\x00bad")
        assert check(root) == 2, "an unreadable file must fail with 2"
        (root / "README.md").write_text("# Home\n", encoding="utf-8")
        (root / "data" / "site-links.json").write_text("{broken", encoding="utf-8")
        assert check(root) == 2, "a broken link list must fail with 2"
    print("selftest ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    return selftest() if args.selftest else check(Path(args.root))


if __name__ == "__main__":
    sys.exit(main())
