# Contributing

All 59 indexed patterns are written (see the Status table in [README.md](README.md)), and contributions are welcome — new patterns, better citations, and new sections most of all.

- **New pattern** → open an issue with the "New pattern" template, or follow [`references/TEMPLATE.md`](references/TEMPLATE.md) exactly if submitting the file directly. Tier and platforms get decided against the rules in `SKILL.md`'s Judgment calls section, not invented per file.
- **New section** (a surface type beyond Sidekick/Control Room/Storefront/Choreography) → talk to the maintainer first. Each section is a real architectural commitment, not just a new folder — see [ARCHITECTURE.md](ARCHITECTURE.md).
- **Found an inaccurate citation or a stale guideline number?** Open an issue with the "Inaccuracy or outdated citation" template. This is the single highest-value report this project can get — a wrong citation is worse than none.

Before submitting a change to `SKILL.md`, `sections/`, or `references/`, run:

```bash
python scripts/validate.py
```

See [AGENTS.md](AGENTS.md) for the full repository layout, terminology, and development rules.
