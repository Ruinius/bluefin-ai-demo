# Part 1: Foundation — HTML Skeleton & Scroll Engine

> **Prerequisite:** Read `docs/style_guide.md` for all CSS variable definitions, typography, and spacing tokens.

## Objective

Build the base HTML file with:
- All CSS custom properties (from style guide)
- The scroll-driven animation engine
- The empty section containers that later parts will populate

## Deliverables

A single `index.html` file containing:

1. **HTML boilerplate** with `<style>` and `<script>` blocks (all inline, zero external dependencies)
2. **CSS custom properties** — all tokens from `docs/style_guide.md` Section 1–5 (colors, typography, spacing, borders, shadows)
3. **Font stack** — system font stack as defined in style guide Section 2
4. **Text rendering** — antialiased, optimizeLegibility
5. **Global styles** — `html, body` at 100% height, no default margin/padding, background `var(--bg-primary)`
6. **Section containers** — one `<div>` per scroll section, each with a unique ID and a CSS height matching the scroll section heights from `docs/style_guide.md` Section 7:

| Section ID | Scroll Height |
|------------|---------------|
| `section-instructions` | 100vh |
| `section-opening` | 100vh |
| `section-problem` | 150vh |
| `section-transition` | 80vh |
| `section-welcome` | 100vh |
| `section-dashboard` | 100vh |
| `section-click-research` | 80vh |
| `section-workspace` | 100vh |
| `section-model-select` | 120vh |
| `section-edit-execute` | 150vh |
| `section-workspace-tab` | 120vh |
| `section-preview-tab` | 150vh |
| `section-closing-1` | 100vh |
| `section-closing-2` | 100vh |
| `section-closing-3` | 100vh |

7. **Scroll engine (JavaScript)** — a `scroll` event listener on `window` that:
   - Determines which section is currently in view
   - Calculates a `progress` value (0.0 → 1.0) for each section based on how far the user has scrolled through it
   - Exposes a function like `getProgress(sectionId)` that other parts can call
   - All animations must be **reversible** — scrolling up plays them backwards

8. **Customization variable** at the top of `<script>`:
   ```js
   const recipientName = "Sarah";
   ```

## Technical Constraints

- Zero external dependencies — no CDN links, no external CSS/JS files
- All CSS in `<style>` tags, all JS in `<script>` tags
- System font stack only (no Google Fonts download)
- All icons will be inline SVGs (added in later parts)

## Easing Curves (from style guide)

Make these available as CSS variables or JS constants:
| Name | Value |
|------|-------|
| Standard | `cubic-bezier(0.4, 0, 0.2, 1)` |
| Decelerate | `cubic-bezier(0, 0, 0.2, 1)` |
| Accelerate | `cubic-bezier(0.4, 0, 1, 1)` |

## What NOT to Build

- Do NOT add any visible content (text, icons, UI components) — those come in Parts 2–7
- Do NOT add the animated cursor — that comes in Part 4
- Only build the skeleton and the scroll calculation engine
