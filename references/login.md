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
