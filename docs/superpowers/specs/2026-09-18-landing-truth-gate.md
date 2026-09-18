# Spec: landing truth gate (package P1, awesome-magicgrid-mbse)

- Date: 2026-09-18
- Branch: feat/pages-landing
- Package: P1 of docs/superpowers/packages/2026-09-18-awesome-magicgrid-mbse-packages.md
- Family reference: ../awesome-archimate/scripts/check_release.py and ../awesome-archimate/.github/workflows/validate.yml (read-only; adapt, do not copy blindly)

## Problem

The product is a dual surface: README.md is the canonical curated list, docs/index.html is the GitHub Pages router. The landing repeats three evidence chips (version, sweep, entries) and nine section-index anchors, all hand-copied from README.md and RELEASE-INFO.txt. Nothing compares the copies to the sources. This repo has no scripts/ directory and no validate.yml, so no release gate runs at all. A version bump, an entry add, or a heading rename desyncs Pages silently while lint and links CI stay green.

Current source values (verified on this branch):

- RELEASE-INFO.txt: `Version: 1.0.0`
- README.md line 7: sweep badge `![Last full sweep: 2026-09](...)`
- README.md: 47 curated bullets under nine `## ` headings (4 + 2 + 12 + 4 + 10 + 3 + 3 + 4 + 5)
- docs/index.html: chips `<dt>version</dt><dd>1.0.0</dd>`, `<dt>sweep</dt><dd>2026-09</dd>`, `<dt>entries</dt><dd>47</dd>`; single `ul.section-index` with nine li

## Goals / Non-goals

Goals:

1. `scripts/check_release.py`: Python stdlib only, CC0 header, asserting the exact set in "Surfaces and exact assertions" below. Collects all failures into one list, exits 1 with named findings, prints one PASS line when clean.
2. `.github/workflows/validate.yml`: runs the gate on push and pull_request to main, SHA-pinned actions, contents: read only.
3. Gate inputs frozen so P2 (landing copy) and P4/P5 (external surfaces citing the chips) build against an enforced contract.

Non-goals:

