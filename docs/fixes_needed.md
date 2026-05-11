# Fixes Needed

This file tracks issues and improvements needed for the Bluefin AI demo.

## Issues Checklist

### Global / Aesthetics

- [x] **Revamp Typography and Color Palette**: Transition from the current "app" feel to a more editorial, literary, and thoughtful vibe.
  - **Vibe**: Editorial, literary, thoughtful.
  - **Typography**: Integrate `Cormorant Garamond` for headings and `Source Serif 4` for body text.
  - **Colors**: Use a warm cream background (`#faf9f7`), charcoal text (`#1a1a1a`), and a dark blue accent color like the ocean.
  - **Style Elements**: Implement drop caps for section starts, pull quotes for emphasis, and elegant horizontal rules for section breaks.
  - **Font Size**: for all the non-product portion, the font sizes should be similar.

### Section 0 — Opening Statement

- [x] **Enhance Tool Mentions with Brand Colors**: (Logos skipped per user request)
  - **Claude Code**: Style text with orange brand color (`#D97757`)
  - **Codex**: Style text with black brand color (`#000000`)
  - **Jules**: Style text with purple brand color (`#673AB7`)
  - **OpenHands**: Style text with yellow brand color (`#FFCD27`)

### Section 3 — Sidebar & Welcome

- [x] **Update Bluefin Logo**: Replace the 'X' in the current gradient circle logo with a fish fin shape.
- [x] **Remove User Avatar**: Remove the circle with the letter 'S' from the sidebar to simplify the UI.
- [x] **Adjust Sidebar Entrance Animation**: Change the animation from sliding in from the left to a smooth fade-in.
- [x] **Dynamic Recipient Name**: Update the "Welcome Sarah" text to dynamically use the filename of the presentation (e.g., "Welcome index" if served as `index.html`).
- [x] Remove the exit button
- [x] Move the widget setting button to the bottom

### Section 6 — Research Workspace

- [x] **Add Missing Command/Chat Input Area**: Implement the input field for user commands.
- [x] **Relocate Model Selector**: Move the selector to the bottom of the left panel, below the command/chat input area.
- [x] **Relocate Pause Button**: Move the pause button to the bottom right edge of the command/chat input area.
- [x] **Expand Overall Instructions**: Add a detailed instruction block stating "You are a senior research analyst..." to provide context for the agent's work, placed on the same level as Steps 1, 2, and 3.
- [x] **Enhance Plan Area Interactivity Cue**: Wrap the static plan text items in distinct gray containers/textboxes to visually indicate they are editable.
- [x] The Command/Chat is fading in, which is wrong. It should be present from the start of this section
- [x] Remove the blinking blue rectangle after "Final Outputs: Google Docs"
- [x] Remove the blinking blue rectangle in the command / chat input area"

### Section 8 — Execution Preview

- [x] **Correct Command/Chat Input Placement**: Ensure the input area is placed correctly on the Left Hand Side (LHS) instead of incorrectly sitting in the plan area.
- [x] Need to fix the strict order of events (in order), and this should happen fairly slowly so the audience can follow:
  - [x] Add the "Save to Google Drive..." text after Google Docs. This is already done correctly.
  - [x] Move the mouse to "Step 1:..."
  - [x] Add "Special focus on Campbell and General Mills" text after "Step 1: Collect... analyst reports." in a way that shows the user is typing more instructions
  - [x] The mouse moves in between "Step 1" and "Step 2" and stops. THEN the new Step 2 box appears.
  - [x] The mouse moves to the new Step 2 and types "save all the reports you find in the input folder"
  - [x] Move the mouse to the input / command area much slower, so the user has time to follow.
  - [x] Type "execute for the US snacks industry in 2026". This is already done correctly. Hurray
  - [x] Simulate that the user hit enter. So the input / command area becomes blank again. A text bubble appears above "Agent is working" with "execute for the US snacks industry in 2026"
  - [x] Slow down all the steps, such as "Searching databases" to simulate better that the agent is hard at work

### Section 10 — Google Docs Preview

- [x] **Remove Unwanted Scrollbar**: Fix the container styling to eliminate the visible scrollbar in the preview area.
- [x] Remove all the blinking blue lines.
- [x] **Revamp Toolbar to Mimic Google Docs**:
  - Remove the current simple bold, italics, and underline controls.
  - Insert a simplified Google Docs SVG icon to reinforce the platform identity.
- [x] **Add Breadcrumb/Link Path**: Display a dynamic path link showing where the document is stored, using the recipient's name (derived from the filename), e.g., `[name]/Drive/d/1aBcDeFgHiJkLmNoP...`.
- [x] **Add Helper Instruction**: Include a clear call-to-action text stating: "Go to Google Docs to edit directly".
