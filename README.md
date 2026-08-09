# Ship It

[![Validate](https://github.com/LunkiBR/ship-it/actions/workflows/validate.yml/badge.svg)](https://github.com/LunkiBR/ship-it/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/github/license/LunkiBR/ship-it)](LICENSE)

**A Claude Code skill that catches the boring-but-important details before you ship a screen or feature.**

Not a linter for your code — a linter for the *product*. Login, checkout, billing, empty states, 404s, admin panels: the parts of an app that follow well-known patterns, and that get half-finished anyway because nobody double-checked the boring stuff before calling it done.

## The problem

Most teams don't ship broken code. They ship *incomplete* screens: a login form with no "forgot password," a paywall with no restore-purchases button, a pricing page with no FAQ, a cancel-subscription flow that guilt-trips the user on the way out. None of that shows up in a test suite. It shows up in support tickets, one-star reviews, and App Store rejections.

This skill gives an agent a structured, opinionated catalog of these patterns — organized so it can be consulted cheaply and precisely, not dumped wholesale into every conversation.

## How it works

A single skill, three hops deep, each hop loaded only when the one before it says to:

```
SKILL.md              →  a pure router: steps, judgment rules, and 4 section names
  sections/*.md        →  one flat index per section: pattern name + one-liner + tier
    references/*.md     →  one file per pattern: the actual checklist, opened only when that
                            exact pattern is the one being built or reviewed
```

Nothing upstream repeats what's downstream. `SKILL.md` doesn't know what's inside a Login checklist; a section index doesn't know what "Fundamental" means beyond the word itself. This is deliberate — see [ARCHITECTURE.md](ARCHITECTURE.md) for the full reasoning, including the two existing Claude skills this design borrows from (`impeccable`, `media-use`) and the Anthropic Agent Skills spec it follows (progressive disclosure, `<500`-line `SKILL.md`, one-hop reference files).

Three things make this more than a flat list of checkboxes:

- **Sections, not platforms.** The four sections — `Sidekick` (mobile app), `Control Room` (in-product web app), `Storefront` (marketing website), `Choreography` (cross-screen interaction flows) — are just entry points. A pattern like Login or Billing that shows up in more than one section still lives in exactly one reference file, so it's written once and never drifts into two contradictory versions.
- **Tiers, not a flat "does this apply?"** Every pattern is tagged `Fundamental`, `Common`, or `Conditional` — a fixed prior for how surprised the agent should be if it's missing, so "use judgment" has an actual anchor instead of drifting toward whichever answer is less work. Security and Privacy are `Fundamental` (assume they exist; excluding them needs a real reason). A payment flow is `Common` (assume it exists unless the product is free or sales-led). A shopping cart is `Conditional` (assume it *doesn't* exist until something multi-item is confirmed) — payment outranks cart because more products charge money than sell multiple items at once.
- **Judgment calls are explicit, not implied.** `SKILL.md` states the failure modes directly: don't nag a B2B tool about a Cart it doesn't need, but don't wave away a Privacy Policy just because the product is small. Once a person has answered a judgment call, the skill doesn't ask again.

## Status

All 59 indexed patterns across the four sections are written and pass `scripts/validate.py`. The one known gap: the Web App source note never ingested its own Login pattern, so Control Room resolves Login through Mobile/Website's shared file rather than having its own row yet — see `sections/control-room.md`.

| Section | Patterns indexed | Fully written |
|---|---:|---:|
| Sidekick (mobile app) | 20 | 20 |
| Control Room (web app) | 10 | 10 |
| Storefront (website) | 23 | 23 |
| Choreography (flows) | 13 | 13 |

`Billing` and `Login` were written by hand first and set the quality bar; the remaining 57 were generated from `generation/PROMPT.md` against that same bar (real citations only when confident they resolve to something real — WCAG 2.2, Apple's HIG/App Store Review Guidelines, Material Design, MDN, GOV.UK Design System), then spot-checked rather than trusted blindly. What's left is deepening citations further over time, not filling gaps.

## Project structure

```
SKILL.md                     the router — read this first
AGENTS.md                    repo layout, terminology, and rules for anyone extending this
ARCHITECTURE.md              design rationale: why one skill, why tiers, why these sections
CONTRIBUTING.md              how to propose a pattern or report a bad citation
sections/
  sidekick.md                mobile app pattern index
  control-room.md            web app pattern index
  storefront.md              website pattern index
  choreography.md            cross-screen flow pattern index
references/
  TEMPLATE.md                format every new pattern file follows
  *.md                       59 pattern files, one per row in the four section indexes
generation/
  PROMPT.md                  the brief handed to a model to write the bulk of the patterns
scripts/
  validate.py                spec/format compliance check — the project's one automated test
.github/
  workflows/validate.yml     runs validate.py in CI
  ISSUE_TEMPLATE/            new-pattern and inaccuracy-report templates
LICENSE                      MIT
```

## Using it

Once installed as a Claude Code skill, it triggers on intent, not on the word "checklist":

> "I just finished the login screen, can you check it over before I ship?"
> "Building a pricing page for the new plan — what usually goes on one of these?"
> "Is our cancel-subscription flow missing anything?"

The agent picks the section, opens only that section's index, names what the product already has versus what a `Fundamental`/`Common` pattern would predict is missing, then opens only the specific pattern file it needs to check line-by-line.

## Contributing a pattern

Every reference file follows [`references/TEMPLATE.md`](references/TEMPLATE.md): a `Platforms` line, a `Tier` line with its default-assumption clause, a one-line definition, and checklist items as `- [ ] **Item** — what it is and why it matters`. Pattern names stay whatever the industry already calls them (Login, Cart, 404) — original phrasing is reserved for the four section names, not the 60-odd individual patterns, so the checklist stays instantly legible instead of requiring a decoder ring.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process, and [AGENTS.md](AGENTS.md) for repository layout and terminology.

## Security

No code runs as part of using this skill — it's Markdown an agent reads. See [SECURITY.md](SECURITY.md) for the prompt-injection threat model and how to report a concern.

## License

[MIT](LICENSE)

## Acknowledgements

This project was inspired in part by [Checklist Design](https://www.checklist.design/), created by George Hatzis.

Checklist Design was one of the references used to identify common product and UX patterns. This project incorporates those concepts into an independently designed agent-oriented auditing system, with its own architecture, applicability rules, prioritization tiers, indexing, and implementation logic.

This project is not affiliated with, endorsed by, or an official adaptation of Checklist Design.

If you find Checklist Design useful, please support and explore the original project.
