# Account

Platforms: Mobile, Web app
Tier: Common — assume it applies unless the product genuinely has no user accounts (e.g. a public tool or content-only site); state the reason when excluding it.

Where users view and manage their personal profile, authentication credentials, linked social accounts, and account lifecycle. Merged here from mobile and web app notes into one unified reference.

- [ ] **Profile picture upload & fallback** — Form to upload or update profile avatar, with sensible fallback (e.g., user initials on solid background) for accounts without custom images.
- [ ] **Display name and identifier** — Editable fields for public display name, username, or job title, with clear distinction between public labels and internal account identifiers.
- [ ] **Email address management** — Current email displayed with option to update, triggering a verification link to the new address before replacing the existing contact detail.
- [ ] **Password change flow** — Dedicated interface to change passwords requiring confirmation of the current password first to prevent unauthorized session hijacking.
- [ ] **Linked third-party accounts** — Overview of connected OAuth providers (Google, Apple, SAML SSO) with options to link or disconnect, blocking disconnection if it is the account's sole authentication method.
- [ ] **Save confirmation feedback** — Clear feedback that profile updates were saved, using inline notifications or accessible toasts with `role="status"` per [WCAG 2.1 SC 4.1.3, Status Messages](https://w3c.github.io/wcag/understanding/status-messages.html).
- [ ] **Account deactivation vs deletion** — Clearly separated options for temporary deactivation and permanent account deletion, with explicit explanations of data impact.
- [ ] **(Mobile) In-app account deletion path** — Direct pathway to initiate account deletion inside the app, required by [Apple's App Store Review Guideline 5.1.1(v)](https://developer.apple.com/app-store/review/guidelines/#account-deletion) for any app supporting account creation.

## Notes

Auto-saving profile changes works well on web app interfaces, but explicit save buttons remain standard on mobile to prevent accidental field updates during scrolling.
