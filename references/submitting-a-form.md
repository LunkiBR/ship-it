# Submitting a form

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every web and mobile form; state the reason if excluding it.

The end-to-end submit lifecycle handling form validation, submission loading states, and success/error feedback.

- [ ] **Explicit submit button** — Prominent submit button with copy adapted to form intent ("Save changes", "Send message").
- [ ] **In-flight submit loading state** — Disabling submit button and displaying loading spinner during network request.
- [ ] **Accessible success feedback** — Displaying clear success notification or redirecting upon successful submission.
- [ ] **Comprehensive error handling** — Presenting top-level alert summary and focusing the first invalid input on submission failure per [WCAG 2.1 SC 3.3.1, Error Identification](https://w3c.github.io/wcag/understanding/error-identification.html).
- [ ] **Form state preservation** — Retaining user-entered form data upon submission failure so users do not have to retype information.
