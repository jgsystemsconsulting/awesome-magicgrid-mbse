# Spec and assessment: awesome-acceptability-assessment

Date: 2026-09-18
Package: P5 (distribution-status-ledger)

## Problem

sindresorhus/awesome list PR is deferred until the acceptability gate is assessed. README already carries the Awesome badge.

## Research

Primary sources consulted this session (sibling assessment pattern plus the same official docs):

- https://github.com/sindresorhus/awesome/blob/main/awesome.md
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
- https://github.com/sindresorhus/awesome

research: local assessment with official awesome contribution docs (URLs above)

## Assessment criteria

1. List must be useful and focused; not a dumping ground.
2. Descriptions must be clear and not promotional fluff.
3. Table of contents and consistent formatting.
4. Links must work; dead links fail review.
5. Prefer established resources; avoid low-quality or spam.
6. Naming: Awesome X pattern; avoid trademark abuse.
7. Review bandwidth: maintainers are slow; list must be high quality before PR.
8. Badge and LICENSE expectations for listed projects.

## Awesome MagicGrid MBSE against the bar

| Criterion | Status | Notes |
|---|---|---|
| Focus | PASS | MagicGrid methodology resources only; nine sections, 47 curated entries |
| Format | PASS | awesome-lint + markdownlint on PR; Contents present; consistent `- [title](url) - description` grammar |
| Links | PASS with CI | P3 lychee covers README.md and docs/index.html; PR fails on broken product-surface links; accepted-403 allowlist documented in CHANGELOG |
| Naming | PASS | Awesome MagicGrid MBSE matches Awesome X; independent list, disclaimer present |
| Badge | PASS | awesome.re badge already on README |
| Licence | PASS | CC0-1.0 list; upstream keep own licences; no re-host of Book of Knowledge |
| Depth | PASS | 47 entries is above the thin-list bar that blocked sibling lists at 17 |
| Neutrality | PASS | Independent of Dassault Systemes / No Magic; disclaimer in README |

## Decision

**Go, with prerequisites.** Do not open the sindresorhus/awesome PR in this package.

Prerequisites before submit:

1. feat/pages-landing merged to main and Pages build green so the submitted homepage is the DESIGN landing.
2. Clean lychee run on README.md + docs/index.html under the PR-blocking CI configuration (P3).
3. Org catalogue entry shipped or at least branched (P4) so discovery is not only GitHub search.
4. Re-read the live pull_request_template.md at submit time; fill every checkbox honestly.
5. Confirm maintainer time for review follow-ups after open.

## Out of scope

Opening or drafting the upstream PR. Growing entry count as a prerequisite for go. CI implementation (owned by P3).
