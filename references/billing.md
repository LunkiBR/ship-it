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
- [ ] **(Mobile) Subscription managed via App Store/Play Store** — For in-app-purchase subscriptions, link out to the platform's own subscription-management screen rather than intercepting cancellation in-app; required by Apple App Store Review Guideline 3.1.1, not just a convention.
- [ ] **(Mobile) Restore purchases** — A button to re-link an existing subscription after reinstalling the app or switching devices. Mandatory, not optional, for any app with non-consumable purchases or auto-renewing subscriptions per Guideline 3.1.1 — its absence is a common rejection reason.
- [ ] **(Mobile) Required subscription disclosures shown before the ask** — Title, length, and price of the auto-renewing subscription, plus working links to the privacy policy and terms of use, all visible before the user is asked to subscribe (Guideline 3.1.1's binder of required pre-purchase information).

## Notes

If the product sells through both a direct web checkout and mobile in-app purchase, the price and plan names should match across both — a common source of support tickets is a user who subscribed on the web being confused why the "same" plan looks different in the app (or vice versa).
