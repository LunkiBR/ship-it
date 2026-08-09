# AGENTS.md

## Project Context

This repository is the source for a single Claude Code Agent Skill (`ship-it`) that helps an AI coding agent catch commonly-forgotten UX/product details on a screen or feature before it ships: login, checkout, billing, pricing, 404s, admin panels, and around 60 other well-known patterns. It packages a large, still-growing catalog as a router (`SKILL.md`) → section indexes (`sections/`) → per-pattern reference files (`references/`), so an agent loads only what a specific task needs rather than the whole catalog every time.

## Repository Layout

- `SKILL.md` — the skill's entry point: frontmatter (`name`, `description`) plus workflow steps and the judgment/tier rules. Read this first; it never contains pattern content, only pointers to it.
- `sections/*.md` — one flat index per section, listing that section's patterns (name, tier, one-liner, link to its reference file). Nothing here is opened unless `SKILL.md` has already narrowed the task to that section.
- `references/*.md` — one file per pattern, the actual checklist. `TEMPLATE.md` is the exact format every new one follows; `billing.md` and `login.md` are the finished quality bar.
- `generation/` — not part of the skill itself. `PROMPT.md` is the brief used to bulk-author the remaining reference files through a cheaper model, grounded in established UX patterns, product standards, and primary references rather than generated from model intuition alone; `create_references.py` and `verify_references.py` are the scripts that ran it and checked its output.
- `scripts/validate.py` — the one automated check this project has: SKILL.md's frontmatter and line budget against the Agent Skills spec, and every reference file's format against this project's own conventions. Run before committing changes to `SKILL.md` or `references/`.
- `ARCHITECTURE.md` — why the project is shaped this way: one skill instead of many, the tier system, the naming decisions (and the one that got reverted), which real precedents were studied.
- `README.md` — the human-facing pitch and current build status.

## Terminology

- **Section** — one of the four top-level surfaces: Sidekick (mobile app), Control Room (in-product web app), Storefront (marketing website), Choreography (cross-screen interaction flows). These four names are deliberately original branding — see ARCHITECTURE.md's naming section for why, and why that's the *only* place originality was worth the cost.
- **Pattern** — one screen or interaction moment (Login, Cart, 404, Making a card payment...). Always the industry-standard name. Never renamed, regardless of how tempting — see the reverted attempt logged in ARCHITECTURE.md.
- **Tier** — `Fundamental`, `Common`, or `Conditional`. The default assumption for whether a pattern applies to a given product, fixed once per pattern so an agent's "use judgment" has an actual anchor instead of drifting toward whichever answer is less work.
- **Cross-cutting pattern** — a pattern that appears in more than one section's index (Billing, Login, Account, Settings, Search, Cart) but still resolves to exactly one reference file, written once.

## Key Components

The whole design is one instance of progressive disclosure applied twice: `SKILL.md` never lists patterns, only sections; a section index never carries a pattern's checklist, only its name, tier, and a link. An agent doing a coverage check reads at most one section index (never the full catalog); an agent verifying a specific screen opens at most one reference file. See ARCHITECTURE.md's "Three-step workflow" section for the full reasoning and the two existing Claude skills (`impeccable`, `media-use`) this structure was modeled on.

The Judgment calls system in `SKILL.md` is equally load-bearing: a pattern's Tier is a prior, not a verdict — item text should never read as if every product needs every pattern regardless of context.

## Testing Conventions

There's no application code here, so "testing" means spec and format compliance:

```bash
python scripts/validate.py
```

This checks `SKILL.md`'s `name`/`description` against the Agent Skills spec's length and charset limits, its body against the ~500-line budget, and every `references/*.md` for a `Platforms:` line, a valid `Tier:` value, and correctly-formatted (unchecked) checklist items. It runs in CI on every push via `.github/workflows/validate.yml`. It cannot check whether a citation is real — that's a human review responsibility (see Development Rules).

## Development Rules

- Pattern names stay industry-standard. Original naming is spent only on the four section names — never on the ~60 individual patterns.
- One skill, not one per section or per pattern. Read ARCHITECTURE.md's reasoning before proposing a split.
- A citation (WCAG, MDN, Apple HIG, Material Design, GOV.UK Design System, or similar) is only added when confident it resolves to a real, correct source. A fabricated citation is worse than no citation — it teaches something false with the appearance of authority. This is the one thing `scripts/validate.py` cannot catch, so it's the one thing a human reviewer should always spot-check before merging new pattern content.
- New reference files follow `references/TEMPLATE.md` exactly, including the `Tier:` line's default-assumption clause.
- Run `python scripts/validate.py` before committing any change to `SKILL.md`, `sections/`, or `references/`.
