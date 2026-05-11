# Fixes Needed

This file tracks issues and improvements needed for the Bluefin AI demo.

## Issues Checklist

### Global / Aesthetics

- [ ] **Revamp Typography and Color Palette**: Transition from the current "app" feel to a more editorial, literary, and thoughtful vibe.
  - **Vibe**: Editorial, literary, thoughtful.
  - **Typography**: Integrate `Cormorant Garamond` for headings and `Source Serif 4` for body text.
  - **Colors**: Use a warm cream background (`#faf9f7`), charcoal text (`#1a1a1a`), and a crimson accent color (`#c41e3a`).
  - **Style Elements**: Implement drop caps for section starts, pull quotes for emphasis, and elegant horizontal rules for section breaks.

### Section 0 — Opening Statement

- [ ] **Enhance Tool Mentions with Logos and Brand Colors**:
  - **Claude Code**: Style text with orange brand color and insert the Claude Code logo SVG before the text.
  - **Codex**: Style text with black brand color and insert the Codex logo SVG before the text.
  - **Jules**: Style text with purple brand color and insert the Jules octopus logo SVG before the text.
  - **OpenHands**: Style text with yellow brand color and insert the OpenHands logo SVG before the text.

### Section 3 — Sidebar & Welcome

- [ ] **Update Bluefin Logo**: Replace the 'X' in the current gradient circle logo with a stylized 'B'.
- [ ] **Remove User Avatar**: Remove the circle with the letter 'S' from the sidebar to simplify the UI.
- [ ] **Adjust Sidebar Entrance Animation**: Change the animation from sliding in from the left to a smooth fade-in.
- [ ] **Dynamic Recipient Name**: Update the "Welcome Sarah" text to dynamically use the filename of the presentation (e.g., "Welcome index" if served as `index.html`).

### Section 6 — Research Workspace

- [ ] **Add Missing Command/Chat Input Area**: Implement the input field for user commands.
- [ ] **Relocate Model Selector**: Move the selector to the bottom of the left panel, below the command/chat input area.
- [ ] **Relocate Pause Button**: Move the pause button to the bottom right edge of the command/chat input area.
- [ ] **Expand Overall Instructions**: Add a detailed instruction block stating "You are a senior research analyst..." to provide context for the agent's work, placed on the same level as Steps 1, 2, and 3.
- [ ] **Enhance Plan Area Interactivity Cue**: Wrap the static plan text items in distinct gray containers/textboxes to visually indicate they are editable.

### Section 8 — Execution Preview

- [ ] **Correct Command/Chat Input Placement**: Ensure the input area is placed correctly on the Left Hand Side (LHS) instead of incorrectly sitting in the plan area.

### Section 10 — Google Docs Preview

- [ ] **Remove Unwanted Scrollbar**: Fix the container styling to eliminate the visible scrollbar in the preview area.
- [ ] **Revamp Toolbar to Mimic Google Docs**:
  - Remove the current simple bold, italics, and underline controls.
  - Insert a simplified Google Docs SVG icon to reinforce the platform identity.
- [ ] **Add Breadcrumb/Link Path**: Display a dynamic path link showing where the document is stored, using the recipient's name (derived from the filename), e.g., `[name]/Drive/d/1aBcDeFgHiJkLmNoP...`.
- [ ] **Add Helper Instruction**: Include a clear call-to-action text stating: "Go to Google Docs to edit directly".
