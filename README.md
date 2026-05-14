# Bluefin AI Demo — v1.0

![Release](https://img.shields.io/badge/release-v1.0-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Tech](https://img.shields.io/badge/tech-HTML5%20%2F%20CSS3%20%2F%20JS-orange)

This repository contains a zero-dependency HTML presentation for **Bluefin**, a business-first AI agent application.

The entire experience is a single HTML file driven by scroll-based animations that tell a narrative and demonstrate the product's value proposition.

## 🚀 The Idea: Bluefin

**The Agentic Workspace for People Who Hate Chatbots.**

While the world is distracted by "magic" chat windows, we are building a horizontal AI agent that treats business logic like software engineering. No VCs, no "ARR tax," and no forced $20/month subscriptions. Just deterministic, skill-based workflows that run on the models you choose.

### 🛠 The Thesis

Current AI products are broken in three ways:

- **Interface:** Chatbots are a poor UI for complex, multi-step work.
- **Cost:** You pay for a $20/mo subscription even if you only use $2 worth of tokens.
- **Efficiency:** Products force expensive proprietary models onto tasks that cheap, open-weight models could handle better.

Bluefin replaces the "prompt-and-pray" loop with a Skills-First architecture.

### ✨ Key Features

- **Skills-First UI:** Abandon the CLI and the chat box. Design repeatable "Skills" using a visual builder.
- **The Magic Wand:** A non-engineer's bridge to complexity. Enter your intent, and the system drafts the skill logic, selects the tools, and recommends the most cost-effective model for the job.
- **Sandbox & Sub-Agents:** Your work doesn't happen in a vacuum. Agents spawn sub-agents that save intermediate outputs (PDFs, data, drafts) into a persistent sandbox you can inspect in real-time.
- **Intelligent Model Routing:** Balance cost and results automatically. Use Llama-3 for the grunt work and Claude 3.5 Sonnet only when the reasoning requires it.
- **Tiny Team, Low Margin:** We aren't here for the VC "unicorn" chase. We operate on a thin margin on top of raw compute (via OpenRouter), passing the savings directly to you.

### 🏗 How It Works

1. **Define:** Create a skill (e.g., "Deep Market Research" or "Code Auditor").
2. **Orchestrate:** The system breaks the task into a graph of sub-agents.
3. **Execute:** Watch agents work in the sandbox, generating intermediate files and data before the final summary.
4. **Repeat:** Save the skill. Run it tomorrow with new data. Get the same high-quality result.

### 💸 Pricing

- **Pay-for-what-you-use:** No bloated monthly tiers.
- **Transparency:** We show you exactly what each sub-step costs.
- **BYOK (Optional):** Bring your own API keys to run at cost.

_Built for the AI-savvy user who wants a factory, not a toy._

### 🏗 High-Utility Use Cases

Standard chatbots treat every interaction as a one-off. Our "Factory" architecture enables persistent, complex workflows that require state and memory:

#### 1. The Synthetic Feedback Panel

- **The Problem:** Asking a single LLM "What do you think of this?" results in a generic, homogenized response.
- **The Factory Solution:** Spawn a panel of 5-10 distinct sub-agents, each with a unique "Persona Skill" (e.g., a skeptical CFO, a design-obsessed PM, a security engineer).
- **The Workflow:** The system routes your document to all agents simultaneously. They save their critiques into the sandbox, and a final "Synthesis Agent" aggregates the conflicting viewpoints into a prioritized action report.

#### 2. The Evolving Topic Wiki (Living Research)

- **The Problem:** Researching a complex topic (e.g., "The state of Solid-State Batteries") usually requires a fresh prompt every week, losing context and nuance over time.
- **The Factory Solution:** Create a persistent "Research Folder" in the sandbox.
- **The Workflow:** As new information is fed in, sub-agents check for contradictions with existing "Wiki" entries, update specific sections, and cite new sources. The output isn't a new report; it’s a refined, version-controlled knowledge base that grows with the topic.

#### 3. Isolated Batch Processing (Anti-Contamination)

- **The Problem:** When you feed 20 resumes or 50 legal contracts into one long chat window, the LLM’s "Attention" starts to bleed across documents, leading to hallucinations and "Context Contamination."
- **The Factory Solution:** Use a "Parallel Sandbox" architecture.
- **The Workflow:** Each document is assigned its own isolated sub-agent and temporary workspace. The agents extract data in parallel using a cheap, structured model (like Gemini 1.5 Flash). Only once all data is structured and verified is it consolidated into a final master sheet.

### 💡 Why this requires a "Factory":

- **Persistence:** Your Wiki doesn't disappear when the browser tab closes.
- **Isolation:** The "Security Engineer" persona doesn't get "polluted" by the "CFO's" logic.
- **Concurrency:** Processing 50 documents happens in seconds, not minutes, by spawning 50 tiny workers simultaneously.

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
