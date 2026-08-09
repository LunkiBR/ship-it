You are writing reference documentation for a Claude Agent Skill. Read this entire brief before writing anything — the rules interact, and skipping to the pattern list will produce inconsistent output.

# What you're extending

This skill helps an AI coding agent catch commonly-forgotten UX/product details on a screen or feature before it ships — login, checkout, billing, empty states, 404s, and so on. It works through three layers, each loaded only when the one before it points to it:

```
SKILL.md              a router: workflow steps + judgment rules + 4 section names
  sections/*.md         one flat index per section: pattern name, tier, one-liner, file link
    references/*.md       one file per pattern — YOUR OUTPUT — opened only when that exact
                           pattern is the one being built or reviewed
```

Your job is **only** the bottom layer: write `references/<pattern-slug>.md` files. Do not touch `SKILL.md`, anything in `sections/`, or invent patterns not on the list below. Two files in `references/` are already finished to the target quality bar — `billing.md` and `login.md` — reproduced below in full. Match their density, voice, and format exactly. Do not read them as inspiration to riff on; read them as the spec.

## Why this matters (so you calibrate effort correctly)

A checklist that's generic ("add error handling," "make it accessible") is worthless — an agent reading it learns nothing it didn't already know. A checklist that's specific — a WCAG success-criterion number, the exact `autocomplete` value, the exact App Store guideline that makes a button mandatory rather than a nicety — changes what the agent actually builds. Every item you write should pass this test: **would a competent developer be surprised by this, or catch a real bug by reading it?** If the answer is no, the item is filler; cut it or make it specific enough that the answer becomes yes.

# The two finished examples (your format and quality target)

## `references/login.md`

```markdown
# Login

Platforms: Mobile, Website (Web app not yet ingested; treat as the same intent with browser-specific mechanics noted inline)
Tier: Common — assume it applies unless the product genuinely has no user accounts (e.g. a public tool or content-only site).

Everything a returning user needs to authenticate quickly and securely. Note the related but separate "Sign up" pattern (new-account creation) — not covered here.

- [ ] **Primary credential fields** — Email/username + password, or a passwordless method, as the main path.
- [ ] **Social/SSO sign-in** — "Continue with Apple" / "Continue with Google" (and SAML/SSO for B2B products) so most users never type a password at all.
- [ ] **Password field with visibility toggle** — Masked by default, with an option to reveal what was typed.
- [ ] **Credential autofill** — Supports the platform's password manager: on web, `autocomplete="username"` on the identifier field and `autocomplete="current-password"` on the password field (`new-password` is for signup/change, not sign-in) per [MDN's autocomplete reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete); on iOS, the matching `textContentType`; on Android, participation in Autofill Framework/Credential Manager. Never set `autocomplete="off"` on these fields — most browsers ignore it for password managers anyway, but it still blocks some assistive tools.
- [ ] **Password field accepts paste** — Never block pasting into the password field; it's how password managers and browser-generated passwords get in. [GOV.UK's password guidance](https://design-system.service.gov.uk/patterns/passwords/) calls this out directly as a common, avoidable mistake.
- [ ] **Biometric re-authentication (mobile)** — Face ID/Touch ID or Android's biometric prompt for a user who has already authenticated once with a password, so they aren't retyping it every launch.
- [ ] **Passkey support** — WebAuthn/passkey sign-in as a phishing-resistant alternative to password (+2FA); increasingly the expected option for security-conscious products, not just a "nice to have" anymore. Also the cleanest way to satisfy [WCAG 2.2 SC 3.3.8, Accessible Authentication](https://w3c.github.io/wcag/understanding/accessible-authentication.html): no step in authentication may require memorizing or transcribing something (a password, an SMS code) unless an alternative that doesn't is also offered.
- [ ] **Forgot-password recovery** — Leads to a reset flow that does not reveal whether a given email is registered (anti-enumeration) — a generic "if that account exists, we sent a link" message rather than "no account found."
- [ ] **Passwordless sign-in (magic link)** — An alternative that emails a one-time sign-in link, useful for users who haven't set up biometrics or a passkey.
- [ ] **Non-revealing error states** — Distinguishes "check your credentials" without confirming which field was wrong, for the same anti-enumeration reason as password reset, while still being clear enough to be useful.
- [ ] **Rate limiting / lockout feedback** — After repeated failed attempts, the user sees a cooldown message rather than a silent, unexplained block. A CAPTCHA is a common choice here but is itself a cognitive-function test under WCAG 2.2 SC 3.3.8 ("solve a puzzle") — pair it with a non-puzzle alternative (e.g. an email link) if this needs to stay accessible.
- [ ] **Persistent session** — "Remember me" or platform-appropriate session persistence, so the user isn't forced to log in on every app launch or browser visit.
- [ ] **Sign-up path for new users** — A visible link to account creation for visitors who land on login without an account yet.
- [ ] **(Mobile) Keyboard handling** — Correct keyboard type for the email field, "Next" advancing focus straight to the password field, and "Go"/"Done" submitting the form.

## Notes

Passkeys and magic links both reduce the load on password-reset support flows — worth prioritizing on products where "forgot password" tickets are a known support cost.
```

