# Search

Platforms: Mobile, Website
Tier: Conditional — assume it does not apply until a search capability or large content catalog is confirmed present.

The search interface helping users locate specific content, products, or pages quickly across mobile and website surfaces.

- [ ] **Prominent search input** — Easily locatable search field with descriptive placeholder text, clear search icon, and adequate target size.
- [ ] **Autocomplete and live suggestions** — Real-time query suggestions updating as the user types, debouncing network calls to prevent interface stutter.
- [ ] **Live result updates** — Results updating dynamically without requiring an explicit form submit action.
- [ ] **Query retention in input** — Active query string retained in the input field to facilitate immediate refining or correction.
- [ ] **Clear query button** — Single-tap clear icon (`aria-label="Clear search query"`) inside the input field to reset text instantly.
- [ ] **Recent search history** — Displaying recent search queries before typing starts, with options to clear history items.
- [ ] **Helpful no-results state** — Informative empty state offering spelling corrections, broader query suggestions, or category navigation links when zero items match.
- [ ] **Keyboard and focus accessibility** — Automatic soft keyboard focus on mobile search screens; full keyboard navigation for web autocomplete dropdowns per [WCAG 2.1 SC 2.1.1, Keyboard Access](https://w3c.github.io/wcag/understanding/keyboard.html).
- [ ] **(Mobile) Sticky search bar & bottom sheet filters** — Fixed search bar at top of viewport with filter controls accessible via bottom sheet overlay.

## Notes

Autocomplete suggestions should prioritize exact matches first, followed by popular categories or recent search history.
