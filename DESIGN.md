# DESIGN.md: Awesome MagicGrid MBSE

## Product

**Name:** Awesome MagicGrid MBSE  
**Purpose:** Public-domain curated index of MagicGrid MBSE methodology resources: official material, the Book of Knowledge, papers and case studies, training, talks, example models, tool support, and peer-methodology pointers.  
**Primary users:** MBSE practitioners who already know the domain.  
**Primary actions:** Scan section index, open an upstream resource, open the full README list, suggest a resource or report a dead link.  
**Surface:** One GitHub Pages landing (`docs/index.html` path family) with in-page anchors. README on GitHub stays the canonical deep list unless a later pass mirrors entries under this contract without drift.

## Design Direction

- **Primary style:** minimal-technical  
- **Secondary influence:** none (cool technical system only; no warm SaaS token blend)  
- **Reference influences:** Vercel (restraint, mono metadata, one claim per viewport), Primer (dense functional UI, tag/state colour), Linear (type-led hierarchy and short motion on a **light** shell only)  
- **Impression constraints:** credible, precise, quiet, dense-tolerant, navigable  
- **Patterns:** progressive-disclosure (section summary then depth via anchors); light homepage-composition for top argument order only  
- **Override note:** none  
- **Avoid:** gradient heroes, glass, emoji chrome, violet/indigo defaults, three equal feature cards, stock photos, multi-hue tags, centre-everything, unthemed shadcn defaults, CDN fonts, accordion-hiding the list

## Design Principles

1. **The list is the product.** Chrome exists to route attention to sections and links, never to perform brand theatre.  
2. **One accent, everywhere.** Interactive and live states only; tags stay neutral chips with mono labels.  
3. **Depth without traps.** Summaries first, stable anchors for deep content; never hide the catalogue behind hover or forced accordions.

## Colour System

Family tokens from the awesome-archimate contract, reused unchanged so sibling landings read as one system. Derived inside minimal-technical ranges (cool neutrals, accent hue 250-256). Concrete tokens:

```css
--color-bg: oklch(0.985 0.006 255);
--color-surface-1: oklch(0.995 0.005 255);
--color-surface-2: oklch(0.998 0.004 255);
--color-surface-3: oklch(1.0 0 0);
--color-primary: oklch(0.19 0.015 260);
--color-accent: oklch(0.58 0.17 253);
--color-text: oklch(0.17 0.012 258);
--color-text-muted: oklch(0.50 0.012 258);
--color-border: oklch(0.915 0.008 255);
--color-focus-ring: var(--color-accent);
--color-success: oklch(0.45 0.10 150);
--color-danger: oklch(0.50 0.14 25);
--color-attention: oklch(0.55 0.12 85);
```

**Derivation notes:** bg/surfaces stay near-white with cool 255 hue so the page reads as one system. Primary and text are near-black ink (no coloured headings). Accent is a single blue at hue 253 inside 250-256, reserved for links, focus, active nav, and the primary CTA border/fill. Semantic colours are functional only (issue/success states), not decoration. Tag chips use surface-1 + border + muted text; never per-tag rainbow hues.

## Typography

- **Display/body:** IBM Plex Sans (self-hosted under `docs/fonts/`; no CDN; OFL licence disclosed alongside)  
- **Monospace:** IBM Plex Mono for versions, dates, tags, slugs, entry metadata  
- **Scale (1.25 from 16px):** 12.8 (meta), 16 (body), 20 (h3), 25 (h2), 31 (h1)  
- **Weights:** 400 body, 500 labels/emphasis/entry titles, 600 section headings  
- **Rules:** Headings distinguished by weight and size, never by colour alone. Prose measure 65-75ch. Tabular nums for counts and years where aligned.

## Layout

- Content max width **1120px**; prose blocks clamp to ~70ch inside that shell  
- **12-column** mental grid; section index as compact two-column list on wide viewports (stacked on mobile), not centred card deck  
- Spacing scale: 4 / 8 / 16 / 32 / 56 (xl). Major sections separated by **64-96px**  
- Density high inside entry blocks; dividers are 1px border, not cards  
- Sticky top nav; no fixed multi-panel app chrome

