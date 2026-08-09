# Gesture navigation

Platforms: Mobile
Tier: Common — assume it applies to touch-based mobile applications unless the UI relies entirely on explicit button controls; state the reason when excluding it.

Touch-based interaction patterns that let users navigate, manipulate content, and perform actions fluidly without relying solely on visible buttons.

- [ ] **Swipe to go back** — Interactive edge swipe gesture to return to the previous screen, disabled selectively on views with horizontal carousels to avoid gesture conflicts.
- [ ] **List item swipe actions** — Swiping left or right on list items to reveal quick actions (delete, archive, mark read), restricted to 2–3 actions maximum with high-contrast icons.
- [ ] **Pull to refresh** — Downward pull gesture on scrollable list views displaying a loading indicator and triggering haptic confirmation upon refresh trigger.
- [ ] **Long-press contextual menus** — Press-and-hold gesture opening contextual menus, with all menu options also accessible through explicit tap targets for accessibility.
- [ ] **Pinch to zoom** — Multi-touch pinch gesture for images and maps, automatically resetting zoom scale upon leaving the view.
- [ ] **Drag to reorder** — Long-press-to-lift followed by drag interaction for reordering list items or grid cards, accompanied by visual elevation and tactile feedback.
- [ ] **Subtle gesture hints** — Subtle visual animation or tooltip introducing key custom gestures during first-time feature usage.
- [ ] **Tactile haptic feedback** — Haptic feedback triggered during finger-obscured moments like pull-to-refresh releases, drag-reorder snaps, or destructive swipe thresholds.

## Notes

Custom gestures should enhance speed for power users but never serve as the sole method to perform critical actions.
