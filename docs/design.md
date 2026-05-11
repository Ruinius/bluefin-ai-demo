# Design Document: Bluefin — Zero-Dependency HTML Demo

## Product Identity

**Name:** Bluefin

**Dual meaning:**

1. **Bluefin tuna is delicious sushi** — playful, approachable, enjoyable.
2. **Bluefin tuna is an apex predator** — powerful, fast, dominant.

This duality reflects the product positioning: a tool that feels effortless and delightful to use, yet is ruthlessly effective under the hood.

## Project Overview

This project is a zero-dependency HTML demo of the Bluefin application, designed to be easily shareable with friends and investors for quick reactions. The entire experience is a single HTML file that tells a narrative through scroll-driven animations, then demonstrates the core product interaction.

## Design Philosophy

- **Premium consumer feel**: Styling should evoke Apple or Tesla — clean, confident, spacious.
- **Light and approachable**: A light base color scheme that does not intimidate business users.
- **Showcase presentation**: The product UI appears as a centered window (slightly smaller than a laptop screen) floating on a dark backdrop — like a product being showcased on stage.
- **Scroll is the only input**: Every transition is controlled by scrolling down (advance) or scrolling up (reverse). No click interactions are required from the viewer — all "clicks" within the product demo are animated.
- **Visual bookending**: The narrative opens on a light background, transitions to a dark backdrop for the product showcase, then returns to light for the closing messages.

---

## Color Palette & Styling

See `docs/style_guide.md` for the full style specification.

**Summary:**

- Light background (off-white / warm white)
- Accent gradient: light blue → dark blue → violet (ocean / Bluefin theme)
- Typography: Premium sans-serif (e.g., SF Pro Display style via system fonts, or Inter/Outfit from Google Fonts — inlined as base64 to maintain zero-dependency)
- Rounded corners, generous whitespace, subtle shadows
- Micro-animations on every transition

---

## Implementation Sections

The demo is divided into 7 coding parts, designed to be implemented sequentially. Each part builds on the previous one and has its own detailed spec:

| Part | File | Sections Covered | Summary |
|------|------|-----------------|---------|
| 1 | [01_foundation.md](sections/01_foundation.md) | — | HTML skeleton, CSS variables, scroll engine |
| 2 | [02_prologue.md](sections/02_prologue.md) | 0.0–2 | Narrative text animations (problem setup) |
| 3 | [03_sidebar_welcome.md](sections/03_sidebar_welcome.md) | 2–3 | Persistent sidebar, welcome screen |
| 4 | [04_dashboard_cursor.md](sections/04_dashboard_cursor.md) | 4–5 | Dashboard UI, animated cursor click |
| 5 | [05_workspace_model.md](sections/05_workspace_model.md) | 6–7 | Research workspace layout, model selector |
| 6 | [06_execution_preview.md](sections/06_execution_preview.md) | 8–10 | Plan editing, file tree, Google Docs preview |
| 7 | [07_epilogue.md](sections/07_epilogue.md) | 11–13 | Closing messages |

### Dependency Chain

```
Part 1 → Part 2 → Part 3 → Part 4 → Part 5 → Part 6 → Part 7
```

Each part assumes all previous parts are complete. The scroll engine (Part 1) and the animated cursor (introduced in Part 4) are shared infrastructure used across multiple parts.

---

## User Experience / Flow

The entire demo is a continuous vertical scroll. Each "section" occupies enough scroll height to control its animations. Scrolling down advances the narrative; scrolling up reverses it.

### Narrative Prologue (Sections 0.0–2)
→ See [Part 2: Prologue](sections/02_prologue.md)

These set up the problem before showing the product.

- **Section 0.0** — Instructions: scroll-down prompt
- **Section 0** — Opening: "AI-native engineers have powerful tools..."
- **Section 1** — The Problem: three quotes from business users
- **Section 2** — Transition: background darkens, product frame appears

### Product Demo (Sections 3–10)
→ See Parts [3](sections/03_sidebar_welcome.md), [4](sections/04_dashboard_cursor.md), [5](sections/05_workspace_model.md), [6](sections/06_execution_preview.md)

