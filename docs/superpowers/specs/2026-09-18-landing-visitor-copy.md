# Spec: landing visitor copy (P2)

## Problem
DESIGN.md promises a full-width primary CTA at the 390px mobile target. Shipped `.primary` was inline-flex content-width. Same file needs a visitor-copy sanity pass.

## Goals
1. Mobile full-width `.primary` rule in docs/index.html.
2. Keep single shared "Open full list" CTA label.
3. Change copy only if a concrete jargon leak is found.

## Non-goals
og:image art; truth-gate values; links.yml; README entries; token changes.

## Acceptance
- `@media (max-width: 639px) { .primary { width: 100%; display: flex; } }` present.
- No visible "Hero" or "Evidence" labels; no FAMILY.md lecture; single CTA label.
- `python scripts/check_release.py` still PASS.

## Research
research: skipped (no external unknowns; DESIGN.md responsive contract is the source)

## Context
Package P2 of docs/superpowers/packages/2026-09-18-awesome-magicgrid-mbse-packages.md. Depends on P1 done.
