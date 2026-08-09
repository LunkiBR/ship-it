# Tab Bar Navigation

Platforms: Mobile
Tier: Common — assume it applies to mobile apps with multi-section top-level navigation; state the reason when excluding it.

The persistent bottom navigation bar providing single-tap access to 3–5 top-level sections of a mobile application.

- [ ] **Strict tab count limit** — Restricted to 3 to 5 primary destinations to prevent visual clutter and mis-taps.
- [ ] **Icon and text label pairing** — Every tab item pairing an intuitive icon with a concise text label for accessibility and clarity.
- [ ] **Distinct active state** — Visually distinct selected state using brand accent color, filled icon variants, or heavy font weight.
- [ ] **Real-time badge counts** — Subtle numerical or dot badges for tabs with unread alerts, updating dynamically without full screen reloads.
- [ ] **Persistent presence** — Remains visible across main view hierarchies; hidden automatically in deep detail screens or modal workflows.
- [ ] **Accessible touch targets** — Minimum tap target area of 44×44pt on iOS per [Apple's Human Interface Guidelines on layout](https://developer.apple.com/design/human-interface-guidelines/layout) and 48×48dp on Android per [Material Design accessibility guidelines](https://m3.material.io/foundations/accessibility/accessibility-checklist).
- [ ] **Selection haptic feedback** — Light haptic tap upon switching active tabs to confirm selection.
