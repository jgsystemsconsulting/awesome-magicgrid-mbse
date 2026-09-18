# Context: landing-truth-gate (2026-09-18)

Context gate output for the P1 spec. All touched files were authored or read
in-session on branch feat/pages-landing; no stale-context risk.

## Surfaces under gate

- docs/index.html (authored this session): evidence chips `<dt>version</dt><dd>1.0.0</dd>`, `<dt>sweep</dt><dd>2026-09</dd>`, `<dt>entries</dt><dd>47</dd>` inside `dl.chips`; single `ul.section-index` with nine li, each exactly one anchor to `https://github.com/jgsystemsconsulting/awesome-magicgrid-mbse/blob/main/README.md#<fragment>`.
- RELEASE-INFO.txt: `Version: 1.0.0` (single `^Version: (\S+)$` match).
- README.md: sweep badge `![Last full sweep: 2026-09](...)` (single occurrence); nine `## ` curated headings: Official Resources, Books and Formal Publications, Papers and Case Studies, Training and Courses, Videos and Talks, Example Models, Tool Support, Community, Related Methodologies; 47 curated bullets, grammar `- [title](url) - description` (no trailing year); a `## Contents` block above with nine internal anchor links that must not be counted as entries; a Contributing section with a non-entry link line.
- Workflows today: links.yml, lint.yml, stale.yml (all SHA-pinned). No validate.yml, no scripts/.

## Family reference (local disk)

- ../awesome-archimate/scripts/check_release.py: REQUIRED-file walk, forbidden paths/content, header sentinel, landing chip regex `<dt>{name}</dt>\s*<dd>([^<]*)</dd>`, sweep badge regex `!\[Last full sweep: (\d{4}-\d{2})\]`, curated section walk with fence tracking, github_slug(title), section-index fragment zip. Its ENTRY_RX requires trailing `(YYYY).` which this repo's grammar must NOT reuse.
- ../awesome-archimate/.github/workflows/validate.yml: checkout 11d5960a326750d5838078e36cf38b85af677262 # v4, setup-python a26af69be951a213d495a4c3e4e4022e16d87065 # v5, python 3.12, `python scripts/check_release.py`.

## Locked constraints (user + package cut)

- Chip dt names (version, sweep, entries) and section-index href fragments are frozen gate inputs; display text may change.
- Python stdlib only; no new dependencies.
- Gate runs on push and pull_request to main.
- contributing.md is lowercase in this repo (REQUIRED list must match actual filenames, unlike archimate's CONTRIBUTING.md).
- No COPYRIGHT/NOTICE files exist here; do not add them in this package.

## Research gate

research: skipped (no external APIs, libraries, or version-sensitive choices; the reference implementation is the sibling repo on local disk, and the one action SHA needed (setup-python) is already resolved and pinned in the family reference)
