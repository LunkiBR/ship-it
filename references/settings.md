# Settings

Platforms: Mobile, Web app
Tier: Common — assume it applies unless the product has no configurable preferences or user accounts; state the reason when excluding it.

The central control hub where users manage account details, preferences, notification channels, application behavior, and legal disclosures.

- [ ] **Categorized section layout** — Grouped into clear visual categories (Account, Notifications, Security, Appearance, Support) to make preferences scannable.
- [ ] **User identity header** — Displaying active avatar, display name, and primary email address at the top of the main settings screen.
- [ ] **Platform-native toggle controls** — Using platform-native switch controls: on iOS `UISwitch`, on Android `Switch`, and on web accessible toggle controls with `aria-checked`.
- [ ] **Immediate-effect toggle behavior** — A toggle applies its new state the instant it's flipped; it never waits for a separate Save/Submit action, and its label describes what turning it *on* does rather than reading as a neutral yes/no.
- [ ] **Security & authentication shortcuts** — Direct links to update passwords, manage two-factor authentication (2FA), and view active device sessions.
- [ ] **Notification preference navigation** — Pathways to channel-specific notification controls (email, push, in-app) organized by category.
- [ ] **Appearance and regional settings** — Controls for theme selection (Light, Dark, System default), language, timezone, and date/number formats.
- [ ] **Danger zone isolation** — Destructive actions (sign out, data export, account deletion) visually isolated at the bottom with red warning cues.
- [ ] **Support and feedback access** — Direct pathways to contact customer support, submit product feedback, or open help center documentation.
- [ ] **Legal links and app build version** — Visible links to Privacy Policy and Terms of Service, along with current build and version numbers for customer support troubleshooting.

## Notes

When organizing settings, prioritize grouping by user task frequency rather than internal engineering architecture.
