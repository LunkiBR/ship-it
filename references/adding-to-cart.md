# Adding to cart

Platforms: Flow
Tier: Conditional — assume it does not apply until an item selection and cart addition moment is confirmed present.

The micro-interaction moment where a user selects item variants and adds a product to their shopping cart.

- [ ] **Explicit variant selection validation** — Ensuring required options (size, color, tier) are selected before enabling cart addition.
- [ ] **Prominent primary CTA button** — Dominant "Add to Cart" button positioned cleanly within viewport on product detail views.
- [ ] **Immediate confirmation feedback** — Visual confirmation state (mini-cart drawer opening, toast banner, button state checkmark) confirming addition without full page reload.
- [ ] **Accessible mini-cart / navigation counter** — Cart badge counter updating dynamically with `aria-live="polite"` feedback (WCAG 2.1 SC 4.1.3, Status Messages).
- [ ] **Out-of-stock handling** — Disabling CTA and displaying clear "Out of Stock" status when selected variant inventory is zero.
