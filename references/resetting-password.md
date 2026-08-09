# Resetting password

Platforms: Flow
Tier: Common — assume it applies unless the product has no password authentication; state the reason when excluding it.

The self-serve recovery flow allowing users to regain access to their account after forgetting their password.

- [ ] **Accessible forgot password link** — Styled link positioned adjacent to the password field, working the same way on mobile as on desktop rather than being a desktop-only affordance.
- [ ] **Identifier request step** — Input field requesting account email address, prefilled if previously entered on login.
- [ ] **Anti-enumeration confirmation state** — Generic success message ("If an account exists for that email, we sent a reset link") preventing email harvesting.
- [ ] **Instructions email delivery** — Email containing secure, time-limited reset link or single-use verification code.
- [ ] **New password form with strength guidance** — Password input field enforcing security criteria with live strength meter.
- [ ] **Reset success & login redirection** — Clear confirmation state redirecting user directly to login with prefilled email.
