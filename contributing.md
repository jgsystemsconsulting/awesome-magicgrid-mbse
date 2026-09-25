# Contributing to Awesome MagicGrid MBSE

**Lint is mandatory.** awesome-lint on README.md must pass on every push/PR to main. See [MATURITY.md](MATURITY.md).

Suggestions and pull requests are welcome. Every entry and every PR must meet the criteria below.

## Inclusion criteria

1. Stable, reachable URL pointing at the resource itself.
2. Direct MagicGrid methodology relevance: official material, the Book of Knowledge, papers and case studies, talks, training, example models, or tool support for applying the method. Generic SysML language material is excluded (the sister list awesome-sysml-v2 covers it), generic MBSE content beyond the method and named peer methodologies is excluded, and CSS or JavaScript "magic grid" layout libraries are excluded at any quality level. Peer methodologies (OOSEM, Harmony-SE, SYSMOD, Arcadia/Capella) appear only as one-line pointers under Related Methodologies.
3. One-line factual description, no marketing adjectives. When the author or presenter is No Magic or Dassault Systemes staff, the description names that affiliation so readers can weigh the source.
4. Active maintenance (commit within 24 months) or foundational value (the MBSE Grid origin paper, the MagicGrid Book of Knowledge, canonical vendor pages).
5. Not a duplicate of an existing entry, and each URL appears in at most one content section. The intro's sister-list cross-link is not a content entry and is exempt.

Registration-walled links are allowed only when the walled page is the canonical source, for example official vendor training. Never link or host copies of the MagicGrid Book of Knowledge PDF or other copyrighted material; link the Goodreads, publisher, or library catalog page instead.

## Entry format

One line per entry, exactly:

```markdown
- [Name](URL) - Description.
```

The name is the resource or product proper name. The URL is canonical: repo root for GitHub projects, product page for commercial tools, no tracking parameters, no trailing slash on GitHub repo roots. The description is one factual sentence that starts uppercase and ends with a period; a short parenthetical is allowed after the first word, for example "(INCOSE 2024)". Entries are sorted alphabetically, case-insensitive, by link text within each section. Commercial products go in the Tool Support section only.

## Local commands

Run these from the repository root before opening a PR:

```bash
npx awesome-lint@2.3.0 README.md
npx markdownlint-cli2 "README.md" "contributing.md"
```

### Link check

`lychee` is a native binary, not an npm package. Install it once with your platform package manager (`scoop`, `winget`, or `choco` on Windows, `brew` on macOS, `pacman`, `zypper`, `snap`, or `apk` on Linux), then run from the repository root:

```bash
lychee --accept '200,204,301,308,403' README.md
```

Export `GITHUB_TOKEN` (for example `GITHUB_TOKEN=$(gh auth token)`) to avoid GitHub rate limiting on `github.com` links. Third-party sites sometimes return transient timeouts or 429s; retry before treating a failure as a broken link. A 403 is accepted only for canonical vendor sources known to block bots, for example DOIs resolving to Wiley; the accepted set is listed in CHANGELOG.md and enforced at the publication gate.

## Maintenance

Three workflows in `.github/workflows/` run on a fixed cadence. This section states what each does.

### Link scan (weekly)

`links.yml` runs lychee every Monday at 18:00 UTC, on every pull request, and on manual dispatch, with the accept set `200,204,301,308,403` matching the local command above. The check is advisory: a PR with broken links gets a warning but is never blocked by it. The "Link Checker Report" issue is created or updated only when the check exits nonzero; a clean run leaves that issue untouched. The accepted-403 allowlist in CHANGELOG.md is enforced by the publication gate, not by this workflow.

### Freshness report (monthly)

`stale.yml` runs on the first day of each month at 06:00 UTC, or on manual dispatch. It collects the `github.com` repository URLs from README.md and lists repos with no push in the last 24 months. The report is advisory: an entry past the window can still be valid under the foundational-value exception (criterion 4). The "Freshness report" issue is refreshed on every run, including months with no stale entries. Criterion 4 speaks of a commit within 24 months; the report measures the repository's last push, which is usually but not always the same thing.

### Lint gates (every PR and push to main)

`lint.yml` runs `awesome-lint@2.3.0` on README.md, and `markdownlint` on README.md and contributing.md, on every pull request targeting main and every push to main. These gates block merge on failure. The local markdownlint command above installs an unpinned npx package and may differ from the version CI runs; the pinned `awesome-lint@2.3.0` matches CI exactly.
