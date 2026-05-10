# Part 4: Dashboard & Cursor Click — Sections 4–5

> **Prerequisite:** Parts 1–3 must be complete. Sidebar, scroll engine, and welcome screen must exist.

## Objective

Build the dashboard page (the main app screen the user sees after welcome) and the animated cursor that clicks the "Research" template card.

## Components

### Section 4 — Dashboard (`section-dashboard`, 100vh)

The main area (right of sidebar) splits into **top and bottom halves**.

**Top Half — "Your workspaces"**

- **Title:** "Your workspaces" (H1 — 32px, weight 600)
- **Search bar** (styled, non-functional):
  - Background: `var(--bg-secondary)`
  - Border: `1px solid var(--border)`
  - Border-radius: `var(--radius-sm)` (8px)
  - Padding: `10px 16px`
  - Placeholder text: "Search workspaces..." in `var(--text-secondary)`
  - Magnifying glass SVG icon inside, left-aligned (16px, line icon)
- **Two workspace cards** side by side:
  - **Card 1:** "Q1 Market Analysis" — last edited: "2 days ago"
  - **Card 2:** "Board Deck Draft" — last edited: "1 week ago"
  - Card styling (from style guide):
    - Background: `var(--bg-primary)` or `white`
    - Border: `1px solid var(--border)`
    - Border-radius: `var(--radius-md)` (12px)
    - Padding: `var(--space-4)` to `var(--space-5)` (16–24px)
    - Shadow: Low elevation at rest
    - Each card has a title (H3 — 18px, weight 500), an optional subtle icon/color accent, and a timestamp (Caption — 13px, `var(--text-secondary)`)

**Bottom Half — "Start a new workspace"**

- **Title:** "Start a new workspace" (H1 — 32px, weight 600)
- **Horizontally-scrolling row** of template cards:
  1. **Blank workspace** — minimal icon, neutral styling
  2. **Research** — magnifying glass + document icon
  3. **Docs** — Google Docs logo (simplified inline SVG)
  4. **Slides** — Google Slides logo (simplified inline SVG)

- Template card styling (from style guide):
  - Fixed width: ~160px
  - Fixed height: ~180px
  - Icon: centered, 40px, colored with accent gradient
  - Label: below icon, H3 weight (18px, 500)
  - Container: horizontal scroll with `gap: var(--space-4)` (16px)
  - Border-radius: `var(--radius-md)` (12px)
  - Border: `1px solid var(--border)`
  - The row should imply more cards exist to the right (subtle overflow indicator or partial card visible)

**Dashboard entrance animation:**
- The whole dashboard layout fades in / slides up slightly as Section 4 progress goes from 0.0 → 0.3
- Cards may stagger in slightly

---

### Section 5 — Animated Cursor Click (`section-click-research`, 80vh)

**The Animated Cursor:**

This is the first appearance of the animated cursor. It will be reused in later parts.

Cursor specifications (from style guide):
- **Outer circle:** 32px diameter, `var(--cursor-blue)` (#3B82F6), `opacity: 0.6`
- **Inner dot:** 8px, `var(--cursor-blue)`, `opacity: 1.0`
- **Movement easing:** `cubic-bezier(0.4, 0, 0.2, 1)`
- **Click animation:** scale down to 0.7 then back to 1.0 over 200ms
- **Trail:** subtle opacity afterimage (optional)

**Animation sequence (driven by scroll progress):**

1. Progress 0.0–0.3: Cursor fades in at an arbitrary starting position
2. Progress 0.3–0.6: Cursor smoothly moves toward the "Research" template card
3. Progress 0.6–0.7: Cursor "clicks" — shrinks briefly, the Research card gets a pressed/highlight state (e.g., subtle scale down, border color change to `var(--blue-mid)`)
4. Progress 0.7–1.0: Dashboard transitions out — the dashboard fades/slides away to make room for the Research workspace (built in Part 5)

## Inline SVG Icons Needed

| Icon | Size | Usage |
|------|------|-------|
| Search (magnifying glass) | 16px | Search bar, line style |
| Blank workspace | 40px | Template card, minimal line style |
| Research (magnifying glass + doc) | 40px | Template card, line/filled hybrid |
| Google Docs logo | 40px | Template card, simplified SVG |
| Google Slides logo | 40px | Template card, simplified SVG |

## What NOT to Build

- Do NOT build the Research workspace layout — that's Part 5
- The cursor component should be **reusable** — Parts 5 and 6 will move it to new positions
- Dashboard cards are NOT clickable by the user — only the animated cursor "clicks"