- links.yml changes, including lychee args and fail policy (P3)
- Landing copy, CSS, mobile CTA (P2)
- docs/DISTRIBUTION.md authoring (P5)
- README entry content edits
- The archimate trailing-`(YYYY).` entry grammar. This repo's entries carry no trailing year, and the gate must not require one. The family's `ENTRY_RX ... \(\d{4}\)\.$` is deliberately not reused.
- COPYRIGHT and NOTICE files (do not exist here, do not create them)
- A multi-file header-sentinel loop over scripts/*.py. Assertion 0 checks this one script's header; generalize when a second script lands.

## Locked constraints

User and package-cut decisions that the implementation must not reopen:

1. Chip dt names `version`, `sweep`, `entries` and the section-index href fragments are frozen gate inputs. Display text (li anchor labels, dd rendering) may change freely.
2. Python standard library only. No new dependencies, no pip install step in CI.
3. The gate runs on push to main and pull_request to main.
4. `contributing.md` is lowercase in this repo. The REQUIRED list must use the tracked name byte-exact. On a case-insensitive local filesystem (Windows) the file check is lenient; CI on ubuntu-latest is the enforcer.
5. No COPYRIGHT or NOTICE files exist here; this package does not add them.
6. The nine curated section titles are frozen as the `CURATED_SECTIONS` tuple. Renaming one is a gate-visible event that forces a coordinated README plus landing change in the same commit.

## Surfaces and exact assertions

### Surface 1: scripts/check_release.py (new file)

First two lines, exact:

```python
# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
```

Docstring names the repo and package (template: `"""Release gate for Awesome MagicGrid MBSE (package P1)."""`). Imports exactly: `pathlib`, `re`, `subprocess`, `sys`. No other imports. No CLI arguments, no config file, no writes to disk. Run context: repository root as working directory, git on PATH (both hold in CI after checkout). All text reads use `encoding="utf-8"`.

The gate collects failures in a `fails` list and performs every check even after earlier ones fail.

Assertion 0: script header. Read the first 400 characters of `scripts/check_release.py` (utf-8). Fail with `header missing: scripts/check_release.py` if `Copyright (c) 2026 JG Systems Consulting Ltd` is absent. Fail with `SPDX missing: scripts/check_release.py` if `SPDX-License-Identifier: CC0-1.0` is absent.

Assertion 1: required files. Each of the following must exist as a file, checked with `pathlib.Path(f).is_file()`:

```python
REQUIRED = [
    "README.md", "LICENSE", "CHANGELOG.md", "CITATION.cff",
    "SECURITY.md", "CODE_OF_CONDUCT.md", "contributing.md",
    "RELEASE-INFO.txt", "DESIGN.md", "DESIGN_BRIEF.md",
    "docs/index.html", "docs/DISTRIBUTION.md", "scripts/check_release.py",
]
```

Missing entry appends `required file missing: {f}`.

Decision, docs/DISTRIBUTION.md: required. P5 authored the file and appended it to REQUIRED in the same change so every REQUIRED entry is true at gate time. `docs/superpowers/backlog.md` (present today) is not gated: it is an internal planning artifact and its absence must not block a release. This repo tracks no `.gitignore`, so none is listed.

Assertion 2: forbidden tracked paths. Run `git ls-files` via subprocess with `capture_output=True` and `text=True`. If returncode is non-zero, append `git ls-files failed: exit {code}` and skip the path walk. Otherwise split stdout on newlines; for each tracked path, a failure if any of these parts appears in the path: `__pycache__`, `.venv`, `.worktrees`, `.pytest_cache`, `.ruff_cache`, `.bak`. Failure form: `forbidden tracked path: {f}`.

Assertion 3: forbidden content scan. One regex, `BEGIN [A-Z ]*PRIVATE KEY`, over exactly these glob patterns: `scripts/*.py`, `*.md`, `*.txt`, `*.cff`, `docs/**/*.html`. For each matched file, read utf-8 (errors="ignore") and on a regex hit append `forbidden content in {path}: BEGIN [A-Z ]*PRIVATE KEY`. Count files scanned across all globs; a zero count is itself a failure (`SCAN_GLOBS matched zero files`), guarding against glob typos making the scan a silent no-op. The family also scans `docs/**/*.md`; this dispatch enumerates five globs, and the delta is accepted: the scan is a tripwire for leaked secrets in release surfaces, not a whole-tree scanner.

Assertion 4: landing chips. Chip extraction regex per name: `<dt>{name}</dt>\s*<dd>([^<]*)</dd>` (names are the frozen lowercase dt strings; `\s*` spans the newline inside `div.chip`). Exactly one hit per name, else `landing chip missing or ambiguous: {name}`.

- version: exactly one `(?m)^Version: (\S+)\s*$` in RELEASE-INFO.txt, else `RELEASE-INFO Version field missing or ambiguous`. The single hit must equal the version chip dd, else `landing version chip {got} != RELEASE-INFO Version {want}`.
- sweep: exactly one `!\[Last full sweep: (\d{4}-\d{2})\]` in README.md, else `README sweep badge missing or ambiguous`. Must equal the sweep chip dd, else `landing sweep chip {got} != README sweep badge {want}`.
- entries: chip dd must fullmatch `[0-9]+`, else `landing entries chip not an integer`. Must equal the curated bullet count from Assertion 5, else `landing entries chip {got} != curated count {want}`.

Unreadable source files (RELEASE-INFO.txt, README.md, docs/index.html) are failures on their own (`unreadable source file: {path}`). When a source is unreadable: skip Assertion 4 comparisons that depend on it; skip Assertion 5 entirely if README is unreadable; skip Assertion 6 entirely if docs/index.html is unreadable. Do not invent empty defaults that would make later comparisons pass.

Assertion 5: curated walk. Hard-coded, order-fixed:

```python
CURATED_SECTIONS = (
    "Official Resources", "Books and Formal Publications",
    "Papers and Case Studies", "Training and Courses",
    "Videos and Talks", "Example Models", "Tool Support",
    "Community", "Related Methodologies",
)
ENTRY_RX = re.compile(r"^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+\S")
```

Walk README.md line by line with fence tracking (a stripped line starting with three backticks toggles an in-fence flag; fenced lines are skipped, so code samples never count). A stripped line starting with `## ` switches the current section to the text after `## `. Only while the current section is one of CURATED_SECTIONS, examine entry candidates: a stripped line starting with `- ` either matches ENTRY_RX as a prefix match (title, absolute http(s) URL, ` - `, description starting with a non-space and running to end of line, no trailing-year requirement) and increments the count, or it fails the regex and appends `curated entry malformed in {section}: {line[:60]}`. Only the `- ` bullet marker is valid; lines starting with `* ` under a curated section are malformed. Numbered lists and prose under curated headings are ignored (they are not the product entry shape). Example of a grammar-valid bullet: `- [CATIA Magic training catalog](https://www.3ds.com/edu/catia-magic-training) - Official Dassault Systemes catalog of CATIA Magic and Cameo training courses, including MagicGrid offerings.`

