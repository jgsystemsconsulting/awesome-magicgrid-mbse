# Spec: link-check product surface (P3)

## Problem
links.yml lychee scanned README.md only with fail:false and advisory PR warnings. docs/index.html product links were unchecked.

## Goals
1. Lychee args cover README.md and docs/index.html.
2. pull_request runs fail on broken product-surface links.
3. Keep SHA-pinned actions and accept set 200,204,301,308,403.
4. Keep non-PR issue-filing behaviour.

## Acceptance
- args include both files and --include-fragments=anchor-only (family pattern) with the existing accept set.
- PR step exits 1 on lychee non-zero.
- Scheduled path still files Link Checker Report issues.

## Research
research: skipped (family links.yml pattern from awesome-archimate on local disk)
