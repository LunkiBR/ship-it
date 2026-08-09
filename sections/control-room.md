# Control Room (in-product web app) — pattern index

10 patterns. Open a pattern's file only once it's the one actually in scope. Tier fixes the default assumption before weighing product context — see `SKILL.md`'s Judgment calls for what Fundamental/Common/Conditional mean and the full workflow.

| Pattern | Tier | Covers | File |
|---|---|---|---|
| 2FA | Common | Setting up or completing two-factor authentication | [../references/2fa.md](../references/2fa.md) |
| Notification Settings | Common | Which notifications arrive, through which channel, how often | [../references/notification-settings.md](../references/notification-settings.md) |
| Account | Common | Personal profile, credentials, account-level details | [../references/account.md](../references/account.md) |
| Help Center | Common | Self-serve documentation hub | [../references/help-center.md](../references/help-center.md) |
| Billing | Common | Payment methods, invoices, subscription lifecycle, cancellation | [../references/billing.md](../references/billing.md) |
| Settings | Common | Central hub for account/notification/app-behavior preferences | [../references/settings.md](../references/settings.md) |
| User Management | Conditional | Admin view for inviting/managing workspace users | [../references/user-management.md](../references/user-management.md) |
| Single Item Detail | Common | Full-detail view of one record from a list | [../references/single-item-detail.md](../references/single-item-detail.md) |
| Admin Panel | Conditional | Admins manage users, org settings, account-wide activity | [../references/admin-panel.md](../references/admin-panel.md) |
| Empty State | Fundamental | What a screen shows when there's no data yet | [../references/empty-state.md](../references/empty-state.md) |

Login isn't listed here yet — the Web App source note hasn't ingested its own Login pattern. Once it does, it'll join Sidekick and Storefront as a third section resolving to [../references/login.md](../references/login.md), tiered Common like it is elsewhere.
