# Design Document: Zero Dependency HTML Demo

## Project Overview

This project is a zero dependency HTML demo of an app, designed to be easily shareable with friends and investors for quick reactions.

## User Experience / Flow

The demo relies on scroll-based interactions to present a narrative before revealing the application interface.

### Initial View (Top of page)
The first thing the user will see is the following text:
> AI-native engineers have: Jules, Codex, Claude Code, OpenHands, and a dozen powerful tools.

### Scroll Interaction 1
As the user scrolls down, the previous message will fade out, and the following text will appear:
> AI-native business folks are saying:
> "What is a markdown? I need a Google Docs or at least a DOCX."
> "I just spent two hours trying to setting up a MCP server for Databricks. What is MCP?"
> "Holy crap, running Claude for a hour on my presentation costed $150."

### Scroll Interaction 2
As the user continues to scroll down, the secondary message fades out, and the main app interface emerges.

## Technical Constraints

- The final deliverable must be a single, zero-dependency HTML file (no external CSS or JS libraries, everything inline or within `<style>`/`<script>` tags).
- Interactions (scroll, fade) must be implemented with vanilla JavaScript and CSS.
