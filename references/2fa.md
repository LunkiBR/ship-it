# 2FA

Platforms: Web app
Tier: Common — assume it applies unless the product has no password authentication or user accounts; state the reason when excluding it.

The setup and verification screens for two-factor authentication protecting user account access.

- [ ] **Multi-method support** — Offering TOTP authenticator apps (Google Authenticator, 1Password) alongside WebAuthn hardware keys or SMS fallback.
- [ ] **Step-by-step setup guide** — Clear multi-step wizard guiding TOTP pairing, QR code scan, and secret key entry.
- [ ] **QR code and secret key display** — Large, scannable QR code paired with a copyable textual secret key for manual entry.
- [ ] **Setup verification step** — Requiring entry of a valid 6-digit code before enabling 2FA, preventing lockouts from broken setups.
- [ ] **Single-use recovery codes** — Generating a set of emergency backup codes, requiring download/copy confirmation before finishing setup.
- [ ] **2FA active success state** — Clear confirmation indicating 2FA is active on the account.
- [ ] **Re-authentication before disable** — Mandatory password re-prompt before disabling or altering 2FA configurations.
