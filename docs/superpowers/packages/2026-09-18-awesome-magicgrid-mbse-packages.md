---
date: 2026-09-18
project: awesome-magicgrid-mbse
mode: light
rounds: 1
input_digest: 9664a42a7d9f1795ccbbd5c9b0f8c1dd02bd307ef8a9d0532d1c125577eb5d85
open_objections: []
---

# Work packages: awesome-magicgrid-mbse (2026-09-18, light mode, round 1)

First package-loop run. Trigger state: landing rebuild plus DESIGN contract
shipped on feat/pages-landing (3 commits over main f60d1a7) with a taste pass
applied. Lens wave returned 14 raw candidates; merge unioned to 6 packages;
triage graded 4 PASS and flagged one critical defect, the P4/P5 dependency
cycle, with an order-level resolution that this cut adopts. One conflict (X1)
escalated and is resolved at the proposal stop by the DESIGN contract.

Dependency order after the cycle fix: P1, P2, P4, P3, P5, P6. P3 runs before
P5 so the acceptability assessment reads enforced CI, not an advisory scan.

## P1: landing-truth-gate

| Field | Value |
|---|---|
| id | P1 |
| name | landing-truth-gate |
| size | M |
| deps | none |
| status | done |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full landing truth gate` |

**Problem.** The product is a dual surface: canonical README list plus the
docs/index.html router. Version, sweep, and entries chips and the nine
section-index anchors are hand-copied into the landing with no check against
README/RELEASE-INFO. This repo has no scripts/ directory and no validate.yml;
nothing runs a release gate at all. A release bump, entry add, or heading
rename desyncs Pages silently while lint and links CI stay green.

**Evidence.**

- docs/index.html evidence chips: `<dt>version</dt><dd>1.0.0</dd>`, `<dt>sweep</dt><dd>2026-09</dd>`, `<dt>entries</dt><dd>47</dd>`
- docs/index.html section-index: nine li anchors to README blob URLs with fragments `#official-resources` through `#related-methodologies`
- RELEASE-INFO.txt:L2, `Version: 1.0.0`
- README.md:L7, sweep badge `![Last full sweep: 2026-09](...)`
- README.md, 47 curated bullets under nine `## ` headings
- Repo has workflows links.yml / lint.yml / stale.yml only; no validate.yml, no scripts/

**In scope.** Add scripts/check_release.py asserting: landing version chip
equals RELEASE-INFO Version; landing sweep chip equals the README sweep badge;
landing entries chip equals the curated bullet count under the nine headings
using this repo's grammar (`- [title](url) - description`, no trailing year
requirement); the single `ul.section-index` carries exactly nine li whose href
fragments equal the GitHub slugs of the nine README headings. Add
.github/workflows/validate.yml running the gate on push and pull_request to
main with SHA-pinned actions; the setup-python pin (sibling SHA
a26af69be951a213d495a4c3e4e4022e16d87065) lives here. Chip dt names
(version/sweep/entries) and the section-index href fragments are frozen gate
inputs; display text may change.

**Out of scope.** Visitor copy and CSS chrome (P2); links.yml args and fail
policy (P3); DISTRIBUTION.md and catalogue work (P4/P5); importing the
archimate trailing-`(YYYY).` entry grammar; README entry content changes.

**Why now.** Locks the evidence contract before P2 edits the same file and
before P4/P5 cite the chips and anchors in external surfaces.

**Triage notes.** PASS, no defects. Merge flagged evidence_free because the
merge dispatch carried lens summaries; the evidence above is restored from the
lens-stage citations, which were resolved against the working tree.

## P2: landing-visitor-copy

