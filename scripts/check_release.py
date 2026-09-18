# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate for Awesome MagicGrid MBSE (package P1)."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

# --- Assertion 0: script header ---
try:
    head = pathlib.Path("scripts/check_release.py").read_text(encoding="utf-8")[:400]
    if "Copyright (c) 2026 JG Systems Consulting Ltd" not in head:
        fails.append("header missing: scripts/check_release.py")
    if "SPDX-License-Identifier: CC0-1.0" not in head:
        fails.append("SPDX missing: scripts/check_release.py")
except (OSError, UnicodeDecodeError):
    fails.append("unreadable source file: scripts/check_release.py")

# --- Assertion 1: required files ---
REQUIRED = [
    "README.md", "LICENSE", "CHANGELOG.md", "CITATION.cff",
    "SECURITY.md", "CODE_OF_CONDUCT.md", "contributing.md",
    "RELEASE-INFO.txt", "DESIGN.md", "DESIGN_BRIEF.md",
    "docs/index.html", "docs/MATURITY.md", "docs/DISTRIBUTION.md", "scripts/check_release.py",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

# --- Assertion 2: forbidden tracked paths ---
FORBIDDEN_PATH_PARTS = [
    "__pycache__", ".venv", ".worktrees", ".pytest_cache", ".ruff_cache", ".bak",
]
git = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True
)
if git.returncode != 0:
    fails.append(f"git ls-files failed: exit {git.returncode}")
else:
    for f in git.stdout.splitlines():
        if any(part in f for part in FORBIDDEN_PATH_PARTS):
            fails.append(f"forbidden tracked path: {f}")

# --- Assertion 3: forbidden content scan ---
FORBIDDEN_CONTENT = re.compile(r"BEGIN [A-Z ]*PRIVATE KEY")
SCAN_GLOBS = ["scripts/*.py", "*.md", "*.txt", "*.cff", "docs/**/*.html"]
scanned = 0
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        if not path.is_file():
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        if FORBIDDEN_CONTENT.search(text):
            fails.append(f"forbidden content in {path}: BEGIN [A-Z ]*PRIVATE KEY")
if scanned < 1:
    fails.append("SCAN_GLOBS matched zero files")


def read_source(path):
    try:
        return pathlib.Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        fails.append(f"unreadable source file: {path}")
        return None


def landing_chip(html, name):
    hits = re.findall(rf"<dt>{re.escape(name)}</dt>\s*<dd>([^<]*)</dd>", html)
    if len(hits) != 1:
        fails.append(f"landing chip missing or ambiguous: {name}")
        return None
    return hits[0].strip()


release_info = read_source("RELEASE-INFO.txt")
readme = read_source("README.md")
html = read_source("docs/index.html")

# --- Assertion 4: landing chips ---
if release_info is not None:
    version_hits = re.findall(r"(?m)^Version: (\S+)\s*$", release_info)
    if len(version_hits) != 1:
        fails.append(
            f"RELEASE-INFO Version field missing or ambiguous: {len(version_hits)} matches"
        )
    else:
        chip_version = landing_chip(html, "version") if html is not None else None
        if chip_version is not None and chip_version != version_hits[0]:
            fails.append(
                f"landing version chip {chip_version} != RELEASE-INFO Version {version_hits[0]}"
            )

if readme is not None:
    sweep_hits = re.findall(r"!\[Last full sweep: (\d{4}-\d{2})\]", readme)
    if len(sweep_hits) != 1:
        fails.append(f"README sweep badge missing or ambiguous: {len(sweep_hits)} matches")
    else:
        chip_sweep = landing_chip(html, "sweep") if html is not None else None
        if chip_sweep is not None and chip_sweep != sweep_hits[0]:
            fails.append(
                f"landing sweep chip {chip_sweep} != README sweep badge {sweep_hits[0]}"
            )

# --- Assertion 5: curated walk ---
CURATED_SECTIONS = (
    "Official Resources", "Books and Formal Publications",
    "Papers and Case Studies", "Training and Courses",
    "Videos and Talks", "Example Models", "Tool Support",
    "Community", "Related Methodologies",
)
ENTRY_RX = re.compile(r"^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+\S")


def curated_walk(text):
    count = 0
    heading_hits = {title: 0 for title in CURATED_SECTIONS}
    contents_hits = 0
    current = None
    in_fence = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## ") and not line.startswith("###"):
            current = line[3:].strip()
            if current == "Contents":
                contents_hits += 1
            if current in heading_hits:
                heading_hits[current] += 1
            continue
        if current in heading_hits and line.startswith("- "):
            if ENTRY_RX.match(line):
                count += 1
            else:
                fails.append(f"curated entry malformed in {current}: {line[:60]}")
        elif current in heading_hits and line.startswith("* "):
            fails.append(f"curated entry malformed in {current}: {line[:60]}")
    return count, heading_hits, contents_hits


curated_count = None
heading_hits = {}
if readme is not None:
    curated_count, heading_hits, contents_hits = curated_walk(readme)
    if contents_hits == 0:
        fails.append("curated heading missing from README: Contents")
    elif contents_hits > 1:
        fails.append(f"curated heading duplicated in README ({contents_hits}x): Contents")
    for title, hits in heading_hits.items():
        if hits == 0:
            fails.append(f"curated heading missing from README: {title}")
        elif hits > 1:
            fails.append(f"curated heading duplicated in README ({hits}x): {title}")

chip_entries = landing_chip(html, "entries") if html is not None else None
if chip_entries is not None:
    if not re.fullmatch(r"[0-9]+", chip_entries):
        fails.append(f"landing entries chip not an integer: {chip_entries}")
    elif curated_count is not None and int(chip_entries) != curated_count:
        fails.append(
            f"landing entries chip {chip_entries} != curated count {curated_count}"
        )


def github_slug(title):
    return re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")


# --- Assertion 6: section-index ---
if html is not None:
    blocks = re.findall(r'<ul class="section-index">(.*?)</ul>', html, re.DOTALL)
    if len(blocks) != 1:
        fails.append(
            f"landing section-index list missing or ambiguous: {len(blocks)} found"
        )
    else:
        lis = re.findall(r"<li\b[^>]*>.*?</li>", blocks[0], re.DOTALL)
        if len(lis) != 9:
            fails.append(f"section-index li count {len(lis)} != 9")
        else:
            fragments = []
            for li in lis:
                hrefs = re.findall(r'href="[^"#]*#([^"]+)"', li)
                if len(hrefs) != 1:
                    fails.append(f"section-index li href missing or ambiguous: {li[:60]}")
                    fragments = None
                    break
                fragments.append(hrefs[0])
            if fragments is not None:
                expected = [github_slug(t) for t in CURATED_SECTIONS]
                for got, want in zip(fragments, expected):
                    if got != want:
                        fails.append(f"section-index fragment mismatch: {got} != {want}")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print(f"release gate: PASS (scanned {scanned} files)")
