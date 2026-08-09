# Architecture notes — checklist skill

This is the standing design doc for the skill being built in this folder.
It exists so the reasoning behind the structure survives past any single conversation.
Nothing here is installed anywhere — this folder is source only.

## The problem this skill solves

People building software forget to check the boring-but-important details before shipping a screen or feature.
Not "is the code correct" — "did we remember the empty state, the error state, the recovery path, the platform convention."
The fix is a checklist of known patterns (Login, Checkout, Billing, Onboarding, Empty State, and so on), each with the specific details that are easy to skip.
An agent building or reviewing a screen should be able to pull up the checklist for that exact pattern and verify the implementation against it.

## Source material

Four notes in the maintainer's personal Obsidian vault, so far:
- `Mobile app checklist (1–20).md` — 20 patterns (gesture navigation, splash screen, checkout, tab bar navigation, in-app notifications, action sheet, billing, search, camera, map view, onboarding checklist, paywall, onboarding, chat, settings, in-app browser, cart, login, account, invite).
- `Web App Checklist.md` — 10 patterns so far (2FA, notification settings, account, help center, billing, settings, user management, single item detail, admin panel, empty state).
- `WebSite Checklist.md` — 23 patterns (security, about, privacy, features, testimonials, affiliate, compare, status, billing, press/media, waitlist, team, cart, search, careers, blog post, contact us, pricing, FAQ, 404, login, blog, sign up).
- `Flow CheckList.md` — 13 patterns, a different axis: cross-screen interaction moments rather than whole screens (adding to cart, uploading media, verifying account, canceling subscription, filtering items, saving changes, entering promo code, showing input error, resetting password, deleting account, contacting support, making a card payment, submitting a form).

More categories are being ingested by the user over time — the architecture below is built to keep absorbing them without restructuring. The three screen-based notes mix Portuguese and English and, combined, run to roughly 20,000 characters each — a single note is already too large to load in full just to check one pattern. They also show real duplication: Billing (all three), Login (Mobile + Website), Account, Settings, Search, and Cart (each in two) are each described once per category, independently and inconsistently. Eliminating both problems — oversized files and duplicated patterns — drives the two decisions below: one reference file per pattern, and an index the agent reads before opening any of them.

## Spec rules this design follows

