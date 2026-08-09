# Saving changes

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every form edit interaction; state the reason if excluding it.

The state feedback flow accompanying form edits, setting persistence, and content modification.

- [ ] **Disabled save state** — Save action button disabled or hidden until a field is edited from its original value.
- [ ] **Active save indicator** — Save button transitioning to active visual state as soon as form values change.
- [ ] **Loading spinner on submit** — Save button displaying inline loading spinner and `aria-disabled="true"` while API call is in-flight.
- [ ] **Explicit save notification** — Accessible confirmation message (toast or inline notification with `role="status"`) confirming edits were saved.
- [ ] **Unsaved changes navigation warning** — Prompting a warning modal if the user attempts to navigate away with dirty unsaved form fields.
