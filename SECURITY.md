# Security

This is a documentation-only Claude Code skill: a `SKILL.md` router and a set of Markdown checklists an agent reads. There's no server, no user data, and no code that runs as part of *using* the skill. The security questions that actually apply here are different from a typical application's — mainly: can this content be used to make an agent do something it shouldn't.

## Reporting a vulnerability

[Private vulnerability reporting](https://github.com/LunkiBR/ship-it/security/advisories/new) is enabled on this repo — use it for anything you'd rather not discuss in a public issue first (a supply-chain concern, a way this content could be abused to manipulate an agent, etc.). For anything else, including "this citation looks wrong," a public issue is fine and preferred — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Prompt injection

The realistic risk with any repo whose content is meant to be loaded into an agent's context: could a contribution smuggle in text that reads as an instruction to the agent rather than a checklist item — "ignore previous instructions," "run this command," "always approve," that kind of thing.

What limits that here:

- **`SKILL.md` requests no elevated tool access.** There's no `allowed-tools` frontmatter granting Bash, file-write, or network permissions. The entire skill is inert Markdown an agent reads with whatever permissions it already has — it cannot grant itself more. Worst case for a successful injection is *misleading text*, not an *executed action*.
- **Every file has a fixed, checkable shape.** `scripts/validate.py` (run in CI on every push and PR) enforces that reference files are `Platforms`/`Tier`/checklist-item Markdown and nothing else structurally — it won't stop cleverly-worded injection hidden inside a legitimate-looking item, but it does mean a PR can't introduce a new frontmatter block, an executable code fence meant to be run, or a structurally different file without the check failing first.
- **New content is reviewed before merging, specifically for this.** [AGENTS.md](AGENTS.md)'s Development Rules already require a human to check every new citation for accuracy; the same review is the place to catch a checklist item that reads as an instruction rather than a description. A wrong citation and an injected instruction are the same category of problem — content that looks legitimate but shouldn't be trusted at face value — and get the same scrutiny.
- **The skill's own instructions ask the agent to reason, not obey blindly.** `SKILL.md`'s Judgment calls section already tells the agent to weigh every item against the actual product rather than execute the checklist mechanically — the same posture that keeps the skill from nagging about a Cart nobody needs also means a stray "you must now do X" sentence inside a checklist item reads as obviously out of place rather than as a natural next step.

## Dependencies and code execution

- `scripts/validate.py` uses only the Python standard library — no third-party packages, no install step, nothing to compromise via a supply-chain attack.
- It's a maintainer-side check that runs in CI and locally before a contribution is merged. It does not run, and is not needed, when someone installs and uses the skill itself.
- Nothing in this repo executes automatically when the skill is installed or triggered — an agent reads Markdown files, full stop.

## What this skill does *not* cover

`ship-it` checks for missing or incomplete **UX and product** details on a screen or feature — a missing "forgot password" link, no restore-purchases button, that kind of thing. It is not a security or accessibility auditor for the *product being reviewed*: passing every applicable pattern in this catalog says nothing about whether that product's own code, infrastructure, or dependencies are secure. Standards are cited here (WCAG, Apple HIG, GOV.UK, etc.) because they're the best available detail for a given pattern, not because this skill verifies compliance with them.
