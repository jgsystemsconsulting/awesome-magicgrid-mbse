# Plan: landing truth gate (P1)

- Date: 2026-09-18
- Spec: docs/superpowers/specs/2026-09-18-landing-truth-gate.md
- Branch: feat/pages-landing
- Repo: awesome-magicgrid-mbse

## Goal

Ship `scripts/check_release.py` and `.github/workflows/validate.yml` so landing chips and section-index anchors cannot drift from RELEASE-INFO/README without a red CI gate.

## Research

research: skipped (no external unknowns; sibling family pattern on local disk is the reference; setup-python SHA already resolved in family)

## Context

- Spec is FCL+ARL clean (Track 1).
- Family reference: ../awesome-archimate/scripts/check_release.py and validate.yml.
- Current tip already has chips version=1.0.0, sweep=2026-09, entries=47 and nine section-index fragments matching CURATED_SECTIONS.

## Tasks

### Task 1: scripts/check_release.py

Create `scripts/check_release.py` implementing the spec Surfaces section exactly.

Steps:

1. Create directory `scripts/` if missing.
2. Write the file with:
   - Lines 1-2 exact CC0 header from the spec.
   - Docstring: `"""Release gate for Awesome MagicGrid MBSE (package P1)."""`
   - Imports only: pathlib, re, subprocess, sys.
3. Implement `fails: list[str] = []` and run all assertions even after earlier failures.
4. Assertion 0: read first 400 chars utf-8 of `scripts/check_release.py`; require both header sentinels with the named finding strings.
5. Assertion 1: REQUIRED list of 12 paths from the spec; `Path(f).is_file()`; `required file missing: {f}`.
6. Assertion 2: `subprocess.run(["git","ls-files"], capture_output=True, text=True)`; non-zero returncode -> `git ls-files failed: exit {code}`; else walk paths for forbidden parts.
7. Assertion 3: globs `scripts/*.py`, `*.md`, `*.txt`, `*.cff`, `docs/**/*.html`; regex `BEGIN [A-Z ]*PRIVATE KEY`; match appends `forbidden content in {path}: BEGIN [A-Z ]*PRIVATE KEY`; scanned count; zero files -> `SCAN_GLOBS matched zero files`.
8. Assertion 4: chip helper `<dt>{name}</dt>\s*<dd>([^<]*)</dd>` for version/sweep/entries; RELEASE-INFO Version field; README sweep badge; entries integer vs curated count.
9. Helper `read_source(path)` utf-8; unreadable -> `unreadable source file: {path}` and skip dependents per spec.
10. Assertion 5: CURATED_SECTIONS tuple (9 titles); ENTRY_RX `^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+\S`; fence tracking; only `- ` bullets under curated sections; `* ` is malformed; heading presence exactly once each; `## Contents` exactly once; return curated_count.
11. Assertion 6: one `ul.section-index`; nine li; one fragment each; zip to `github_slug(title)` for CURATED_SECTIONS order.
12. Output: on fails print `RELEASE GATE FAILED:` plus `  - {f}` lines, `sys.exit(1)`; else `release gate: PASS (scanned {n} files)`.

Done when: file exists on disk with the header and all assertion names present in source.

### Task 2: validate.yml

Create `.github/workflows/validate.yml` with the exact YAML block from the spec (checkout SHA `11d5960a326750d5838078e36cf38b85af677262` # v4, setup-python SHA `a26af69be951a213d495a4c3e4e4022e16d87065` # v5, python 3.12, `python scripts/check_release.py`).

Done when: file exists and both SHAs appear verbatim.

### Task 3: clean run

From repo root:

```bash
python scripts/check_release.py
```

Expect exit 0 and a PASS line with scanned count > 0. Confirm curated count path yields 47 (entries chip already 47).

Done when: exit code 0 observed this session.

### Task 4: seeded drifts

Scratch only; never commit broken state. For each drift: seed, run, assert exit 1 and named finding substring, `git restore` the file.

- Drift A: set version dd in docs/index.html to `0.0.0`. Expect `landing version chip 0.0.0 != RELEASE-INFO Version 1.0.0`.
- Drift B: set entries dd to `48`. Expect `landing entries chip 48 != curated count 47`.
- Drift C: rename `## Community` to `## Forums` in README.md. Expect `curated heading missing from README: Community` and `landing entries chip 47 != curated count 43`.

After all three: `git status` clean (no modified files).

Done when: all three drifts failed as named and tree is clean.

### Task 5: workflow pin check

```bash
grep -n "11d5960a326750d5838078e36cf38b85af677262\|a26af69be951a213d495a4c3e4e4022e16d87065" .github/workflows/validate.yml
```

Both SHAs present. Optionally parse YAML if PyYAML available; structural presence is enough.

Done when: both SHAs verified.

### Task 6: commit

One atomic commit on feat/pages-landing:

```
Add release gate for landing chips and section anchors

scripts/check_release.py asserts version/sweep/entries chips and the
nine section-index fragments against RELEASE-INFO and README.
validate.yml runs the gate on push and PR to main with SHA-pinned actions.
```

Files: `scripts/check_release.py`, `.github/workflows/validate.yml`.

## Out of scope

links.yml, landing copy/CSS, DISTRIBUTION.md, README entry edits, COPYRIGHT/NOTICE.

## Completion

Write `docs/superpowers/plans/2026-09-18-landing-truth-gate-EXECUTED.md` with one line `done` after Tasks 1-6 pass. Parent owns that write after the executor reports complete.
