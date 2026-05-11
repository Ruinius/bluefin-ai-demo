# Part 2: Narrative Prologue — Sections 0.0–2

> **Prerequisite:** Part 1 (foundation) must be complete. The scroll engine and section containers must exist.

## Objective

Implement the opening narrative that sets up the problem before the product appears. These are full-screen, text-only sections with scroll-driven fade animations.

## Sections

### Section 0.0 — Instructions (`section-instructions`, 100vh)

- **Content:** Centered text: "This is a zero-dependency HTML presentation. Scroll down to proceed."
  - Below the scroll arrow, a smaller caption: "Built with [github.com/Ruinius/bluefin-ai-demo](https://github.com/Ruinius/bluefin-ai-demo). If you liked this presentation, please let me know by giving a star."
  - The link must be a real `<a>` tag with `target="_blank"` and `pointer-events: auto` so it is clickable
- **Animation:** A simple, subtle animated arrow or mouse icon below the text, indicating "scroll down"
- **Behavior:**
  - Fades in on page load (not scroll-dependent)
  - Fades out as user begins scrolling (progress 0.0 → 0.3)

### Section 0 — Opening Statement (`section-opening`, 100vh)

- **Content:** Centered text (Hero/Narrative size — 48px, weight 600):

  > AI-native engineers have: Jules, Codex, Claude Code, OpenHands, and a dozen powerful tools.

- **Animation:**
  - Fades in as progress reaches ~0.2
  - Fully visible at progress ~0.5
  - Fades out as progress approaches 1.0

### Section 1 — The Problem (`section-problem`, 150vh)

- **Content:** Centered text block (Hero/Narrative size):

  > AI-native business folks are saying:
  >
  > "What is a markdown? I need a Google Docs or at least a DOCX."
  >
  > "I just spent two hours trying to set up a MCP server for Databricks. What is MCP?"
  >
  > "Holy crap, running Claude for an hour on my presentation cost $150."

- **Animation:**
  - The header "AI-native business folks are saying:" fades in first
  - Each quote fades in with a **stagger** (e.g., each starts ~0.15 progress later than the previous)
  - All fade out together as progress approaches 1.0

### Section 2 — Transition to Product (`section-transition`, 80vh)

- **Content:** No new text
- **Animation:**
  - Any remaining text fades out
  - The background transitions from full-screen to reveal the product chrome (sidebar appears — this is a cue for Part 3)
  - This section acts as a "bridge" — by the end of its scroll, the sidebar should be visible

## Styling Reference

- Text color: `var(--text-primary)` for main text
- Background: `var(--bg-primary)` or `var(--gradient-subtle)` for a very subtle gradient
- Text should be centered both horizontally and vertically in the viewport
- Use `position: sticky; top: 0;` or `position: fixed` patterns so text stays centered while scrolling controls opacity
- Font: Hero/Narrative level from style guide (48px, weight 600, line-height 1.2, letter-spacing -0.02em)
- Quotes can use a slightly smaller size (e.g., Body or H2) with italic styling for contrast

## What NOT to Build

- Do NOT build the sidebar — that's Part 3
- Do NOT add any product UI — only the narrative text
