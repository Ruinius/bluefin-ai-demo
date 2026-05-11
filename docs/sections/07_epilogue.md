# Part 7: Closing Epilogue — Sections 11–13

> **Prerequisite:** Parts 1–6 must be complete. The entire product demo must exist.

## Objective

Build the closing sequence that fades out the product UI and presents three final messages, one at a time.

## Components

### Product UI Fade-Out

As the user scrolls past Section 10 (Preview tab), the entire product UI — sidebar, workspace, panels, everything — fades out together. By the start of Section 11, the screen should be back to a clean background.

**Animation:**

- Use the end of Section 10's progress (0.85–1.0) or early Section 11 progress (0.0–0.2)
- All product UI elements fade to opacity 0 and can be hidden (`display: none` or `visibility: hidden`)
- The sidebar, which has been persistent since Section 2, also fades out here

---

### Section 11 — Closing Message 1 (`section-closing-1`, 100vh)

Centered on screen, same style as the prologue:

> **A business-first AI agent**

**Animation:**

- Fades in at progress 0.1–0.3
- Holds at full opacity 0.3–0.7
- Fades out at progress 0.7–0.9

**Styling:**

- Font: Hero/Narrative size (48px, weight 600, line-height 1.2)
- Color: `var(--text-primary)`
- Centered both horizontally and vertically
- Background: `var(--bg-primary)` or `var(--gradient-subtle)`

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
- [ ] Transition to the product UI with sidebar (Section 2–3)
- [ ] Show the welcome screen (Section 3)
- [ ] Display the dashboard (Section 4)
- [ ] Animate cursor clicking Research (Section 5)
- [ ] Show the workspace layout with Plan tab (Section 6)
- [ ] Animate the model selector dropdown (Section 7)
- [ ] Animate plan editing and execution (Section 8)
- [ ] Show file tree populating in Workspace tab (Section 9)
- [ ] Show Google Docs preview being written (Section 10)
- [ ] Fade out product UI and show three closing messages (Sections 11–13)
- [ ] All animations are reversible (scrolling up plays them backwards)
- [ ] Total scroll distance is approximately 1,550vh
