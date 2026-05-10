# Part 3: Sidebar & Welcome Screen — Section 3

> **Prerequisite:** Parts 1–2 must be complete. The scroll engine, section containers, and prologue must exist.

## Objective

Build the persistent left sidebar and the welcome screen that appears after the prologue fades out.

## Components

### Persistent Left Sidebar

A thin vertical band on the far left that **remains visible from Section 2 onward** (once the product UI appears, it never leaves).

**Specifications (from `docs/style_guide.md` Section 6):**
- Width: **56px** (thin, icon-only)
- Background: `var(--gradient-sidebar)` — `linear-gradient(180deg, #1A1F2E 0%, #0F172A 100%)`
- Position: fixed, left edge, full viewport height
- z-index: high enough to stay above content

**Contents (top to bottom):**

1. **Bluefin logo** (top)
   - 28px mark
   - Styled with ocean gradient or white
   - Inline SVG

2. **User avatar**
   - 32px circle
   - 2px white border
   - Can be a placeholder circle with initials or a generic silhouette

3. **Settings icon** (gear/cog)
   - 20px inline SVG, white
   - `opacity: 0.7` at rest → `1.0` on hover
   - Transition: `opacity 0.2s ease`

4. **Exit button** (at bottom of sidebar)
   - 20px inline SVG, white
   - `opacity: 0.7` → `1.0` on hover
   - Transition: `opacity 0.2s ease`

**Layout:**
- Items spaced with `var(--space-5)` (24px) between them
- Logo at top, avatar below, settings further down, exit pinned to bottom

**Sidebar entrance animation:**
- During Section 2 (transition), the sidebar slides in from the left (translateX(-56px) → translateX(0))
- Synchronized with Section 2's scroll progress

### Section 3 — Welcome Screen (`section-welcome`, 100vh)

**Content:**
The entire main area (right of sidebar, i.e., `margin-left: 56px`) shows a single centered message:

> **Welcome back, [Name]**

Where `[Name]` is replaced by the `recipientName` variable defined in Part 1.

**Styling:**
- Font: Hero/Narrative size (48px, weight 600)
- Color: `var(--text-primary)`
- Centered horizontally and vertically in the main area

**Animation:**
- Fades in as Section 3 progress goes from 0.0 → 0.3
- Holds at full opacity from ~0.3 → 0.7
- Fades out as progress goes from 0.7 → 1.0

## Inline SVG Icons Needed

All icons must be inline SVGs (no external files):

| Icon | Size | Notes |
|------|------|-------|
| Bluefin logo mark | 28px | Custom — can be a stylized "B" or fish fin shape |
| Settings (gear) | 20px | Line icon style |
| Exit / logout | 20px | Line icon style (door with arrow, or power symbol) |

## What NOT to Build

- Do NOT build the dashboard — that's Part 4
- Do NOT add the animated cursor — that's Part 4
- The sidebar has no click interactivity — it is purely visual
