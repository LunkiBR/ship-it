# Making a card payment

Platforms: Flow
Tier: Common — assume it applies unless the product accepts no direct credit card payments; state the reason when excluding it.

The transaction flow for collecting, validating, processing, and confirming credit or debit card payments.

- [ ] **Form fields for card details** — Input fields for Card Number, Expiration Date, CVV, and Billing Zip Code.
- [ ] **Client-side Luhn validation** — Validating card number formatting and expiration dates before sending API request.
- [ ] **In-flight processing state** — Displaying full overlay or button loading spinner to prevent double submission while payment processes.
- [ ] **Clear transaction success state** — Immediate confirmation view confirming funds were charged with receipt details.
- [ ] **Detailed payment error handling** — Specific messages for declined cards, insufficient funds, or expired cards without exposing raw gateway errors.