| Field | Value |
|---|---|
| id | P2 |
| name | landing-visitor-copy |
| size | S |
| deps | P1 |
| status | done |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full landing visitor copy` |

**Problem.** DESIGN.md promises a full-width primary CTA at the 390px mobile
target, but the shipped `.primary` is inline-flex with no mobile width rule,
so the hero control stays content-width on small viewports. The same file
carries the open chrome nits from the taste pass (no og:image, optional per
DESIGN) and has had no independent copy review against the rebuilt nav, hero,
and section prose.

**Evidence.**

- DESIGN.md Responsive Behaviour: `Mobile (390px target): stacked hero, full-width CTA (>=44px tall)`
- docs/index.html `.primary`: `display: inline-flex; min-height: 44px;` with no mobile width rule
- docs/index.html nav/hero: Top / Status / Sections / Curation / Contribute, single shared `Open full list` CTA label

**In scope.** docs/index.html only: mobile full-width primary CTA rule
matching the DESIGN contract; keep the single shared CTA label; a visitor-copy
sanity pass over nav/hero/evidence/sections/curation/contribute strings,
changing copy only where a concrete jargon leak or unclear referent is found.

**Out of scope.** og:image art generation (X1 resolution: stays out; b-02
holds the row); truth-gate chip and anchor values; links.yml; README entries;
token or contrast changes (already shipped).

**Why now.** Same file P1 freezes; landing CSS and copy settle before the
catalogue and link-check packages point CI and external surfaces at the page.

**Triage notes.** PASS, no defects. X1 (og:image scope in or out of this
package) resolved at the proposal stop: out, because DESIGN.md Imagery says
"no social image for this surface" and the outcome bar does not request one.

## P3: link-check-product-surface

| Field | Value |
|---|---|
| id | P3 |
| name | link-check-product-surface |
| size | S |
| deps | P2 |
| status | ready |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full link check product surface` |

**Problem.** The product is a curated link list, but CI lychee-scans README.md
only, never docs/index.html, and PR runs set fail: false with an advisory
warning step. Landing CTAs, section-index anchors, contribute links, and the
licence footer rot uncaught, and broken product-surface links merge with a
warning.

**Evidence.**

- .github/workflows/links.yml args: `--no-progress --max-retries 3 --accept '200,204,301,308,403' README.md`
- .github/workflows/links.yml: `fail: false` plus advisory-only PR warning step
- docs/index.html: nav/hero README links, nine section-index anchors, contribute links, labs licence-enquiries link

**In scope.** .github/workflows/links.yml only: add docs/index.html to lychee
args; make pull_request runs fail on broken product-surface links while
keeping the scheduled non-PR issue-filing behaviour; keep existing SHA-pinned
action refs and the accept set unless a landing URL forces a documented
allowlist delta.

**Out of scope.** Gate-side chip and fragment assertions (P1); landing
content (P2); stale.yml and lint.yml.

**Why now.** The acceptability assessment (P5) must read enforced CI, not a
seed-time advisory run; the awesome membership bar treats link rot as a
rejection reason.

**Triage notes.** PASS, no defects.

## P4: org-catalogue-entry

