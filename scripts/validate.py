#!/usr/bin/env python3
"""Spec-compliance check for this skill. Stdlib only, no dependencies.

Checks SKILL.md against the Agent Skills spec (name/description limits, body
line budget) and every references/*.md against this project's own format
(Platforms line, Tier line with a valid value, no pre-checked boxes).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ERRORS = []

VALID_TIERS = {"Fundamental", "Common", "Conditional"}


def check_skill_md():
    path = ROOT / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        ERRORS.append("SKILL.md must start with a YAML frontmatter block (---)")
        return
    end = text.find("\n---", 4)
    frontmatter = text[4:end]
    body = text[end + 4:]
    fm = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()

    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        ERRORS.append(f"SKILL.md name {name!r} must be 1-64 lowercase letters/numbers/hyphens")
    if "claude" in name or "anthropic" in name:
        ERRORS.append(f"SKILL.md name {name!r} must not contain 'claude' or 'anthropic'")

    desc = fm.get("description", "")
    if not (0 < len(desc) <= 1024):
        ERRORS.append(f"SKILL.md description must be 1-1024 chars, got {len(desc)}")

    body_lines = body.count("\n")
    if body_lines > 500:
        ERRORS.append(f"SKILL.md body is {body_lines} lines, over the 500-line budget")


def check_reference_files():
    for path in sorted((ROOT / "references").glob("*.md")):
        if path.name == "TEMPLATE.md":
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            ERRORS.append(f"references/{path.name}: must start with a '# Title' heading")
        if not re.search(r"^Platforms: .+$", text, re.MULTILINE):
            ERRORS.append(f"references/{path.name}: missing a 'Platforms: ...' line")

        tier_match = re.search(r"^Tier: (\w+)", text, re.MULTILINE)
        if not tier_match:
            ERRORS.append(f"references/{path.name}: missing a 'Tier: ...' line")
        elif tier_match.group(1) not in VALID_TIERS:
            ERRORS.append(
                f"references/{path.name}: Tier {tier_match.group(1)!r} must be one of {sorted(VALID_TIERS)}"
            )

        for i, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("- [x]"):
                ERRORS.append(
                    f"references/{path.name}:{i}: pre-checked ('- [x]') item — "
                    "reference files describe what to check, not what's already done"
                )
            elif re.match(r"^- \*\*", stripped):
                ERRORS.append(f"references/{path.name}:{i}: checklist item missing the '- [ ]' prefix")


def check_sections():
    for path in sorted((ROOT / "sections").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "| Pattern |" not in text:
            ERRORS.append(f"sections/{path.name}: missing the pattern index table")


if __name__ == "__main__":
    check_skill_md()
    check_reference_files()
    check_sections()

    if ERRORS:
        print(f"{len(ERRORS)} problem(s) found:\n")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(1)

    print("All checks passed.")
