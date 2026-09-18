# ARL triage log: 2026-09-18-landing-truth-gate

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 numbered lists ignored under curated ## | r1 | r1 | Design | Contract is nine sections of `- [title](url) - desc` bullets. Numbered lists are not the product entry shape; chip measures that grammar only. |
| C2 fence-empty + chip 0 ratifies | r1 | r1 | Design | Empty list with matching chip 0 is consistent dual-surface truth, not silent failure. |
| C3/M forbidden-content no finding string | r1 | r1 | Genuine | Match path has no named fail form; implementer could treat scan as soft. |
| C4/M git ls-files empty-success | r1 | r1 | Genuine | Non-zero git or empty inventory must fail, not pass. |
| M1 side ## sections bypass count | r1 | r1 | Design | Non-curated sections (Contributing, Contents) are intentional; scope is the nine. |
| M2 no on-page id in index.html | r1 | r1 | Design | Section-index targets GitHub README fragments, not landing in-page ids. |
| M3 L106 end-to-end proof overclaim | r1 | r1 | Genuine | Wording overclaims; rewrite to chip==walk only. |
| M4 header required but not runtime-asserted | r1 | r1 | Genuine | Add first-two-lines assert or drop "requires directly". |
| M5 off-site href with hash allowed | r1 | r1 | Design | Absolute GitHub README blob URLs with fragments are the intended product links. |
| M6 unreadable skip A5/A6 undefined | r1 | r1 | Genuine | State A5/A6 preconditions when sources unreadable. |
| M7 AC4 imports wider than Surface 1 | r1 | r1 | Genuine | AC4 must match closed import list. |
| M8 star bullets vs ENTRY_RX | r1 | r1 | Genuine | Spec must pick one: only `- ` valid (drop `* `) or widen ENTRY_RX. Pick only `- `. |
| A secret tripwire scope | r1 | r1 | Advisory-skipped | Stated tripwire, not whole-tree scanner. |
| A version only RELEASE-INFO | r1 | r1 | Design | Out of scope per package; chip contract is RELEASE-INFO only. |
| A three drifts not full matrix | r1 | r1 | Design | Acceptance samples three drifts; not full assertion coverage claim. |
| A self-integrity pin residual | r1 | r1 | Design | Review-only residual accepted for one-script gate. |
| A docstring exact text | r1 | r1 | Advisory-skipped | Cheap template optional; not a runtime fail. |
| A utf-8 encoding | r1 | r1 | Genuine | Require encoding="utf-8" on all text reads. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Forbidden-content no finding string | new_hire, auditor | MAJ | Genuine | Fixed (Assertion 3) |
| git ls-files empty-success | saboteur, auditor | MAJ/CRIT | Genuine | Fixed (Assertion 2) |
| L106 end-to-end proof overclaim | saboteur | MAJ | Genuine | Fixed |
| Header not runtime-asserted | saboteur | MAJ | Genuine | Fixed (Assertion 0) |
| Unreadable skip A5/A6 | auditor | MAJ | Genuine | Fixed |
| AC4 imports wider than Surface 1 | auditor | MAJ | Genuine | Fixed |
| Star bullets vs ENTRY_RX | saboteur, new_hire, auditor | MAJ | Genuine | Fixed (only - valid) |
| Numbered lists / fence+chip0 / side sections / on-page id / off-site href | saboteur | CRIT/MAJ | Design | Wontfix (nine-section contract) |
| Secret tripwire / version-only / three drifts / self-integrity / docstring | mixed | ADV | Advisory-skipped or Design | Skipped |

Fixes applied: 7
Inflation rate: 46% (6/13 CRITICAL+MAJOR triaged Design; remaining genuine fixed)
Validation: SKIP

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Seven genuine fix locs | saboteur, new_hire, auditor | - | resolved by this change | Confirmed |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 7
Document is ready.