From Anthropic's Agent Skills documentation, cross-checked against the installed `skill-creator` skill's own source (the official `skill-creator` plugin's `SKILL.md`):

- A skill is a folder containing `SKILL.md` (YAML frontmatter + Markdown body), plus optional bundled files. Only `name` and `description` are required frontmatter fields.
- `name`: max 64 characters, lowercase letters/numbers/hyphens only, cannot contain "claude" or "anthropic". Convention leans toward gerund form (`processing-pdfs`), but real installed skills on this machine (`impeccable`, `ponytail`, `media-use`) mostly use a plain brand word instead — the name is for identity, not for triggering.
- `description`: max 1024 characters, written in third person. Claude is documented to under-trigger skills, so the description should be deliberately explicit about trigger contexts and phrases rather than just describing what the skill does.
- Progressive disclosure has three levels: (1) name + description, always in context, roughly 100 tokens; (2) the `SKILL.md` body, loaded only once the skill triggers, kept under roughly 500 lines; (3) bundled reference files, loaded only on demand, effectively unlimited in size or count.
- Reference files should stay one level deep from `SKILL.md` — avoid chains where a reference file points to another reference file. Any reference file over 100–300 lines should carry a table of contents.

## Two real precedents, and why one applies here

Two multi-domain skills are already installed on this machine, and their actual files (not just their one-line descriptions) were read to see how each handles breadth:

**hyperframes family** — `hyperframes`, `hyperframes-animation`, `hyperframes-core`, `hyperframes-cli`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-registry` are seven separate top-level skills. This split exists because each one is a genuinely different technical workflow — rendering CLI operations, animation math, brand/creative direction, and so on are not interchangeable tasks. The main `hyperframes` skill acts as a mandatory entry point with an explicit `Need → Skill` routing table, closing with: "Domain skills never take ownership of the end-to-end deliverable. Load only what the active workflow needs."

**media-use** — describes itself as "the single skill for every media need," and deliberately consolidates a much wider breadth (background music, sound effects, images, icons, logos, voice, text-to-speech, transcription, captions, color grading, background removal) into one skill, because every one of those subdomains is reached through the same verb and the same workflow (`resolve`, in its case). Its `SKILL.md` is only 96 lines and is almost entirely a routing table — "Where to look — read only the file your task needs" — pointing into nine `references/*.md` files, one per task type. `impeccable` (UI/UX audits) uses the identical shape: one skill, a command table, and roughly 30 files under `reference/`.

The dividing line: split into separate skills when the triggering context genuinely differs (hyperframes' case — nobody asks for "animation" and "CLI rendering" in the same breath). Split into reference files within one skill when everything shares a single workflow and trigger shape (media-use's case).

**This checklist is media-use's case.** "Check this screen or feature against known best practices before shipping" is one workflow, whether the screen is mobile, web, a marketing site, or a desktop app. Splitting by platform would also recreate, at the skill level, the exact duplication already visible in the Obsidian notes today.

## On becoming a widely-used, public skill

The highest-adoption examples found during research — `VoltAgent/awesome-agent-skills` (~30k stars) and `obra/superpowers` (reported as the most-starred Claude Code skills repo) — win on positioning and curation, not on being mega-skills: a sharp one-line value proposition, granular and well-named skills, visible trust signals. That points toward keeping this skill itself lean and single-purpose, and putting adoption effort into the repo's README and framing later, once naming and content are settled — not into fragmenting the skill.

## Recommended architecture

- **One skill**, not one per section. Folder/skill name is still open (see Naming).
- `SKILL.md` — pure router: steps + branch logic + a `Sections` table naming each section and pointing at its index file. No pattern names, no checklist content lives here — see Three-step workflow below.
- `sections/<name>.md` — one file per section (mobile, web app, website, more later), each a flat index of that section's patterns: name, one-line description, link to its reference file.
- `references/<pattern-slug>.md` — **one file per pattern, not per section.** Cross-cutting patterns (Login, Billing, Settings, Account, Search, Cart, and others as they surface) get a single merged file covering every section they apply to, with section-specific notes inline only where they genuinely differ. This is the direct fix for the original Billing/Settings/Login duplication across the source notes.
- `references/TEMPLATE.md` — the authoring template, so ingestion of new sections (mobile, web app, website, whatever comes next) produces consistent files without needing to re-derive the format each time.
- Descriptions are written to be explicit about trigger contexts (mobile, web app, website; "before shipping", "review", "audit", "is this done") so the skill fires even when nobody says the word "checklist."

## Three-step workflow: route, then index, then detail

A single category note running ~20,000 characters cannot be loaded whole just to check one pattern — most of it would be irrelevant to the task at hand. Once the count of sections grows past three (mobile, web app, website, plus more being ingested — roughly 5 sections × 10 patterns × 5 items projected, several hundred checklist items total), even a flat index of every pattern across every section stops being the right thing to load on every trigger: a task clearly scoped to a mobile screen has no use for the Website section's twenty-some rows. `SKILL.md` is kept a pure router — steps and branch logic only, no pattern content and, as of this revision, no pattern index either — modeled directly on `mattpocock-skills:ask-matt`, whose entire `SKILL.md` is a flow map that never inlines a skill's content, only routes to it with a one-line reason. Three steps, each a step down the information hierarchy:

1. **Route to a section.** Mobile app, web app, website, or a section added later — named in a small table in `SKILL.md` itself (currently 3 rows, one per section, growing by one row per section ingested).
2. **Index check, one section, no pattern files.** Open only that section's file under `sections/` and, from pattern names and one-liners alone, name which patterns the project has, is building, or lacks. This is the step that answers "what's missing" (no Status page, no 2FA) without opening any pattern's detail.
3. **Detail check, one pattern at a time.** Only for the pattern(s) actually being built, reviewed, or fixed right now, open its reference file (linked from the section index) and check the implementation against every item in it.

Each step is a context pointer to the next: `SKILL.md` names sections and points at `sections/<name>.md`; each section file names patterns and points at `references/<pattern>.md`. Nothing above a step restates what the step it points to already says — the section files don't repeat the workflow, the reference files don't repeat which sections use them beyond a `Platforms:` line.

## Judgment: not every pattern applies to every product

A checklist applied mechanically produces false positives — telling a B2B tool with no self-serve purchase that it's "missing" a Cart, or a two-person startup that it's "missing" a Careers page. That failure is what erodes trust in a tool like this faster than any missing pattern would: a fourth Obsidian note (`Flow CheckList.md`, 13 patterns — Adding to cart, Uploading media, Verifying account, Canceling subscription, Filtering items, Saving changes, Entering promo code, Showing input error, Resetting password, Deleting account, Contacting support, Making a card payment, Submitting a form) makes this unavoidable rather than an edge case: most of those patterns only make sense if the product already has the underlying capability (something to sell, a subscription, an upload feature), so the applicability question comes up on nearly every one, not occasionally.

**Local precedent**: `impeccable` (the UI/UX audit skill already installed here) solves the identical problem for design audits. Its `Setup` step runs `context.mjs` once per session to load `PRODUCT.md` and `DESIGN.md` — durable context about what the product actually is — before any critique or audit runs, and its routing explicitly does not hard-block when that context is missing: "a narrow refinement of existing code proceeds on the incumbent implementation as context.mjs directs, offering init afterward rather than blocking on it." The lesson taken from this: gather product context once, weigh every judgment call against it, and never let a missing context file stop the work outright.

**External grounding**: Atul Gawande's *Checklist Manifesto* argues a checklist has to leave room for judgment and craft rather than being followed rigidly — the discipline is in first recognizing what kind of situation you're in, then applying the checklist to that. A 2026 paper on auditing AI agents (arXiv 2603.20637, "AEGIS") names two of the specific reasoning failures relevant here: **Speculation** (flagging a defect without verifying it against real context) and **Over-Trust** (accepting a rule's applicability without checking it) — both map directly onto "the skill said Cart is a pattern, so tell them to build one."

**What this drives in `SKILL.md`**: a new step 1 ("build a one-line picture of the product") ahead of the section/index/detail steps, and a `Judgment calls` section stating the guardrails explicitly rather than leaving them implied — because the failure runs in both directions. An agent that under-applies judgment nags about a Cart nobody needs; an agent that over-applies it can just as easily wave away a Privacy Policy because "the product is small," when data-protection law doesn't grant a size exemption. The fix for both is the same: state the one-line reason before excluding anything, weigh legal/security patterns against the law rather than the product's size, and — once the person has actually answered — don't ask again.

## Tiers: a prior for the judgment call, not just a rule to invent each time

The Judgment calls section above tells the agent to reason about applicability, but "use judgment" with no anchor drifts toward whichever answer is less work — usually toward excluding things, since a stated gap invites pushback and a stated non-gap doesn't. The fix: every pattern carries a fixed **Tier**, set once in its section index (and echoed in its reference file once one exists), that fixes the starting assumption before any product-specific reasoning runs.

Three tiers, each changing the default in a specific direction:
- **Fundamental** — assume it applies everywhere in the section; excluding it needs a stated, unusual reason held to real suspicion (Security, Privacy, 404, Contact Us, Empty State, Saving changes, Showing input error, Deleting account — several of these are legal/data-protection floors, not style choices).
- **Common** — assume it applies unless the product picture clearly rules it out (Billing, Login, Checkout, Making a card payment — most monetized or account-based products need these, but free or sales-led products are a real, ordinary exception).
- **Conditional** — assume it does *not* apply until a specific narrower capability is confirmed present (Cart, Adding to cart, Entering promo code, Camera, Chat, Invite — each needs something more specific than "this product could plausibly do X in general").

The worked example that drove this: Cart and Checkout/payment are both non-Fundamental, but payment outranks cart, because most products that charge money do so through some Common-tier payment flow, while only a subset of those layer a Conditional-tier multi-item cart on top. Tiering them the same (or leaving both to be reasoned from scratch every time) would lose that distinction and let the agent treat a missing Cart as seriously as a missing payment method.

Assigning tiers was a judgment pass over the ~59 patterns and flow items known so far, done once here rather than left for the agent to re-derive per run — re-deriving "is Splash Screen more expected than Camera" from nothing, every session, is exactly the kind of restated reasoning progressive disclosure is supposed to avoid paying for twice.

## Original names — sections only, patterns stay plain

A collaborator who helped build part of the original checklist reviewed this project and liked the mechanism, but asked for names distinct from the source markdown's own wording. First pass renamed all 66 patterns too (Login → "Welcome Back", Cart → "The Basket," and so on) — corrected before it reached any user-facing file: a creative name is only worth it where it doesn't cost the agent anything to use, and "Login," "About," "Cart," "Billing," "Settings" are already the industry-standard terms for what they are. Renaming universally-recognized UI vocabulary adds a translation step every time the skill is used (the agent has to remember "Welcome Back means Login") for no real gain — the opposite of agent ergonomics. Original names earn their place only at the **section** level, where there are just four of them, they're referenced constantly, and they're the layer that most resembled `checklist.design`'s own top-level categories:

| New name | Was |
|---|---|
| Storefront (marketing website) | Website |
| Sidekick (mobile app) | Mobile app |
| Control Room (in-product web app) | Web app |
| Choreography (cross-screen flows) | Flow |

All 66 pattern names stay exactly as the source calls them (Login, Cart, Billing, About, Onboarding, and so on) — the `Covers` one-liner next to each is where this project's own voice and detail live, not the name.

The `description` frontmatter field in `SKILL.md` also keeps plain terms ("mobile app screen," "web app," "website") rather than the new section names — the description exists purely to make the skill trigger reliably, and nobody asks to review their "Sidekick." The section names are read only after the skill has already fired, not before.

## Standards research folded into the two written patterns

Requested alongside the renaming: pull real detail from WCAG/WAI, MDN, Material Design, Apple HIG, and GOV.UK Design System into the material, not just rename it. Applied so far to the two patterns that already have full reference files:

- **Login** — [WCAG 2.2 SC 3.3.8, Accessible Authentication (Minimum)](https://w3c.github.io/wcag/understanding/accessible-authentication.html): no step in authentication may require a cognitive function test (memorizing a password, transcribing an SMS code) unless an alternative or assist mechanism exists — the standards basis for why password-manager support and passkeys aren't nice-to-haves. [MDN's autocomplete reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) confirms `current-password` (sign-in) vs `new-password` (signup/change) as the two distinct values, and that browsers may ignore `autocomplete="off"` on login fields specifically to keep password managers working. GOV.UK Design System's password guidance: let users paste their password, and support a reveal toggle.
- **Billing** — [Apple's App Store Review Guideline 3.1.1](https://developer.apple.com/app-store/review/guidelines/): a Restore Purchases action is mandatory (not just good practice) for any app with non-consumable purchases or auto-renewing subscriptions, and required subscription disclosures (title, length, price, and working links to the privacy policy and terms) must appear before the user is asked to subscribe — added as its own item, which the earlier draft didn't have.

At this scale — 59 patterns across four sections — writing every reference file by hand would cost more tokens and time than the content is worth per pattern. The fix: `generation/PROMPT.md` packages the same standards, format, and anti-hallucination rules demonstrated above into a brief a cheaper model can execute, grounded in established UX patterns, product standards, and primary references rather than generated from model intuition alone. All 57 remaining patterns were generated this way, then spot-checked by hand (one formatting bug found and fixed — a stray backtick left in `checkout.md`'s Tier line; citations checked against what's actually verifiable, none found fabricated). `scripts/validate.py` now covers the mechanical half of that check (format, Tier validity, no pre-checked boxes) so it doesn't have to be redone by eye every time; citation accuracy stays a human-review responsibility, documented as such in `AGENTS.md`.

## Naming — decided: `ship-it`

Matches the tone set by the user's own `hop-in` project: casual, simple, a little playful, still clearly purposeful. Earlier brainstormed candidates, kept here for the record: `gutcheck` · `onceover` · `go-for-launch` · `readycheck` · `allclear` · `lastlook` · `sweep`.

## License: MIT

Same choice both real precedents (`ponytail`, `agent-skills`) made.

## What's deliberately not done yet

- Bringing Web app to parity with Mobile/Storefront/Choreography on its Login pattern, or ingesting further sections beyond the four above — the user is still adding those.
- Any edits to the Obsidian vault — this project's content now leads, but hasn't been synced back.
- Wrapping this in `skills/<name>/` alongside a `.claude-plugin/plugin.json` (the convention both `ponytail` and `agent-skills` use once a repo is meant to be installed as a plugin from a marketplace). For now the repo root stays the skill's own root, so cloning the repo directly gives a working `ship-it/` folder to copy straight into `~/.claude/skills/` — matching how `impeccable`/`media-use` are laid out. Revisit if this ever needs to bundle more than one skill or ship through a marketplace.
