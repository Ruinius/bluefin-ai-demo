# Part 6: Execution, File Tree & Preview — Sections 8–10

> **Prerequisite:** Parts 1–5 must be complete. The Research workspace with Plan tab, model selector, tabs, and cursor must all exist.

## Objective

Implement the most animation-heavy sections: the plan editing, command execution, file tree population, and Google Docs preview. These are the "wow" moments of the demo.

## Components

### Section 8 — Animated Editing & Execution (`section-edit-execute`, 150vh)

A sequence of animated interactions on the **Plan tab** (right panel) and the **AI Agent panel** (left panel).

**Animation sequence (driven by scroll progress):**

1. **Progress 0.0–0.3 — Edit Final Output:**
   - Cursor moves to the "Final Output: Google Doc" line in the plan
   - Cursor clicks, a text editing caret appears
   - Text is appended character by character: **" → Save to Google Drive /Projects/US-Snacks-2026/"**
   - Final line reads: "Final Output: Google Doc → Save to Google Drive /Projects/US-Snacks-2026/"
   - Typing speed: ~40–60ms per character (from style guide)

2. **Progress 0.3–0.5 — Type command:**
   - Cursor moves to a command/chat input area at the bottom of the plan area
   - Text is typed character by character:
     > "execute for the US snacks industry in 2026"
   - Same typing speed as above
   - Input area styling: similar to search bar — `var(--bg-secondary)`, `var(--radius-sm)`, subtle border

3. **Progress 0.5–0.7 — Agent starts working:**
   - The AI agent panel (left side) comes alive
   - A spinner or pulsing animation appears
   - Status messages appear sequentially in the chat area:
     - "Searching databases..."
     - "Reading analyst reports..."
     - "Analyzing market data..."
   - Each message fades in with slight delay
   - The pulse/spinner should feel alive and active

4. **Progress 0.7–1.0:** Agent continues working (activity carries into next sections)

---

### Section 9 — Workspace Tab: File Tree (`section-workspace-tab`, 120vh)

**Animation sequence (driven by scroll progress):**

1. **Progress 0.0–0.2:** Cursor moves to the **Workspace** tab and clicks it
   - Plan tab becomes inactive (text color changes, underline removed)
   - Workspace tab becomes active (blue text, 2px underline)
   - Tab transition: 300ms crossfade

2. **Progress 0.2–1.0:** File tree populates

**File tree structure:**

```
📁 Research: US Snacks 2026
├── 📁 input_metadata/
│   └── 📄 sources.yaml (being edited)
├── 📁 input/
│   ├── 📄 Morningstar_US_Snacks_Overview.pdf
│   ├── 📄 Campbell_Q4_2025_Earnings.pdf
│   ├── 📄 Mondelez_Investor_Presentation.pdf
│   ├── 📄 Euromonitor_Snack_Market_2026.pdf
│   ├── 📄 Hershey_Annual_Report_2025.pdf
│   ├── 📄 PepsiCo_Frito_Lay_Segment.pdf
│   ├── 📄 Nielsen_Snack_Trends_Q1_2026.pdf
│   ├── 📄 USDA_Food_Industry_Outlook.pdf
│   ├── 📄 General_Mills_Snack_Division.pdf
│   └── 📄 Kellanova_Post_Merger_Analysis.pdf
```

**File tree styling (from style guide):**
- Monospace font: `var(--font-mono)` (13px)
- Folder icons: 📁 emoji or inline SVG (filled, subtle color)
- File icons: 📄 emoji or inline SVG (line icon)
- Indentation: 20px per level

**File tree animation:**
- The root folder and `input_metadata/` appear first
- `sources.yaml` appears with a **pulsing green dot** (`var(--success)` — #10B981) indicating "being edited"
- The `input/` folder appears
- Files populate **one by one** with slide-in-from-left + fade-in animation (300ms each)
- Space files across the remaining scroll progress so they don't all appear at once

**Agent panel** (left side) continues showing activity throughout.

---

### Section 10 — Preview Tab: Google Docs (`section-preview-tab`, 150vh)

**Animation sequence (driven by scroll progress):**

1. **Progress 0.0–0.15:** Cursor moves to the **Preview** tab and clicks it
   - Workspace tab becomes inactive
   - Preview tab becomes active
   - Tab transition: 300ms crossfade

2. **Progress 0.15–1.0:** Google Docs preview appears and fills with content

**Google Docs preview styling (from style guide):**
- White page centered in the panel
- Shadow: High elevation (`0 12px 40px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04)`)
- Simplified toolbar bar at top (gray background, with minimal formatting icons — bold, italic, underline, alignment — all non-functional)
- Page has comfortable margins (~40px padding)

**Document content being "typed":**
- **Title:** "US Snacks Industry Analysis — 2026" (large text, Google Docs style H1)
- **Executive Summary** section header
  - 2–3 lines of body text appearing character-by-character or line-by-line
- **Market Size & Growth** section header
  - 2–3 lines of content
- **Key Players** section header
  - A few bullet points

- A blue cursor line should be visible (Google Docs-style blinking cursor) at the point where text is being "typed"
- Text typing speed: 40–60ms per character
- The document should feel like a **real Google Doc** being authored — NOT markdown

**Agent panel** (left side) continues showing activity. Status messages can update to:
- "Writing Executive Summary..."
- "Generating market analysis..."
- "Formatting document..."

## Inline SVG Icons Needed

| Icon | Size | Usage |
|------|------|-------|
| Folder | 16px | File tree, filled with subtle color |
| File | 16px | File tree, line icon |
| Pulsing dot | 8px | "Being edited" indicator, animated green circle |
| Bold (B) | 14px | Google Docs toolbar (simplified) |
| Italic (I) | 14px | Google Docs toolbar (simplified) |
| Underline (U) | 14px | Google Docs toolbar (simplified) |

## What NOT to Build

- The Google Docs toolbar does NOT need to be fully faithful — just enough icons to feel real
- No actual text editing capability — everything is animated/scroll-driven
- Do NOT build the closing epilogue — that's Part 7
