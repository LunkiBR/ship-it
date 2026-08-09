# Splash Screen

Platforms: Mobile
Tier: Fundamental — assume it applies to virtually every mobile app to cover cold launch initialization; state the reason if excluding it.

The initial launch screen displayed while the mobile application bootstraps core frameworks, authenticates session tokens, and renders the primary view.

- [ ] **Centered brand logo** — Clean, high-resolution brand logo or wordmark centered on a uncluttered background.
- [ ] **Brand-aligned background** — Solid background color or subtle brand styling eliminating visual flash during transition from the mobile OS home screen.
- [ ] **Minimal launch duration** — Displayed strictly for necessary technical cold-start setup; never artificially delayed for marketing display.
- [ ] **Smooth view transition** — Intentional fade or slide transition to the main interface avoiding jarring cuts or screen flashes.
- [ ] **Non-interactive layout** — Completely free of buttons, form inputs, or clickable elements, serving strictly as a visual loading bridge.
- [ ] **Loading indicator for long cold starts** — Visual progress bar or activity spinner displayed if initialization exceeds 1 second.
- [ ] **Dark mode launch support** — Separate launch screen storyboard assets configured for light and dark system appearance settings.

## Notes

On iOS, launch storyboards should match the structural layout of the main landing screen to create a seamless app open animation.