From this point, the **product frame** — a centered, rounded-corner window on a dark backdrop — is visible. All product UI lives inside this frame.

#### Persistent Left Sidebar
→ See [Part 3: Sidebar](sections/03_sidebar_welcome.md)

A thin vertical band on the left side **inside the product frame** containing (top to bottom):

- **Bluefin logo** (top)
- **User avatar** — small circular profile picture
- **Settings icon** — gear/cog widget
- **Exit button** — bottom of sidebar

#### Section 3 — Welcome Screen
→ See [Part 3](sections/03_sidebar_welcome.md)

> **Welcome back, [Name]**

`[Name]` is a customizable variable (`const recipientName = "Sarah";`).

#### Section 4 — Dashboard
→ See [Part 4](sections/04_dashboard_cursor.md)

- Top: "Your workspaces" with search bar and two workspace cards
- Bottom: "Start a new workspace" with template cards (Blank, Research, Docs, Slides)

#### Section 5 — Animated Click: Select "Research"
→ See [Part 4](sections/04_dashboard_cursor.md)

Animated cursor clicks the "Research" card, transitioning to workspace.

#### Section 6 — Research Workspace
→ See [Part 5](sections/05_workspace_model.md)

Left panel: AI Agent (model selector, pause, chat area)
Right panel: Tabs (Plan | Workspace | Preview), Plan tab active with structured steps.

#### Section 7 — Model Selector
→ See [Part 5](sections/05_workspace_model.md)

Cursor clicks model selector, dropdown shows models with cost ($) and rating (★):

**Models listed:**
| Model | Cost | User Rating
|-------|-----------------|-----|
| Claude Opus 4.7 | $$$$$ | ★★★★★
| Claude Sonnet 4.6 | $$$$ | ★★★★
| GPT-5.5 | $$$$$ | ★★★★★
| GPT-5.3-Codex | $$$$ | ★★★★
| Gemini 3.1 Pro | $$$$ | ★★★★
| GLM-5.1 | $$$ | ★★★
| Deepseek-4 | $$$ | ★★★
| Kimi K2.6 | $$ | ★★
| MiniMax M2.7 | $ | ★★

Cursor selects **MiniMax M2.7**.

#### Section 8 — Editing & Execution
→ See [Part 6](sections/06_execution_preview.md)

1. Cursor edits "Final Output" to add Google Drive path
2. Types "execute for the US snacks industry in 2026"
3. Agent starts working with status messages

#### Section 9 — Workspace Tab
→ See [Part 6](sections/06_execution_preview.md)

Cursor clicks Workspace tab. File tree populates with 10 research PDFs.

#### Section 10 — Preview Tab
→ See [Part 6](sections/06_execution_preview.md)

Cursor clicks Preview tab. Google Docs-style document is written live by the agent.

### Closing Epilogue (Sections 11–13)
→ See [Part 7: Epilogue](sections/07_epilogue.md)

The product frame fades out, the dark backdrop transitions back to the light background, and three closing messages appear:

1. **"A business-first AI agent"**
2. **"Cost conscious with the right AI model for every task"**
3. **"On-prem and hyper-secure deployments available"**

---

## Technical Constraints

- The final deliverable must be a single, zero-dependency HTML file (no external CSS or JS libraries, everything inline or within `<style>`/`<script>` tags).
- All interactions (scroll, fade, animations) must be implemented with vanilla JavaScript and CSS.
- The `[Name]` variable must be easily editable at the top of the `<script>` section.
- Google Fonts may be embedded as base64-encoded `@font-face` declarations, or system font stacks may be used to maintain zero-dependency status.
- All icons/logos should be inline SVGs.

## Customization Points

| Variable        | Location          | Purpose                             |
| --------------- | ----------------- | ----------------------------------- |
| `recipientName` | Top of `<script>` | Personalizes "Welcome back, [Name]" |
| Workspace names | Config object     | Past workspace card titles          |
| Plan steps      | Config object     | Pre-populated plan content          |
