# Action Sheet

Platforms: Mobile
Tier: Common — assume it applies to mobile apps offering contextual secondary actions or selection menus; state the reason when excluding it.

A modal sheet sliding up from the screen bottom to present context-specific actions or confirm user choices.

- [ ] **Descriptive header** — Optional title and message providing context for the presented choices.
- [ ] **Backdrop dimming and dismissal** — Dimmed background overlay where tapping outside or swiping down dismisses the sheet without triggering actions.
- [ ] **Destructive action styling** — Destructive choices styled in red, placed at the bottom or visually separated from safe options.
- [ ] **Explicit cancel button** — Dedicated "Cancel" button allowing safe closure on both iOS and Android.
- [ ] **Expandable snap points** — Defined stop heights (half-sheet, full-sheet) with drag handle indicator when sheet contents are expandable.
- [ ] **Scrollable content container** — Fixed action buttons while internal list content scrolls when options exceed sheet height.
- [ ] **Keyboard avoid behavior** — Sheet position and height dynamically adjusting when text input within the sheet brings up the soft keyboard.
