# Bluefin AI Demo — v1.0

![Release](https://img.shields.io/badge/release-v1.0-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Tech](https://img.shields.io/badge/tech-HTML5%20%2F%20CSS3%20%2F%20JS-orange)

This repository contains a zero-dependency HTML presentation for **Bluefin**, a business-first AI agent application.

The entire experience is a single HTML file driven by scroll-based animations that tell a narrative and demonstrate the product's value proposition.

## The Idea: Bluefin

Bluefin is designed to solve common pain points for business users interacting with AI:
- **Business-Friendly Outputs**: Generates documents directly in formats users need (like Google Docs or DOCX) rather than raw markdown.
- **Cost Conscious**: Automatically selects the right AI model for every task to keep costs under control.
- **Secure**: Offers on-prem and hyper-secure deployments.

## Dynamic Personalization

The demo features dynamic personalization based on the filename:
- The "Welcome back, [Name]" message reads the filename of the presentation.
- If you want to send the presentation to a specific person (e.g., **Tiger**), simply rename `index.html` to `Tiger.html`.
- If served as `index.html`, it falls back to "Welcome back, index".

## How to Run the Demo

To view the demo locally, you can use the provided Python development server:

1. Ensure you have `uv` installed.
2. Run the server:
   ```bash
   uv run python main.py
   ```
3. Open your browser and navigate to `http://localhost:8000`.

Alternatively, since it is a zero-dependency static file, you can simply open `index.html` (or your renamed file) directly in any modern web browser.

## Support the Project

This release (v1.0) marks the completion of the interactive demo.
- **If you like the idea, please give this project a star!** ⭐️
- If there is enough demand, I will proceed with building the full product.

---

For technical details on the design and implementation, see [docs/design.md](docs/design.md).