| Field | Value |
|---|---|
| id | P4 |
| name | org-catalogue-entry |
| size | M |
| deps | P1, P2 |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full org catalogue entry` |

**Problem.** The org catalogue (labs.jgsystemsconsulting.com) is the named
growth channel for this list, and the landing footer already points visitors
at the labs domain, but no catalogue entry exists in
jgsystemsconsulting-website data/products.yml and that site's rendered
docs/index.html does not list the product.

**Evidence.**

- docs/index.html footer links to labs.jgsystemsconsulting.com/licensing.html
- RELEASE-INFO.txt: Product Awesome MagicGrid MBSE, Version 1.0.0, canonical Pages URL in the landing head
- Sibling pattern: jgsystemsconsulting-website commit 1a67e71 "chore: add awesome-archimate to Labs product catalogue" on branch feat/awesome-archimate-catalogue-entry; website main clean at 1a67e71

**In scope.** In the jgsystemsconsulting-website repository: add the
awesome-magicgrid-mbse entry to data/products.yml following the sibling entry
shape, with fields aligned to RELEASE-INFO and the canonical Pages URL;
regenerate or update the rendered docs/index.html as that site requires;
leave a clean branch ready to merge. In this repository: nothing (the
DISTRIBUTION row update belongs to P5).

**Out of scope.** Merging the website branch (stays ready-for-review by
design); sindresorhus/awesome work; landing HTML.

**Why now.** Catalogue cites the frozen product identity from P1's gated
surfaces; runs after the landing settles (P2) and before the ledger (P5)
records the channel.

**Triage notes.** FAIL on the merged dep list (P4/P5 cycle). Adopted
resolution (b): P4 deps reduce to [P1, P2]; the DISTRIBUTION row update moves
to P5 authoring. Grade is PASS under the corrected deps.

## P5: distribution-status-ledger

| Field | Value |
|---|---|
| id | P5 |
| name | distribution-status-ledger |
| size | S |
| deps | P1, P3, P4 |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion; value proposed this as two packages, unioned here) |
| first_prompt | `/superpowers-process full distribution ledger and awesome acceptability assessment` |

**Problem.** Distribution status has no home: no DISTRIBUTION.md ledger
exists, and the sindresorhus/awesome acceptability gate is unassessed even
though README.md:L1 already carries the Awesome badge. Publish, catalogue,
and awesome-submission state cannot be recorded in one place, and the largest
external channel stays neither pursued nor closed.

**Evidence.**

- No docs/DISTRIBUTION.md in the repo tree
- README.md:L1 Awesome badge claimed
- Sibling ledger shape: awesome-archimate docs/DISTRIBUTION.md channel table with org-catalogue and deferred awesome rows
- This list: 47 entries, CHANGELOG-recorded clean lychee seed run with a 9-link accepted-403 allowlist

**In scope.** Add docs/DISTRIBUTION.md with channel rows (repo, Releases,
Pages, About, org catalogue, sindresorhus/awesome, deliberate N/A rows)
recording honest status against this list's 1.0.0 state, the Pages surface,
and the P4 catalogue branch. Write the acceptability assessment as a separate
spec document (go/no-go plus prerequisites) judged against the membership
bar, this list's 47 entries, and the post-P3 enforced lychee posture; link it
from the awesome row. Assessment only: no awesome PR is opened.

**Out of scope.** The website catalogue edit (P4); opening or drafting the
upstream awesome PR; growing entry count; CI changes.

**Why now.** The ledger is written once against real channel states (P4
branch exists, P3 CI enforced) instead of being patched per package.

**Triage notes.** FAIL on the merged dep list (cycle half). Adopted
resolution (b): P5 deps [P1, P3, P4], order slot 5. Grade is PASS under the
corrected deps.

## P6: ff-merge-pages-landing

| Field | Value |
|---|---|
| id | P6 |
| name | ff-merge-pages-landing |
| size | S |
| deps | P1, P2, P3, P5 |
| status | ready |
| promoted_ids | [] |
| corroboration | 1 (value; risk and cohesion routed it to backlog as release chore) |
| first_prompt | `/superpowers-process full ff merge pages landing` |

**Problem.** feat/pages-landing carries the whole landing programme ahead of
main. The outcome closes only after the branch FF-merges to main, the branch
is deleted, main is pushed, and the GitHub Pages build is verified green;
otherwise the work stays stranded on a feature branch.

**Evidence.**

- Branch state: feat/pages-landing, N commits over main f60d1a7, main clean
- GitHub Pages serves docs/ from main; the landing goes live only after the merge and push

**In scope.** FF-merge feat/pages-landing into main; delete the feature
branch; push origin main (switching gh auth to the org owner account if the
push 403s); confirm the Pages build is green for this repository.

**Out of scope.** Implementing P1-P5; merging the external website catalogue
branch (tracked by P4, stays ready-for-review); tagging a new semver
(RELEASE-INFO already records 1.0.0).

**Why now.** Terminal step; runs only when the in-repo packages are done.

**Triage notes.** PASS. Kept as a package per the outcome bar; risk/cohesion
dissent (release chore) rides in the merge kills. This run drains it last.

## Conflict X1 (resolved at proposal stop)

P2 og:image scope: value lens excluded social-card art (DESIGN says none for
this surface); cohesion lens included og:image as optional. Resolved out of
P2 by the DESIGN contract (Imagery: "no social image for this surface") and
the outcome bar, which does not request one. Backlog row b-02 holds the
residue if a social card is ever wanted.
