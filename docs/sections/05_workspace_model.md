# Part 5: Research Workspace & Model Selector — Sections 6–7

> **Prerequisite:** Parts 1–4 must be complete. Sidebar, dashboard, and animated cursor must exist.

## Objective

Build the Research workspace layout (the main working view of the app) and the animated model selector dropdown interaction.

## Components

### Section 6 — Research Workspace Layout (`section-workspace`, 100vh)

The main area (right of sidebar) splits into **left and right halves**.

**Left Half — AI Agent Panel**

- Approximately 35–40% of the main area width
- Background: slightly different shade or same `var(--bg-primary)` with a right border (`1px solid var(--border)`)

Contents (top to bottom):

1. **Model selector** at the top
   - Styled like a select/dropdown trigger
   - Shows currently selected model name + chevron-down icon
   - Default text: **"MiniMax M2.7"**
   - Styling: `var(--bg-secondary)` background, `var(--radius-sm)` corners, `padding: 10px 16px`
   - The dropdown itself is built in Section 7 (below)

2. **Pause button**
   - Circular pause icon (filled circle with two vertical bars)
   - Below or beside the model selector
   - Not interactive — just visual

3. **Chat/status area**
   - Takes remaining vertical space
   - Initially empty or shows a subtle "Ready" state
   - This area will be animated in Part 6

**Right Half — Work Area with Tabs**

- Approximately 60–65% of the main area width

**Tab bar at top:**
- Three tabs: **Plan** | **Workspace** | **Preview**
- Tab styling (from style guide):
  - Style: underline tabs
  - Inactive: `var(--text-secondary)`, no underline
  - Active: `var(--blue-dark)`, 2px bottom border in `var(--blue-mid)`
  - Transition: color and border `0.2s ease`
  - Font: H3 size (18px), weight 500
- **Plan** tab is active by default

**Plan Tab Content:**

A structured plan document displayed in the work area:

- **"Overall Instructions"** — section header (H2, 24px, weight 600)
- **Step 1:** Collect and analyze market data from industry databases and analyst reports
- **Step 2:** Identify key players, market trends, and competitive dynamics
- **Step 3:** Synthesize findings into an executive summary with charts and data tables
- **Final Output:** Google Doc

Each step should be styled as a clean list item with step number bolded. Use Body text size (15px). Add comfortable spacing between steps.

**Workspace entrance animation:**
- The layout slides/fades in as Section 6 progress goes from 0.0 → 0.4
- Left and right panels may stagger slightly

---

### Section 7 — Animated Model Selector (`section-model-select`, 120vh)

**Animation sequence (driven by scroll progress):**

1. **Progress 0.0–0.2:** Cursor (from Part 4) moves to the model selector trigger
2. **Progress 0.2–0.3:** Cursor clicks — model selector trigger gets pressed state
3. **Progress 0.3–0.5:** Dropdown opens with animation:
   - Scale from 0.95 → 1.0 + fade in, 200ms feel
   - Dropdown styling (from style guide):
     - White background
     - Border-radius: `var(--radius-md)` (12px)
     - Shadow: High elevation
     - Appears below the model selector trigger

4. **Progress 0.3–0.5:** Dropdown content visible — list of models:

   Each row shows:
   - Model name (left-aligned)
   - Cost indicator (dollar signs, right-aligned)
   - User rating (stars, right-aligned)

   **Models listed:**

   | Model | Cost | User Rating |
   |-------|------|-------------|
   | Claude Opus 4.7 | $$$$$ | ★★★★★ |
   | Claude Sonnet 4.6 | $$$$ | ★★★★ |
   | GPT-5.5 | $$$$$ | ★★★★★ |
   | GPT-5.3-Codex | $$$$ | ★★★★ |
   | Gemini 3.1 Pro | $$$$ | ★★★★ |
   | GLM-5.1 | $$$ | ★★★ |
   | Deepseek-4 | $$$ | ★★★ |
   | Kimi K2.6 | $$ | ★★ |
   | MiniMax M2.7 | $ | ★★ |

   - Row hover: `var(--bg-secondary)` background
   - MiniMax M2.7 should have a checkmark icon + `var(--blue-light)` background tint (currently selected)

5. **Progress 0.5–0.7:** Cursor moves down the list to **MiniMax M2.7** (already selected, cursor just confirms)
6. **Progress 0.7–0.8:** Cursor clicks on MiniMax M2.7 — row gets highlight flash
7. **Progress 0.8–1.0:** Dropdown closes (reverse of open animation), model selector trigger still shows "MiniMax M2.7"

## Inline SVG Icons Needed

| Icon | Size | Usage |
|------|------|-------|
| Chevron down | 12–16px | Model selector trigger |
| Checkmark | 16px | Selected model indicator |
| Pause | 24px | Pause button (filled circle with bars) |

## What NOT to Build

- Do NOT build the Workspace or Preview tab content — those come in Part 6
- The Plan tab content should be static at this point (editing animations come in Part 6)
- Chat/status area remains empty — Part 6 will animate it
