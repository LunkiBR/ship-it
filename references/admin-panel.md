# Admin Panel

Platforms: Web app
Tier: Conditional — assume it does not apply until system administration or organization management capabilities are confirmed present.

The high-level administration suite for platform owners to oversee users, system settings, billing, and security audit logs.

- [ ] **Role-gated route security** — Strict server-side and client-side access control restricting view access to admin roles.
- [ ] **Global user administration** — Directory of all system accounts with controls to manage roles, reset 2FA, or freeze access.
- [ ] **Organization & domain settings** — Controls for configuring SSO SAML, custom domains, and workspace branding.
- [ ] **System usage overview** — High-level metric dashboards tracking API calls, storage usage, and active seats.
- [ ] **Organization billing control** — Centralized view of invoices, contract terms, seat counts, and payment methods.
- [ ] **Comprehensive audit log** — Immutable log recording security events, permission modifications, and admin actions.
- [ ] **Typed confirmation danger zone** — Requiring typed confirmation (e.g. typing the workspace name) reserved for the single most destructive, rarest action here (deleting the workspace), not applied to every delete button — overusing this pattern turns it into a rote click that stops protecting anything.