## `references/billing.md`

```markdown
# Billing

Platforms: Web app, Mobile, Website
Tier: Common — assume it applies unless the product picture shows it's free or sales-led; state the reason when excluding it.

Where users see what they're being charged, when, and manage payment methods, invoices, and the subscription lifecycle. Merged here from three previously separate, drifting notes (Mobile, Web app, Website) — most items apply everywhere; a few are called out as platform-specific.

- [ ] **Current plan and next billing date/amount** — Visible without digging into history. Show the plan name next to the amount, not just a number.
- [ ] **Payment method on file** — Shown with masked details (e.g. card brand + last 4 digits). Never display a full card number.
- [ ] **Add or update payment method** — A flow to add a new method or change the default one, separate from viewing billing history.
- [ ] **Billing history with downloadable invoices/receipts** — Past charges listed, each with a downloadable PDF. "Receipt" reads more natural on mobile; "invoice" on web/B2B.
- [ ] **Invoice legal fields** — Company name, address, and VAT/Tax ID included where legally required (EU VAT, UK, Brazil NF-e, and similar regimes). Missing these blocks business customers from expensing the charge.
- [ ] **Tax/VAT shown as a separate line** — Not folded silently into the total; shown on both the checkout preview and the final invoice.
- [ ] **Promo or discount code field** — A place to apply a coupon and see it reflected in the next charge, not only at initial checkout.
- [ ] **Failed payment recovery** — High-visibility messaging with a direct action to update the payment method. Consider a grace period (dunning) before hard-locking the account, since immediate lockout on a single failed card is a common source of churn.
- [ ] **Billing contact email** — Where invoices and payment-failure notices are sent. On team plans this is often different from the account owner's login email — worth a dedicated field.
- [ ] **Refund path** — A link or explanation of how to request a refund: through the platform's own process for in-app purchases (Apple/Google), or through support/self-service for direct web billing.
- [ ] **Plan change (upgrade/downgrade)** — A clear path to change plans, with proration explained before the user confirms.
- [ ] **Cancellation flow reachable without contacting support** — Regulators (FTC "click-to-cancel" rule, EU consumer law) increasingly require cancellation to be at least as easy as sign-up; a "call us to cancel" flow is a compliance risk in some jurisdictions, not just a UX one.
- [ ] **Usage-based billing, if the plan is metered** — Current usage shown against the included quota before the invoice generates, not only after the charge lands.
- [ ] **(Mobile) Subscription managed via App Store/Play Store** — For in-app-purchase subscriptions, link out to the platform's own subscription-management screen rather than intercepting cancellation in-app; required by [Apple's App Store Review Guideline 3.1.1](https://developer.apple.com/app-store/review/guidelines/), not just a convention.
- [ ] **(Mobile) Restore purchases** — A button to re-link an existing subscription after reinstalling the app or switching devices. Mandatory, not optional, for any app with non-consumable purchases or auto-renewing subscriptions per Guideline 3.1.1 — its absence is a common rejection reason.
- [ ] **(Mobile) Required subscription disclosures shown before the ask** — Title, length, and price of the auto-renewing subscription, plus working links to the privacy policy and terms of use, all visible before the user is asked to subscribe (Guideline 3.1.1's binder of required pre-purchase information).

## Notes

If the product sells through both a direct web checkout and mobile in-app purchase, the price and plan names should match across both — a common source of support tickets is a user who subscribed on the web being confused why the "same" plan looks different in the app (or vice versa).
```

Notice what these two files actually do: roughly 6–16 items each, every item is one to three sentences, at least 2–3 items per file cite a specific named standard with a real linkable source rather than a vague "follow best practices," platform-specific nuance is marked inline with `(Mobile)` or folded into the sentence rather than split into a separate section, and the closing `## Notes` is used sparingly — only for one thing that doesn't fit as a checkbox, omitted entirely if there's nothing that qualifies.

# Exact format every output file must follow

```markdown
# <Pattern Name — exactly as given in the pattern list below, do not rename it>

Platforms: <comma-separated, exactly as given in the pattern list below>
Tier: <Fundamental | Common | Conditional — exactly as given> — <one clause stating the default assumption and what would flip it, in the same voice as the two examples' Tier lines>

<One to two sentences defining what this screen/moment is and when a product has one. Third person, no marketing language.>

- [ ] **<Item name, 2-6 words>** — <1-3 sentences: what it is, why it matters or what failure it prevents, platform nuance inline if relevant, a real citation if you have one>
- [ ] **<repeat, aim for 6-14 items — match the density of the source material below, don't pad and don't truncate>**

## Notes

<Optional. One paragraph, only if there's a cross-cutting caveat that doesn't fit as a checkbox item. Omit this whole section — heading included — if there's nothing that qualifies.>
```

