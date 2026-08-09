# Verifying account

Platforms: Flow
Tier: Common — assume it applies unless account creation requires zero identity verification; state the reason when excluding it.

The verification moment where a user confirms ownership of their email address or phone number during onboarding.

- [ ] **Clear verification trigger** — Explaining clearly why verification is required and displaying the exact email address or phone number used.
- [ ] **Verification code input** — Digit input fields supporting autofill (`autocomplete="one-time-code"` on web/iOS) allowing single-tap OTP insertion.
- [ ] **Resend code mechanism** — Visible option to request a new code with a countdown timer preventing API spam.
- [ ] **Actionable verification error states** — Specific error messages for expired codes, incorrect digits, or rate-limited attempt lockouts.
- [ ] **Verification success transition** — Instant visual confirmation upon valid code entry, automatically advancing the user to the next step.
