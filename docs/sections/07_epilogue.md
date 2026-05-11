# Part 7: Closing Epilogue — Sections 11–13

> **Prerequisite:** Parts 1–6 must be complete. The entire product demo must exist.

## Objective

Build the closing sequence that fades out the product frame, transitions the dark backdrop back to a light background, and presents three final messages on the clean light background.

## Components

### Product Frame Fade-Out & Background Transition

As the user scrolls past Section 10 (Preview tab), the entire product frame — sidebar, workspace, panels, everything inside it — fades out together. Then the dark backdrop transitions back to the light background. By the start of Section 11, the screen should be back to the same clean light background (`var(--bg-primary)`) that the prologue used.

**Animation (two phases):**

**Phase 1 — Product frame fades out:**
- Use the end of Section 10's progress (0.85–1.0) or early Section 11 progress (0.0–0.15)
- The entire product frame (including all contents — sidebar, workspace, panels) fades to opacity 0
- Can be hidden (`display: none` or `visibility: hidden`) after fade completes

**Phase 2 — Dark backdrop transitions to light:**
- Section 11 progress (0.0–0.3)
- The background transitions from `var(--bg-dark-backdrop)` (`#0D1117`) back to `var(--bg-primary)` (`#FAFBFD`)
- This creates a satisfying visual bookend: light → dark (product) → light (closing messages)
- The closing messages should NOT appear until the background has fully transitioned to light

---

### Section 11 — Closing Message 1 (`section-closing-1`, 100vh)

Centered on screen, same style as the prologue:

> **A business-first AI agent**

**Animation:**

- Fades in at progress 0.1–0.3
- Holds at full opacity 0.3–0.7
- Fades out at progress 0.7–0.9

**Styling:**

- Font: Hero/Narrative size (32px, weight 600, line-height 1.2)
- Color: `var(--text-primary)`
- Centered both horizontally and vertically on the viewport
- Background: `var(--bg-primary)` — light, matching the prologue aesthetic

---

### Section 12 — Closing Message 2 (`section-closing-2`, 100vh)

Centered on screen:

> **Cost conscious with the right AI model for every task**

Same animation pattern and styling as Section 11.

---

### Section 13 — Closing Message 3 (`section-closing-3`, 100vh)

Centered on screen:

> **On-prem and hyper-secure deployments available**

Same animation pattern and styling as Sections 11–12.

**End state:**

- After Section 13's individual fade-in/out cycle, a final scroll section reveals all three closing messages stacked vertically (visible simultaneously)
- Below the three messages, a smaller caption-sized message reads: "If you liked this presentation, please let me know by giving a star to:" followed by a clickable link to `https://github.com/Ruinius/bluefin-ai-demo`
- The link must be a real `<a>` tag with `target="_blank"` and `pointer-events: auto` so it is clickable
- The page should not allow further scrolling past this final section

## What NOT to Build

- No interactive elements in the epilogue — purely visual (except the GitHub star link in the end state)
- No buttons — this is a passive scroll presentation

## Final Checklist

After implementing Part 7, the complete demo should:

- [ ] Start at Section 0.0 (instructions)
- [ ] Scroll through the narrative prologue (Sections 0–2)
- [ ] Transition to dark backdrop with centered product frame (Section 2)
- [ ] Show the welcome screen inside the product frame (Section 3)
- [ ] Display the dashboard (Section 4)
- [ ] Animate cursor clicking Research (Section 5)
- [ ] Show the workspace layout with Plan tab (Section 6)
- [ ] Animate the model selector dropdown (Section 7)
- [ ] Animate plan editing and execution (Section 8)
- [ ] Show file tree populating in Workspace tab (Section 9)
- [ ] Show Google Docs preview being written (Section 10)
- [ ] Fade out product frame, transition dark backdrop back to light, and show three closing messages (Sections 11–13)
- [ ] All animations are reversible (scrolling up plays them backwards)
- [ ] Total scroll distance is approximately 1,550vh
