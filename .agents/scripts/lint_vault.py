"""Read-only vault linter for `Arsenal Vault/`. Prints findings; never writes files.

Usage (from the repo root):  python .agents/scripts/lint_vault.py [vault_dir]
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

VAULT = Path(sys.argv[1] if len(sys.argv) > 1 else "Arsenal Vault")
SKIP_DIRS = {".obsidian", ".smart-env", ".trash"}
LINK = re.compile(r"!?\[\[([^\]]+?)\]\]")
FENCE = re.compile(r"```.*?```", re.S)
MIN_CHARS = 80  # below this, a note counts as near-empty


def notes():
    for p in sorted(VAULT.rglob("*.md")):
        if not SKIP_DIRS.intersection(p.parts):
            yield p


def targets(text):
    text = FENCE.sub("", text)  # links inside code fences are not links
    for raw in LINK.findall(text):
        name = raw.split("|")[0].split("#")[0].strip()
        if name:
            yield name


def main():
    if not VAULT.is_dir():
        sys.exit(f"vault not found: {VAULT}")
    files = list(notes())
    titles = {p.stem.lower(): p for p in files}
    inbound = defaultdict(set)
    no_links, broken, short = [], [], []

    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        found = list(targets(text))
        if not found:
            no_links.append(p)
        if len(text.strip()) < MIN_CHARS:
            short.append(p)
        for name in found:
            key = Path(name).name.lower()
            if key in titles:
                if titles[key] != p:
                    inbound[titles[key]].add(p)
            elif Path(name).suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".svg", ".html"}:
                broken.append((p, name))

    orphans = [p for p in files if p not in inbound]
    rel = lambda p: p.relative_to(VAULT).as_posix()

    print(f"Vault: {VAULT}  |  notes: {len(files)}")
    sections = [
        ("No wikilinks", [rel(p) for p in no_links]),
        ("Broken links", [f"{rel(p)}  ->  [[{n}]]" for p, n in broken]),
        ("Orphans (no inbound links)", [rel(p) for p in orphans]),
        (f"Near-empty (<{MIN_CHARS} chars)", [rel(p) for p in short]),
    ]
    for title, items in sections:
        print(f"\n## {title}: {len(items)}")
        for item in items[:60]:
            print(f"  - {item}")
        if len(items) > 60:
            print(f"  ... and {len(items) - 60} more")


if __name__ == "__main__":
    main()
