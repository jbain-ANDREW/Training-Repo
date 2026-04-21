**Nav:** [Repo README](../README.md) · [Repo README](../README.md)

---

# Training-Repo — Teaching Site Expansion

**Repo:** Training-Repo  
**Status:** Soon  
**Todo refs:** TD019  
**Last updated:** 2026-04-21

---

## Goal
Maintain and expand the intro teaching site at jamesabain.com/Training-Repo — covering VS Code, Python, AI tools (Claude, Copilot), GitHub workflow, and Google Apps Script for students learning to vibe-code.

## Users
Students and beginners learning to program with AI assistance.

## Key Decisions Already Made
- Stack: GitHub Pages static HTML — no build step, no dependencies
- Hosted at `jamesabain.com/Training-Repo/`
- Nav pattern: top nav with dropdowns (VS Code ▾, Python ▾, AI Tools ▾, Exercises ▾)
- VS Code separated from Python (its own dropdown and page)
- Cross-links to Build-With-AI for advanced topics
- Feedback link labelled "Suggest or Improve"

## Next Steps
1. Replace screenshot placeholder divs in `gas-intro.html` and `vscode-setup.html` with real screenshots (TD019)

## Open Questions
- Which pages still need screenshots?
- Any new topics to add to the AI Tools or Exercises dropdowns?

## Prompt Context
- All pages are in `docs/` — static HTML with inline CSS and JS
- Nav is repeated manually on each page (no shared template)
- Pages follow a consistent card/section pattern
- `docs/examples/` holds standalone deployable HTML examples
- `docs/splash-pages/` holds splash page examples

---

**Nav:** [Repo README](../README.md) · [Repo README](../README.md)
