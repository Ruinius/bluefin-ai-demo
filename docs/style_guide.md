# Bluefin — Style Guide

This document defines the visual language for the Bluefin demo. Every element should feel premium, clean, and confident — inspired by Apple and Tesla product pages.

---

## 1. Color Palette

### Base Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-primary` | `#FAFBFD` | Page background — warm off-white |
| `--bg-secondary` | `#F0F2F5` | Card backgrounds, input fields |
| `--bg-sidebar` | `#1A1F2E` | Left sidebar — dark navy |
| `--text-primary` | `#1A1A2E` | Headings, primary text |
| `--text-secondary` | `#6B7280` | Descriptions, timestamps, muted text |
| `--text-inverse` | `#FFFFFF` | Text on dark backgrounds |
| `--border` | `#E5E7EB` | Subtle borders, dividers |

### Accent / Ocean Gradient
| Token | Hex | Usage |
|-------|-----|-------|
| `--blue-light` | `#60A5FA` | Light blue — highlights, hover states |
| `--blue-mid` | `#3B82F6` | Mid blue — primary buttons, active states |
| `--blue-dark` | `#1E40AF` | Dark blue — emphasis, headings |
| `--violet` | `#7C3AED` | Violet accent — special highlights, tags |
| `--violet-light` | `#A78BFA` | Light violet — secondary accents |

### Gradient Definitions
```css
/* Primary brand gradient — used sparingly for key CTAs and the logo mark */
--gradient-ocean: linear-gradient(135deg, #60A5FA 0%, #3B82F6 40%, #7C3AED 100%);

/* Subtle background gradient — for hero sections or large containers */
--gradient-subtle: linear-gradient(180deg, #FAFBFD 0%, #EEF2FF 100%);

/* Sidebar gradient */
--gradient-sidebar: linear-gradient(180deg, #1A1F2E 0%, #0F172A 100%);
```

### Semantic Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--success` | `#10B981` | Completed states, check marks |
| `--warning` | `#F59E0B` | Cost indicators ($$) |
| `--cursor-blue` | `#3B82F6` | Animated cursor circle |

---

## 2. Typography

### Font Stack
Use the system font stack for premium feel without external dependencies:
```css
--font-primary: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', 'Inter', Roboto, Helvetica, Arial, sans-serif;
--font-mono: 'SF Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
```

> **Note:** If we decide to embed Inter or Outfit from Google Fonts as base64, this will be done inline within `<style>` tags to preserve zero-dependency status.

### Type Scale
| Level | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|--------|-------------|----------------|-------|
| Hero / Narrative | 48px | 600 | 1.2 | -0.02em | Prologue & epilogue messages |
| H1 | 32px | 600 | 1.3 | -0.01em | Page titles ("Your workspaces") |
| H2 | 24px | 600 | 1.35 | -0.005em | Section headers |
| H3 | 18px | 500 | 1.4 | 0 | Card titles, tab labels |
| Body | 15px | 400 | 1.6 | 0 | Paragraph text, descriptions |
| Caption | 13px | 400 | 1.5 | 0.01em | Timestamps, small labels |
| Mono | 13px | 400 | 1.5 | 0 | File names, code, YAML |

### Text Rendering
```css
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
text-rendering: optimizeLegibility;
```

---

## 3. Spacing System

Use an 8px base grid. All spacing should be multiples of 4 or 8.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight gaps (icon-to-text) |
| `--space-2` | 8px | Small internal padding |
| `--space-3` | 12px | Compact padding |
| `--space-4` | 16px | Standard padding |
| `--space-5` | 24px | Section gaps |
| `--space-6` | 32px | Large gaps |
| `--space-7` | 48px | Section separators |
| `--space-8` | 64px | Major layout gaps |

---

## 4. Borders & Corners

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 8px | Small elements (buttons, inputs, tags) |
| `--radius-md` | 12px | Cards, modals |
| `--radius-lg` | 16px | Large cards, panels |
| `--radius-xl` | 24px | Hero elements |
| `--radius-full` | 9999px | Circular (avatars, cursor dot) |

Border style:
```css
border: 1px solid var(--border);
```

---

## 5. Shadows & Elevation

Three levels of elevation to create depth hierarchy:

| Level | CSS | Usage |
|-------|-----|-------|
| Low | `0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06)` | Cards at rest |
| Medium | `0 4px 12px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.04)` | Hovered cards, dropdowns |
| High | `0 12px 40px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04)` | Modals, focused elements |

---

## 6. Component Specifications

### Left Sidebar
- Width: **56px** (thin, icon-only)
- Background: `var(--gradient-sidebar)`
- Icons: **20px**, white, `opacity: 0.7` → `1.0` on hover
- Logo: top, 28px mark
- Avatar: 32px circle, 2px white border
- Spacing between items: `var(--space-5)`
- Transition: `opacity 0.2s ease`

### Cards (Workspace cards, Template cards)
- Background: `var(--bg-primary)` or `white`
- Border: `1px solid var(--border)`
- Border-radius: `var(--radius-md)`
- Padding: `var(--space-4)` to `var(--space-5)`
- Shadow: Low elevation at rest → Medium on hover
- Hover: slight `translateY(-2px)` lift, shadow increase
- Transition: `all 0.25s cubic-bezier(0.4, 0, 0.2, 1)`

### Template Cards (Start a new workspace)
- Fixed width: ~160px
- Fixed height: ~180px
- Icon: centered, 40px, colored with accent gradient
- Label: below icon, `H3` weight
- Horizontal scroll container with `gap: var(--space-4)`