Rules that are easy to get wrong:
- No YAML frontmatter. The `# Title`, `Platforms:` line, and `Tier:` line are plain Markdown text, not a metadata block.
- The `Tier` value must match exactly what's given in the pattern list below — you are not re-deriving tiers, they're already decided.
- Every checkbox uses `- [ ]`, never `- [x]` and never a plain bullet.
- Item names are bolded with `**`, the description follows an em dash `—` (not a hyphen, not a colon).
- Write in **American English** even when the source material or a cited standard (e.g. GOV.UK) uses British spelling.

# Where the content comes from — and the one rule that matters most

The 57 patterns below started from the maintainer's own curated notes on what each pattern already knows to check (not included in this repo — internal working material, not a public source). Treat that the way the two finished examples above were built: don't invent a checklist from a pattern's name alone, and don't stop at a thin restatement of the definition ("confirms the save happened") — add the real substance a competent developer would actually need, the same way the original thin drafts of Billing/Login became the two files above. If you're extending this list with a pattern that isn't already covered, ground it the same way: real product knowledge of what that screen or flow typically gets wrong, verified against the standards below, not a generic template filled in from the pattern's name.

**Do not invent a specific standard, guideline number, or URL you are not confident is real.** A wrong citation is worse than no citation — it teaches the agent using this file something false with the appearance of authority. If you know the general principle but not a specific citable source, state the principle plainly (the way most items in the two examples above do, with no citation at all) rather than attaching a fabricated one. Only cite when you would bet on the citation being checkable and correct.

When you do have a real citation to add, prioritize pulling from:
- **WCAG / WAI** (`w3c.github.io/wcag/understanding/`, `w3.org/WAI/`) — for anything involving forms, authentication, status/error communication, or color-only signals. WCAG 2.2's Accessible Authentication (3.3.8) and target-size criteria are especially relevant across many patterns here, not just Login.
- **MDN** (`developer.mozilla.org`) — for exact HTML attributes, input types, ARIA roles, and browser API names (autocomplete values, input `type`, `aria-live`, etc.).
- **Apple Human Interface Guidelines** (`developer.apple.com/design/human-interface-guidelines/`) and **App Store Review Guidelines** (`developer.apple.com/app-store/review/guidelines/`) — for iOS-specific mobile patterns (tap target sizes, native components like MapKit, in-app purchase rules).
- **Material Design** (`m3.material.io`) — for the Android-side equivalent wherever you'd otherwise only give the iOS number (e.g. tap target size: Apple says 44×44pt, Material says 48×48dp — give both where a pattern lists one already, since the existing `sections/sidekick.md` index flags this exact gap for Tab Bar Navigation).
- **GOV.UK Design System** (`design-system.service.gov.uk/patterns/`) — for plain-language content patterns, form design, and anything about passwords, error messages, or confirmation pages. Its patterns are unusually specific and battle-tested; several apply directly (Contact Us, FAQ, Sign up, Showing input error).

Not every item needs a citation — the two examples above cite maybe a quarter of their items. Forcing a citation onto every line produces the same generic-filler problem as having none.

# The judgment-calls system (why Tier exists, so your Tier clause is consistent)

- **Fundamental** — assume it applies to virtually every product in its section; excluding it needs a stated, unusual reason. Several Fundamental patterns here are legal/accessibility floors (Privacy, Security, 404, Showing input error, Deleting account), not style choices — write their Tier clause and content with that weight.
- **Common** — assume it applies unless the product's own context clearly rules it out (a free product doesn't need Billing; a product with no teams doesn't need Verifying account via a second contact method). Most patterns are this tier.
- **Conditional** — assume it does **not** apply until a specific, narrower capability is confirmed present, not just plausible in general. Don't write these as if every product needs them — the Tier clause should name the specific capability that would make it apply (e.g. Cart's is "until a multi-item purchase flow is confirmed," not just "if the product sells things," which is Billing's bar, not Cart's).

# Pattern names stay industry-standard — do not rename them