## Shape Language

- Radius: sm **3px**, md **5px**, lg **7px**  
- Hairline borders (`1px solid var(--color-border)`)  
- Elevation: none by default; at most one soft shadow on the primary CTA  
- Dividers separate entries; avoid boxed card stacks

## Components

| Need | Source |
|---|---|
| Page shell, nav, footer | Custom, tokens above (existing `docs/index.html` is the seed; restyle to this contract) |
| Primary/secondary buttons | Custom button styles mapped to primary/accent |
| Section index links | Custom anchor list; Primer density as reference only |
| Entry rows | README-only under this contract; mono year already in entry titles |
| Tags/chips | Custom neutral chips (surface-1, border, mono 12.8px) |
| Disclosure | Native `<details>` only for optional secondary copy; section bodies stay open by default |
| Icons | none; text and CSS only for this surface |

Registry order respected: reuse family landing HTML first; no component library on this surface.

## Motion

- Philosophy: state change only; motion is felt, not featured  
- Duration **120-200ms**, easing ease-out  
- Properties: opacity and 4-8px translate only  
- Hover: colour/underline on links; no scale, no parallax, no bounce  
- `@media (prefers-reduced-motion: reduce)` disables animation and transition

## Imagery

- No stock photography. No abstract AI gradients  
- Typography + list only; the Awesome badge is the sole decorative element in the hero  
- Open Graph: title + description; no social image for this surface

## Responsive Behaviour

- **Desktop (>=1024px):** two-column section index  
- **Tablet:** single column; nav wraps  
- **Mobile (390px target):** stacked hero, full-width CTA (>=44px tall), section anchors as stacked list, no horizontal overflow, body still >=16px

## Accessibility

- Body text and muted text meet WCAG AA on bg/surfaces  
- Visible `:focus-visible` ring using accent (2px, offset 2px) on every interactive control  
- Keyboard: all nav anchors, CTAs, and issue links operable  
- Touch targets >=44px on primary actions and nav links  
- `lang="en"`; semantic landmarks (`nav`, `main`, `footer`); heading order h1 -> h2  
- Reduced motion respected as above

## Component Sources

1. Family landing HTML from awesome-archimate (`docs/index.html`), tokens unchanged  
2. No shadcn or marketing kits on this list product  
3. Custom last for any entry-row mirroring under a future contract

## Anti-patterns

From the family contract plus project rules:

- Centred indigo/violet gradient hero  
- Inter/Roboto as the only font  
- Three identical feature cards  
- Glassmorphism and glow  
- Oversized radii outside 3/5/7  
- Generic "transform your workflow" copy  
- Rainbow tags; emoji in chrome  
- CDN font hotlink  
- Dark shell on this light long-read brief  
- Maintainer chrome leaking to visitors (classification banners, doc IDs, revision counters)

## Reference Sites

1. https://vercel.com: mono metadata, contrast, one CTA per viewport  
2. https://primer.style: dense functional hierarchy for chips and lists  
3. https://linear.app: type weight hierarchy and short motion (light adaptation only)

## Quality Bar

Must feel like a careful technical index from a competent maintainer.  
Must not feel like: a default Tailwind marketing page, an AI template, a generic dashboard theme, or a SaaS launch landing.

**Pilot composition order:** nav -> hero (claim + one primary CTA) -> evidence strip (version, last sweep, entry count, text-only family pointer) -> section index (primary) -> short curation note -> contribute links -> footer (CC0, licence enquiry, maintainer).

**Implementation note (not style):** Path S static `docs/` with self-hosted Plex is the first build; Path N Next export is deferred until a spoke needs app components. Superpowers process owns implementation.

**Provenance:** derived from the awesome-archimate DESIGN.md / DESIGN_BRIEF.md family contract (2026-09-18), which was itself derived from the minimal-technical style corpus (styles/minimal-technical/STYLE.md, patterns/progressive-disclosure.md, patterns/homepage-composition.md, references/vercel.md, references/primer.md, references/linear.md, anti-patterns/generic-ai-ui.md). Tokens reused unchanged per the family constraint: no second design system.