### Buttons
- Primary: `var(--gradient-ocean)` background, white text, `var(--radius-sm)`
- Secondary: transparent, `var(--blue-mid)` text, `1px solid var(--blue-mid)`
- Ghost: transparent, `var(--text-secondary)` text
- All: `padding: 10px 20px`, `font-weight: 500`, `font-size: 14px`
- Hover: subtle brightness increase or shadow
- Transition: `all 0.2s ease`

### Search Bar
- Background: `var(--bg-secondary)`
- Border: `1px solid var(--border)` → `var(--blue-mid)` on focus
- Border-radius: `var(--radius-sm)`
- Padding: `10px 16px`
- Placeholder text: `var(--text-secondary)`
- Search icon (magnifying glass SVG) inside, left-aligned

### Tabs (Plan | Workspace | Preview)
- Style: underline tabs
- Inactive: `var(--text-secondary)`, no underline
- Active: `var(--blue-dark)`, 2px bottom border in `var(--blue-mid)`
- Transition: color and border `0.2s ease`
- Font: `H3` size, `weight 500`

### Model Selector Dropdown
- Trigger: styled like a select box with current model name + chevron
- Dropdown: white bg, `var(--radius-md)`, High shadow
- Each row: model name, cost indicator (e.g., $$$), and user rating (e.g., ★★★★★)
- Hover: `var(--bg-secondary)` background
- Selected: checkmark icon + `var(--blue-light)` background tint

### Animated Cursor
- Circle: 32px diameter, `var(--cursor-blue)`, `opacity: 0.6`
- Inner dot: 8px, `var(--cursor-blue)`, `opacity: 1.0`
- Click animation: scale down to 0.7 then back to 1.0 over 200ms
- Movement: `cubic-bezier(0.4, 0, 0.2, 1)` easing
- Trail: subtle opacity afterimage (optional)

### File Tree (Workspace tab)
- Monospace font: `var(--font-mono)`
- Folder icons: 📁 emoji or inline SVG
- File icons: 📄 emoji or inline SVG
- Indentation: 20px per level
- New file animation: slide in from left + fade in, 300ms
- "Being edited" indicator: small pulsing dot (green `var(--success)`)

### Google Docs Preview
- White page centered in the panel with subtle shadow (High elevation)
- Simplified toolbar bar at top (gray, with minimal formatting icons)
- Page title in large text
- Body text appearing character-by-character or line-by-line
- Blue cursor line visible (Google Docs style blinking cursor)

---

## 7. Animation & Timing Guidelines

### Scroll-Driven Animations
- Each "section" in the scroll has a defined scroll range (e.g., 100vh per section)
- Animations are calculated as a progress value (0.0 → 1.0) based on scroll position
- All animations must be **reversible** — scrolling up plays them backwards

### Easing Curves
| Name | Value | Usage |
|------|-------|-------|
| Standard | `cubic-bezier(0.4, 0, 0.2, 1)` | Most transitions |
| Decelerate | `cubic-bezier(0, 0, 0.2, 1)` | Elements entering view |
| Accelerate | `cubic-bezier(0.4, 0, 1, 1)` | Elements leaving view |

### Duration Guidelines
| Animation Type | Duration | Notes |
|----------------|----------|-------|
| Fade in/out | 400–600ms | Narrative text |
| Card hover | 250ms | Quick feedback |
| Cursor movement | 600–800ms | Smooth, natural feel |
| Cursor click | 200ms | Snappy |
| Tab switch | 300ms | Content crossfade |
| File appearing | 300ms | Slide + fade |
| Text typing | 40–60ms/char | Natural typing speed |
| Dropdown open | 200ms | Scale + fade |

### Scroll Section Heights
Each section needs enough scroll distance for its animations to feel unhurried:
| Section | Scroll Height | Content |
|---------|---------------|---------|
| 0.0 — Instructions | 100vh | Zero-dependency notice & scroll prompt |
| 0 — Opening | 100vh | Opening statement |
| 1 — Problem | 150vh | Three quotes with stagger |
| 2 — Transition | 80vh | Fade to product |
| 3 — Welcome | 100vh | Welcome message |
| 4 — Dashboard | 100vh | Dashboard layout |
| 5 — Click Research | 80vh | Cursor animation |
| 6 — Workspace | 100vh | Layout appears |
| 7 — Model select | 120vh | Dropdown + selection |
| 8 — Edit & execute | 150vh | Multiple edits + typing |
| 9 — Workspace tab | 120vh | Files populating |
| 10 — Preview tab | 150vh | Google Docs being written |
| 11–13 — Closing | 100vh each | Three closing messages |

**Total estimated scroll:** ~1,550vh

---

## 8. Inline SVG Icons Needed

All icons must be inline SVGs to maintain zero-dependency status.

| Icon | Usage | Style |
|------|-------|-------|
| Bluefin logo | Sidebar top | Custom mark, ocean gradient |
| Settings (gear) | Sidebar | Line icon, 20px |
| Exit / logout | Sidebar bottom | Line icon, 20px |
| Search (magnifying glass) | Search bar | Line icon, 16px |
| Blank workspace | Template card | Minimal, line style |
| Research (magnifying glass + doc) | Template card | Line/filled hybrid |
| Google Docs logo | Template card | Simplified inline SVG |
| Google Slides logo | Template card | Simplified inline SVG |
| Pause | AI agent panel | Filled circle with bars |
| Chevron down | Model selector | Small, line style |
| Checkmark | Selected model | Line icon |
| Folder | File tree | Filled, subtle color |
| File | File tree | Line icon |
| Pulsing dot | "Editing" indicator | Animated circle |
