# Checkout

Platforms: Mobile
Tier: Common — assume it applies unless the product has no mobile monetary transactions; state the reason when excluding it.

The mobile payment flow optimized for native digital wallet methods, small-screen input constraints, and quick order completion.

- [ ] **Native wallet payments** — Apple Pay and Google Pay offered as top-tier primary checkout actions for single-tap biometric confirmation.
- [ ] **Manual card entry fallback** — Form interface for credit and debit card entry when native digital wallets are unavailable or declined.
- [ ] **Persistent order summary** — Collapsible order summary showing line items, quantities, and final price throughout all checkout steps.
- [ ] **Minimal form fields** — Requesting only essential shipping and billing details, avoiding redundant fields.
- [ ] **Platform autofill support** — Input fields configured with iOS `textContentType` and Android Autofill hints for single-tap address completion.
- [ ] **Keyboard type optimization** — Numeric keypads for card numbers (`keyboardType="number-pad"`), expiration dates, and security codes (CVV), plus `autocorrect="off"`, `autocapitalize="off"`, and `novalidate` on these fields so the OS doesn't fight the input.
- [ ] **Guest checkout as the prominent option** — "Continue as guest" shown at least as prominently as "Create an account," not buried below it or requiring a second screen — forcing account creation before purchase is a common, avoidable cause of checkout abandonment.
- [ ] **Multi-step progress tracking** — Clear step indicator (e.g. Shipping → Payment → Confirm) on multi-screen checkout workflows.
- [ ] **Payment failure recovery** — Returning users to the payment step with entered data preserved and a clear error explanation upon payment decline.
- [ ] **Order confirmation view** — Dedicated confirmation screen displaying order number, summary, payment method, and estimated delivery dates.