An earlier pass tried giving every pattern an original, branded name (Login → "Welcome Back," Cart → "The Basket") and it was reverted: renaming terms as universally recognized as "Login" or "Cart" costs the agent a translation step for no benefit. Use every pattern name exactly as written in the list below. (The four *section* names — Sidekick, Control Room, Storefront, Choreography — are intentionally original and already decided; you won't need to touch those, just know they exist as the `Platforms` groupings below.)

# The 57 patterns to write

One file per row, at `references/<file>`. `Platforms` values below use the section's plain name, not its original section name (mobile app / web app / website / flow) — same convention as the two finished examples.

## Cross-cutting (appears in more than one section — write once, still one file)

| Pattern | Tier | Platforms | File |
|---|---|---|---|
| Account | Common | Mobile, Web app | `references/account.md` |
| Settings | Common | Mobile, Web app | `references/settings.md` |
| Search | Conditional | Mobile, Website | `references/search.md` |
| Cart | Conditional | Mobile, Website | `references/cart.md` |

## Mobile app only

| Pattern | Tier | File |
|---|---|---|
| Gesture navigation | Common | `references/gesture-navigation.md` |
| Splash Screen | Fundamental | `references/splash-screen.md` |
| Checkout | Common | `references/checkout.md` |
| Tab Bar Navigation | Common | `references/tab-bar-navigation.md` |
| In-App Notifications | Common | `references/in-app-notifications.md` |
| Action Sheet | Common | `references/action-sheet.md` |
| Camera | Conditional | `references/camera.md` |
| Map View | Conditional | `references/map-view.md` |
| Onboarding Checklist | Conditional | `references/onboarding-checklist.md` |
| Paywall | Conditional | `references/paywall.md` |
| Onboarding | Common | `references/onboarding.md` |
| Chat | Conditional | `references/chat.md` |
| In-App Browser | Conditional | `references/in-app-browser.md` |
| Invite | Conditional | `references/invite.md` |

(Platforms line for all of the above: `Mobile`)

## Web app only

| Pattern | Tier | File |
|---|---|---|
| 2FA | Common | `references/2fa.md` |
| Notification Settings | Common | `references/notification-settings.md` |
| Help Center | Common | `references/help-center.md` |
| User Management | Conditional | `references/user-management.md` |
| Single Item Detail | Common | `references/single-item-detail.md` |
| Admin Panel | Conditional | `references/admin-panel.md` |
| Empty State | Fundamental | `references/empty-state.md` |

(Platforms line for all of the above: `Web app`)

## Website only

| Pattern | Tier | File |
|---|---|---|
| Security | Fundamental | `references/security.md` |
| About | Common | `references/about.md` |
| Privacy | Fundamental | `references/privacy.md` |
| Features | Common | `references/features.md` |
| Testimonials | Common | `references/testimonials.md` |
| Affiliate | Conditional | `references/affiliate.md` |
| Compare | Conditional | `references/compare.md` |
| Status | Common | `references/status.md` |
| Press / Media | Conditional | `references/press-media.md` |
| Waitlist | Conditional | `references/waitlist.md` |
| Team | Common | `references/team.md` |
| Careers | Conditional | `references/careers.md` |
| Blog Post | Conditional | `references/blog-post.md` |
| Contact Us | Fundamental | `references/contact-us.md` |
| Pricing | Common | `references/pricing.md` |
| FAQ | Common | `references/faq.md` |
| 404 | Fundamental | `references/404.md` |
| Blog | Conditional | `references/blog.md` |
| Sign up | Common | `references/sign-up.md` |

(Platforms line for all of the above: `Website`)

## Flow only (cross-screen interaction moments, not whole screens)

| Pattern | Tier | File |
|---|---|---|
| Adding to cart | Conditional | `references/adding-to-cart.md` |
| Uploading media | Conditional | `references/uploading-media.md` |
| Verifying account | Common | `references/verifying-account.md` |
| Canceling subscription | Conditional | `references/canceling-subscription.md` |
| Filtering items | Conditional | `references/filtering-items.md` |
| Saving changes | Fundamental | `references/saving-changes.md` |
| Entering promo code | Conditional | `references/entering-promo-code.md` |
| Showing input error | Fundamental | `references/showing-input-error.md` |
| Resetting password | Common | `references/resetting-password.md` |
| Deleting account | Fundamental | `references/deleting-account.md` |
| Contacting support | Common | `references/contacting-support.md` |
| Making a card payment | Common | `references/making-a-card-payment.md` |
| Submitting a form | Fundamental | `references/submitting-a-form.md` |

(Platforms line for all of the above: `Flow`. These are interaction moments, not screens — e.g. "Resetting password" is a sub-flow of the Login pattern above, and "Deleting account" of the Account pattern above, but they stay in separate files for now; don't merge them or cross-reference between a Flow file and a screen file.)

# Before you finish

For each of the 57 files, check:
1. Does the `Tier` line match the table exactly, and does its clause name a real, specific condition (not "if applicable")?
2. Is every item something a competent developer could be wrong about — not a restatement of the pattern's own definition?
3. If you added a citation, would you bet money it resolves to a real page saying what you claim?
4. Would this file, dropped next to `login.md` and `billing.md` with no introduction, read like it was written by the same author?

Output: 57 Markdown files, one per row above, at the exact paths given. Nothing else — no changes to any other file in this project.
