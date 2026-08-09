# Showing input error

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every form input; state the reason if excluding it.

The validation flow detecting invalid form inputs and communicating errors accessibly to the user.

- [ ] **Post-blur field validation** — Validating field criteria after focus leaves the input, avoiding annoying errors while the user is actively typing. Validating on every keystroke instead reads as the system scolding the user before they've finished.
- [ ] **Accessible error messaging** — Linking error text to input fields using `aria-invalid="true"` and `aria-describedby="error-id"` (WCAG 2.1 SC 3.3.1, Error Identification).
- [ ] **Multi-modal error signals** — Combining red border colors with clear error text and warning icons (WCAG 2.1 SC 1.4.1, Use of Color).
- [ ] **Constructive error suggestions** — Providing specific instructions on how to fix the error (WCAG 2.1 SC 3.3.3, Error Suggestion).
- [ ] **Error clearing on re-focus** — Resetting field error styling while the user edits the field to correct values.