Each curated heading is tallied on an exact stripped match `## {title}`. Zero hits appends `curated heading missing from README: {title}`; more than one appends `curated heading duplicated in README ({n}x): {title}`.

Contents exclusion: the `## Contents` block (nine internal-anchor bullets such as `- [Official Resources](#official-resources)`) is excluded by construction because the walk counts only under the nine curated headings. Assert `## Contents` appears exactly once (same missing/duplicated findings form as above) so a stray second Contents heading cannot shadow a curated section. The entries-chip equality in Assertion 4 proves only that the chip equals the curated walk count under the nine headings (47 today). It does not scan the whole README for every link-shaped line.

Assertion 6: section-index. Find `ul class="section-index"` blocks with `re.findall(r'<ul class="section-index">(.*?)</ul>', html, re.DOTALL)`. Exactly one block, else `landing section-index list missing or ambiguous: {n} found`. Inside it, exactly nine `<li>...</li>` elements, else `section-index li count {n} != 9`. Each li carries exactly one `href="[^"#]*#([^"]+)"` match, else `section-index li href missing or ambiguous: {li[:60]}`. Compare the nine fragments, in order, against `[github_slug(t) for t in CURATED_SECTIONS]` where `github_slug(title)` is `re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")`. Any mismatch appends `section-index fragment mismatch: {got} != {want}`.

Expected heading-to-fragment table (all nine anchors exist in docs/index.html today):

| README heading | fragment |
|---|---|
| Official Resources | official-resources |
| Books and Formal Publications | books-and-formal-publications |
| Papers and Case Studies | papers-and-case-studies |
| Training and Courses | training-and-courses |
| Videos and Talks | videos-and-talks |
| Example Models | example-models |
| Tool Support | tool-support |
| Community | community |
| Related Methodologies | related-methodologies |

Output contract: if `fails` is non-empty, print `RELEASE GATE FAILED:` followed by one `  - {finding}` line per failure, exit 1. Otherwise print `release gate: PASS (scanned {scanned} files)` and exit 0.

### Surface 2: .github/workflows/validate.yml (new file)

Exact content (family-identical; the job name, runs-on, and both pins carry over unchanged):

```yaml
name: validate

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Set up Python
        uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5
        with:
          python-version: "3.12"
      - name: Run release gate
        run: python scripts/check_release.py
```

No other workflow files change. The existing links.yml, lint.yml, and stale.yml stay untouched.

## Acceptance criteria

1. Clean run. `python scripts/check_release.py` from the repository root on the feat/pages-landing tip exits 0 and prints the PASS line with a scanned count greater than zero. All 12 REQUIRED files exist at their tracked names, and the counted curated bullets are 47.
2. Seeded drift verification (scratch edits in the working tree; seed, run, revert with `git restore <file>`; never commit a broken state). Each drift must exit 1 with the named findings:
   - Drift A, version chip mismatch: set the version dd in docs/index.html to `0.0.0`. Expected finding includes `landing version chip 0.0.0 != RELEASE-INFO Version 1.0.0`.
   - Drift B, entries chip off-by-one: set the entries dd to `48`. Expected finding includes `landing entries chip 48 != curated count 47`.
   - Drift C, renamed section heading: rename `## Community` to `## Forums` in README.md. Expected findings include `curated heading missing from README: Community` and `landing entries chip 47 != curated count 43` (Community's four bullets leave the count). Assertion 6 compares landing fragments to hard-coded CURATED_SECTIONS slugs, not live README titles, so a README-only rename does not produce a section-index fragment mismatch.
   After the three runs, `git status` reports a clean tree with no modified files.
3. Workflow validity. validate.yml parses as YAML with any available parser; structurally it is the family reference with no deltas, and both action SHAs appear verbatim.
4. Stdlib-only check. The script imports only pathlib, re, subprocess, and sys. No other imports anywhere.

## Research

research: skipped (no external unknowns; sibling family pattern on local disk is the reference; setup-python SHA already resolved in family)

## Context

Context gate output: docs/superpowers/context/2026-09-18-landing-truth-gate-context.md. It records the exact chip markup, the RELEASE-INFO and README source lines, the nine-heading list, today's workflow inventory (links.yml, lint.yml, stale.yml; no validate.yml, no scripts/), the locked constraint list, and the family reference behaviors including the one grammar difference (archimate ENTRY_RX requires a trailing `(YYYY).`; this repo must not). Work package contract: docs/superpowers/packages/2026-09-18-awesome-magicgrid-mbse-packages.md, section "P1: landing-truth-gate", which fixes scope, the dependency position (P1 first; P2 edits the same landing file next), and the frozen-input rule.
