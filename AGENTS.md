# AGENTS.md

This file documents the architectural patterns, module boundaries, and documentation standards for the project, as required by the agent rules.

## Project Overview

**Bluefin** is a zero-dependency HTML demo of an AI-native business agent application, designed for quick sharing with investors and stakeholders. The entire experience is a single HTML file driven by scroll-based animations that tell a narrative and then demonstrate the product.

## Architecture

- **Frontend**: A single `index.html` file containing all HTML, CSS, and JavaScript. Zero external dependencies.
- **Backend**: None (static site).
- **Development Server**: A simple Python HTTP server in `main.py` (run via `uv run python main.py`).

## Module Boundaries

- `index.html`: Contains the entire application logic and presentation. All CSS is inline in `<style>` tags. All JavaScript is inline in `<script>` tags. All icons are inline SVGs.
- `main.py`: Serves the files for local testing on port 8000.

## Key Design Decisions

- **Scroll-driven**: All animations advance on scroll down and reverse on scroll up. No click interaction required from the viewer.
- **Customizable recipient**: A `recipientName` variable at the top of the script section personalizes the "Welcome back" message.
- **Zero dependencies**: No external CSS, JS, fonts (unless base64-inlined), or image files.
- **Premium aesthetic**: Apple/Tesla-inspired. Light background, ocean-themed accent colors (light blue → dark blue → violet).
- **Product frame showcase**: The product UI (Sections 2–10) is displayed inside a centered, rounded-corner window (`#product-frame`) floating on a dark backdrop (`#dark-backdrop`). The visual flow is: light background (prologue) → dark backdrop + product frame (demo) → light background (epilogue). All product UI (sidebar, dashboard, workspace) lives inside `#product-frame` using `position: absolute`. See `docs/style_guide.md` Section 9.

## Documentation Index

The following documentation files should be maintained and checked for updates at the end of a coding run:

- `README.md`: Basic project information and setup.
- `docs/design.md`: Design overview and index — links to the 7 implementation sections below.
- `docs/style_guide.md`: Color palette, typography, spacing, component specifications, animation timing, icon inventory.
- `docs/fixes_needed.md`: List of issues and improvements to be fixed.
- `AGENTS.md`: This file, tracking architecture and agent instructions.

### Implementation Sections (in `docs/sections/`)

The design is split into 7 sequential coding parts. Each part has its own detailed spec and builds on the previous:

| Part | File | What It Covers |
|------|------|----------------|
| 1 | `docs/sections/01_foundation.md` | HTML skeleton, CSS variables, scroll engine |
| 2 | `docs/sections/02_prologue.md` | Narrative text animations (Sections 0.0–2) |
| 3 | `docs/sections/03_sidebar_welcome.md` | Persistent sidebar, welcome screen (Sections 2–3) |
| 4 | `docs/sections/04_dashboard_cursor.md` | Dashboard UI, animated cursor (Sections 4–5) |
| 5 | `docs/sections/05_workspace_model.md` | Research workspace, model selector (Sections 6–7) |
| 6 | `docs/sections/06_execution_preview.md` | Plan editing, file tree, Google Docs preview (Sections 8–10) |
| 7 | `docs/sections/07_epilogue.md` | Closing messages (Sections 11–13) |

**Dependency chain:** Part 1 → Part 2 → Part 3 → Part 4 → Part 5 → Part 6 → Part 7
