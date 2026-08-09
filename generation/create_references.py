import os

references_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references")

files_data = {
    # ---------------------------------------------------------
    # Cross-cutting (4)
    # ---------------------------------------------------------
    "account.md": """# Account

Platforms: Mobile, Web app
Tier: Common — assume it applies unless the product genuinely has no user accounts (e.g. a public tool or content-only site); state the reason when excluding it.

Where users view and manage their personal profile, authentication credentials, linked social accounts, and account lifecycle. Merged here from mobile and web app notes into one unified reference.

- [ ] **Profile picture upload & fallback** — Form to upload or update profile avatar, with sensible fallback (e.g., user initials on solid background) for accounts without custom images.
- [ ] **Display name and identifier** — Editable fields for public display name, username, or job title, with clear distinction between public labels and internal account identifiers.
- [ ] **Email address management** — Current email displayed with option to update, triggering a verification link to the new address before replacing the existing contact detail.
- [ ] **Password change flow** — Dedicated interface to change passwords requiring confirmation of the current password first to prevent unauthorized session hijacking.
- [ ] **Linked third-party accounts** — Overview of connected OAuth providers (Google, Apple, SAML SSO) with options to link or disconnect, blocking disconnection if it is the account's sole authentication method.
- [ ] **Save confirmation feedback** — Clear feedback that profile updates were saved, using inline notifications or accessible toasts with `role="status"` per [WCAG 2.1 SC 4.1.3, Status Messages](https://w3c.github.io/wcag/understanding/status-messages.html).
- [ ] **Account deactivation vs deletion** — Clearly separated options for temporary deactivation and permanent account deletion, with explicit explanations of data impact.
- [ ] **(Mobile) In-app account deletion path** — Direct pathway to initiate account deletion inside the app, required by [Apple's App Store Review Guideline 5.1.1(v)](https://developer.apple.com/app-store/review/guidelines/#account-deletion) for any app supporting account creation.

## Notes

Auto-saving profile changes works well on web app interfaces, but explicit save buttons remain standard on mobile to prevent accidental field updates during scrolling.
""",

    "settings.md": """# Settings

Platforms: Mobile, Web app
Tier: Common — assume it applies unless the product has no configurable preferences or user accounts; state the reason when excluding it.

The central control hub where users manage account details, preferences, notification channels, application behavior, and legal disclosures.

- [ ] **Categorized section layout** — Grouped into clear visual categories (Account, Notifications, Security, Appearance, Support) to make preferences scannable.
- [ ] **User identity header** — Displaying active avatar, display name, and primary email address at the top of the main settings screen.
- [ ] **Platform-native toggle controls** — Using platform-native switch controls: on iOS `UISwitch`, on Android `Switch`, and on web accessible toggle controls with `aria-checked`.
- [ ] **Security & authentication shortcuts** — Direct links to update passwords, manage two-factor authentication (2FA), and view active device sessions.
- [ ] **Notification preference navigation** — Pathways to channel-specific notification controls (email, push, in-app) organized by category.
- [ ] **Appearance and regional settings** — Controls for theme selection (Light, Dark, System default), language, timezone, and date/number formats.
- [ ] **Danger zone isolation** — Destructive actions (sign out, data export, account deletion) visually isolated at the bottom with red warning cues.
- [ ] **Support and feedback access** — Direct pathways to contact customer support, submit product feedback, or open help center documentation.
- [ ] **Legal links and app build version** — Visible links to Privacy Policy and Terms of Service, along with current build and version numbers for customer support troubleshooting.

## Notes

When organizing settings, prioritize grouping by user task frequency rather than internal engineering architecture.
""",

    "search.md": """# Search

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
""",

    "cart.md": """# Cart

Platforms: Mobile, Website
Tier: Conditional — assume it does not apply until a multi-item purchase flow is confirmed present.

The pre-checkout shopping cart screen where users review selected items, adjust quantities, apply promotional discounts, and review price totals.

- [ ] **Itemized order list** — Each item displayed with thumbnail image, product title, selected variant options (size, color), unit price, and extended line total.
- [ ] **Quantity stepper controls** — Touch-friendly plus/minus controls or numeric inputs meeting accessible touch target guidelines (minimum 44×44pt on iOS, 48×48dp on Android) to adjust quantities without page reloads.
- [ ] **Item removal action** — Clear option to remove individual items from the cart, ideally paired with a brief undo toast notification.
- [ ] **Itemized price breakdown** — Clear summary listing subtotal, applied discounts, estimated shipping fees, taxes, and final grand total.
- [ ] **Promo code entry field** — Input field to enter discount codes with instant validation feedback and updated price calculations.
- [ ] **Prominent checkout CTA** — Visually dominant primary button leading directly into the payment checkout flow.
- [ ] **Empty cart state** — Informative state shown when cart contains zero items, featuring a clear CTA button returning to store browsing.
- [ ] **Continue shopping link** — Visible link or back action returning to catalog browsing without losing current cart state.
- [ ] **(Mobile) Swipe-to-remove gesture** — Left-swipe gesture on item cards revealing a quick destructive remove action.
""",

    # ---------------------------------------------------------
    # Mobile app only (14)
    # ---------------------------------------------------------
    "gesture-navigation.md": """# Gesture navigation

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
""",

    "splash-screen.md": """# Splash Screen

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
""",

    "checkout.md": """# Checkout

Platforms: Mobile
Tier: Common — assume it applies unless the product has no mobile monetary transactions; state the reason when excluding it.`

The mobile payment flow optimized for native digital wallet methods, small-screen input constraints, and quick order completion.

- [ ] **Native wallet payments** — Apple Pay and Google Pay offered as top-tier primary checkout actions for single-tap biometric confirmation.
- [ ] **Manual card entry fallback** — Form interface for credit and debit card entry when native digital wallets are unavailable or declined.
- [ ] **Persistent order summary** — Collapsible order summary showing line items, quantities, and final price throughout all checkout steps.
- [ ] **Minimal form fields** — Requesting only essential shipping and billing details, avoiding redundant fields.
- [ ] **Platform autofill support** — Input fields configured with iOS `textContentType` and Android Autofill hints for single-tap address completion.
- [ ] **Keyboard type optimization** — Numeric keypads for card numbers (`keyboardType="number-pad"`), expiration dates, and security codes (CVV).
- [ ] **Multi-step progress tracking** — Clear step indicator (e.g. Shipping → Payment → Confirm) on multi-screen checkout workflows.
- [ ] **Payment failure recovery** — Returning users to the payment step with entered data preserved and a clear error explanation upon payment decline.
- [ ] **Order confirmation view** — Dedicated confirmation screen displaying order number, summary, payment method, and estimated delivery dates.
""",

    "tab-bar-navigation.md": """# Tab Bar Navigation

Platforms: Mobile
Tier: Common — assume it applies to mobile apps with multi-section top-level navigation; state the reason when excluding it.

The persistent bottom navigation bar providing single-tap access to 3–5 top-level sections of a mobile application.

- [ ] **Strict tab count limit** — Restricted to 3 to 5 primary destinations to prevent visual clutter and mis-taps.
- [ ] **Icon and text label pairing** — Every tab item pairing an intuitive icon with a concise text label for accessibility and clarity.
- [ ] **Distinct active state** — Visually distinct selected state using brand accent color, filled icon variants, or heavy font weight.
- [ ] **Real-time badge counts** — Subtle numerical or dot badges for tabs with unread alerts, updating dynamically without full screen reloads.
- [ ] **Persistent presence** — Remains visible across main view hierarchies; hidden automatically in deep detail screens or modal workflows.
- [ ] **Accessible touch targets** — Minimum tap target area of 44×44pt on iOS per [Apple's Human Interface Guidelines on layout](https://developer.apple.com/design/human-interface-guidelines/layout) and 48×48dp on Android per [Material Design accessibility guidelines](https://m3.material.io/foundations/accessibility/accessibility-checklist).
- [ ] **Selection haptic feedback** — Light haptic tap upon switching active tabs to confirm selection.
""",

    "in-app-notifications.md": """# In-App Notifications

Platforms: Mobile
Tier: Common — assume it applies to apps with user activity feeds or transactional updates; state the reason when excluding it.

The dedicated in-app activity center displaying updates, system alerts, and social interactions, distinct from system push notifications.

- [ ] **Reverse chronological feed** — Most recent notification items listed first with clear relative timestamps ("2m ago", "Yesterday").
- [ ] **Unread status indicators** — Visual unread markers (accent dot, bold typography, tinted background) for unread items.
- [ ] **Mark all as read action** — Single tap control to clear all unread indicators simultaneously.
- [ ] **Notification grouping** — Aggregating related notification triggers (e.g., "5 people commented on your post") into single expandable items to reduce clutter.
- [ ] **Swipe-to-dismiss gesture** — Left-swipe action on individual notifications to dismiss or archive them.
- [ ] **Deep link routing** — Tapping a notification navigates directly to the referenced item or screen within the app.
- [ ] **Empty notification state** — Friendly empty state graphic and messaging when the inbox contains no notifications.
- [ ] **Settings shortcut** — Direct link from notification feed to notification preference controls.
""",

    "action-sheet.md": """# Action Sheet

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
""",

    "camera.md": """# Camera

Platforms: Mobile
Tier: Conditional — assume it does not apply until photo, video, or document capture capability is confirmed present.

The custom camera view for capturing photos, videos, or document scans, including viewfinder controls and preview review.

- [ ] **Contextual permission prompt** — Requesting camera and microphone permissions at the exact moment of capture with clear justification, not during app launch.
- [ ] **Fullscreen viewfinder layout** — Clear viewfinder display with an accessible, high-contrast capture shutter button centered at the bottom.
- [ ] **Flash mode toggle** — Flash controls (Auto, On, Off) directly accessible in the viewfinder header.
- [ ] **Camera flip toggle** — Easy-to-reach button to switch between front and rear camera lenses, positioned to avoid accidental taps.
- [ ] **Post-capture preview** — Immediate preview screen allowing the user to inspect the captured media with options to retake or confirm.
- [ ] **Session gallery picker** — Shortcut to select existing photos from the device photo gallery as an alternative to taking a new photo.
""",

    "map-view.md": """# Map View

Platforms: Mobile
Tier: Conditional — assume it does not apply until location-based mapping features are confirmed present.

The interactive map screen showing user position, location pins, overlays, and contextual venue details.

- [ ] **Custom marker pins** — High-contrast map markers with touch targets meeting 44×44pt (iOS) and 48×48dp (Android) guidelines.
- [ ] **Marker clustering** — Grouping dense clusters of nearby markers into single numbered cluster pins at low zoom levels.
- [ ] **Native map components** — Built using native MapKit (iOS) or Google Maps SDK (Android) for smooth vector rendering and gesture performance.
- [ ] **Location permission handling** — Prompting for location permission with clear context, offering manual location search if permission is denied.
- [ ] **Re-center location CTA** — Floating action button to quickly re-center the map view onto the user's current GPS coordinates.
- [ ] **Selected item bottom sheet** — Tapping a marker expands a bottom sheet detailing the location without navigating away from the map.
- [ ] **Offline tile caching indicator** — Displaying cached map tiles when offline with subtle UI indicating location data may be outdated.
""",

    "onboarding-checklist.md": """# Onboarding Checklist

Platforms: Mobile
Tier: Conditional — assume it does not apply until an interactive, task-based setup flow for new users is confirmed present.

An in-app setup widget tracking progress through key setup tasks to guide new users to early value.

- [ ] **Non-intrusive card layout** — Presented as a collapsible dashboard card or bottom sheet, not a blocking modal overlay.
- [ ] **Visible progress tracking** — Clear fraction counter (e.g., "2 of 5 completed") paired with a visual progress bar.
- [ ] **Direct action navigation** — Tapping any incomplete task item navigates straight to the screen where that action can be performed.
- [ ] **Completion celebration** — Brief, delight-inducing animation (confetti or check mark pulse) upon completing all setup tasks.
- [ ] **Dismissible control** — Option to dismiss or hide the checklist for users who prefer self-guided exploration.
- [ ] **Persistent widget recovery** — Option to re-open the checklist from account settings or home view while incomplete.
""",

    "paywall.md": """# Paywall

Platforms: Mobile
Tier: Conditional — assume it does not apply until premium locked content or subscription paywalls are confirmed present.

The screen gating access to premium features or content, presenting tier options and subscription checkout.

- [ ] **Value breakdown & feature list** — Concise summary of exact capabilities or content unlocked by upgrading.
- [ ] **Prominent purchase CTA** — Dominant primary action button to subscribe or start a trial.
- [ ] **Free trial disclosure** — Transparent trial details (e.g., "7 days free, then $9.99/mo") placed directly adjacent to the CTA.
- [ ] **Neutral close action** — Visible close button ("X" or "Not now") in neutral styling to return to free experience without manipulative guilt copy.
- [ ] **Restore purchases button** — Mandatory button allowing existing subscribers to restore active entitlements per [Apple's App Store Review Guideline 3.1.1](https://developer.apple.com/app-store/review/guidelines/#in-app-purchase).
- [ ] **Guideline-compliant subscription terms** — Mandatory legal disclosures (subscription title, length, price, link to Privacy Policy and Terms of Use) displayed before purchase.
""",

    "onboarding.md": """# Onboarding

Platforms: Mobile
Tier: Common — assume it applies to mobile apps requiring initial user orientation or setup; state the reason when excluding it.

The first-run welcome carousel orienting new users, collecting initial preferences, and setting up the core experience.

- [ ] **Concise step sequence** — Restricted to 3 to 5 essential slides focusing on primary value propositions.
- [ ] **Visual step indicator** — Page dots or progress bar showing current position and remaining steps.
- [ ] **Flexible step navigation** — Supporting both swipe gestures and explicit "Next" buttons for advancing slides.
- [ ] **Contextual permission timing** — Explaining permission context before triggering native OS prompts (notifications, camera, location).
- [ ] **Skip onboarding option** — Prominent "Skip" option allowing experienced users to jump straight into the application.
- [ ] **Personalization choices** — 1 or 2 quick initial questions (e.g., role, interests) to customize the home feed immediately.
- [ ] **Soft keyboard layout adjust** — Form steps adjusting layout dynamically when soft keyboard appears.
""",

    "chat.md": """# Chat

Platforms: Mobile
Tier: Conditional — assume it does not apply until real-time messaging between users or support agents is confirmed present.

The real-time messaging screen supporting text, media attachments, message statuses, and active keyboard handling.

- [ ] **Keyboard push-up layout** — Message input bar anchoring directly above the soft keyboard without hiding conversation history.
- [ ] **Persistent input bar** — Fixed bottom bar containing text area, attach button, and send button.
- [ ] **Distinct message bubbles** — Right-aligned colored bubbles for sent messages, left-aligned gray bubbles for received messages.
- [ ] **Swipe-to-reply gesture** — Swiping a message bubble right to start an inline reply thread.
- [ ] **Long-press context menu** — Long-pressing a message bubble to reveal reaction emojis, copy, reply, or delete options.
- [ ] **Read status indicators** — Subtle indicators (sent, delivered, read checkmarks) below sent messages.
- [ ] **Media attachment previews** — Inline image/video thumbnails in input bar before sending.
- [ ] **Animated typing indicator** — Real-time indicator ("User is typing...") when the counterparty is drafting a response.
- [ ] **Jump to latest button** — Floating button to scroll directly to the latest message when scrolled up in chat history.
""",

    "in-app-browser.md": """# In-App Browser

Platforms: Mobile
Tier: Conditional — assume it does not apply until the app opens external web links within an embedded web view.

The embedded web view screen displaying external web content safely without kicking the user out of the mobile app.

- [ ] **Domain URL display** — Displaying verified domain hostname in the top bar to verify security before users enter credentials.
- [ ] **Explicit close button** — Persistent "Done" or "X" button to dismiss the web view and return instantly to native app context.
- [ ] **Open in system browser CTA** — Option menu item to hand off current URL to Safari or Chrome.
- [ ] **Share link action** — Native share sheet shortcut to copy or send the webpage link.
- [ ] **Loading progress bar** — Top-edge progress bar indicating web page fetch and render status.
""",

    "invite.md": """# Invite

Platforms: Mobile
Tier: Conditional — assume it does not apply until team workspaces or multi-user invitation capabilities are confirmed present.

The flow for inviting team members or contacts to shared workspaces, setting access roles, and managing pending invitations.

- [ ] **Email invite entry** — Primary input field to enter single or multiple email addresses.
- [ ] **Role assignment picker** — Dropdown or selector specifying invited role (Admin, Member, Viewer) with clear permission explanations.
- [ ] **Device contact picker** — Integration with native device contacts to select invitees without manual email typing.
- [ ] **Pending invite management** — List of sent invitations with options to resend or revoke pending access.
- [ ] **Shareable invite link** — Option to generate a secure join link with customizable permissions and expiration dates.
- [ ] **Member seat limit indicator** — Displaying remaining workspace seat count before reaching plan billing limits.
""",

    # ---------------------------------------------------------
    # Web app only (7)
    # ---------------------------------------------------------
    "2fa.md": """# 2FA

Platforms: Web app
Tier: Common — assume it applies unless the product has no password authentication or user accounts; state the reason when excluding it.

The setup and verification screens for two-factor authentication protecting user account access.

- [ ] **Multi-method support** — Offering TOTP authenticator apps (Google Authenticator, 1Password) alongside WebAuthn hardware keys or SMS fallback.
- [ ] **Step-by-step setup guide** — Clear multi-step wizard guiding TOTP pairing, QR code scan, and secret key entry.
- [ ] **QR code and secret key display** — Large, scannable QR code paired with a copyable textual secret key for manual entry.
- [ ] **Setup verification step** — Requiring entry of a valid 6-digit code before enabling 2FA, preventing lockouts from broken setups.
- [ ] **Single-use recovery codes** — Generating a set of emergency backup codes, requiring download/copy confirmation before finishing setup.
- [ ] **2FA active success state** — Clear confirmation indicating 2FA is active on the account.
- [ ] **Re-authentication before disable** — Mandatory password re-prompt before disabling or altering 2FA configurations.
""",

    "notification-settings.md": """# Notification Settings

Platforms: Web app
Tier: Common — assume it applies unless the product sends no notifications across any channel; state the reason when excluding it.

The matrix configuration page where users manage notification categories, channels, and delivery frequency.

- [ ] **Logical notification categories** — Grouping settings into product activity, mentions, billing, security, and marketing updates.
- [ ] **Granular channel matrix** — Checkbox grid allowing independent control for Email, In-App, Push, and SMS per category.
- [ ] **Delivery frequency controls** — Options for real-time alerts versus daily or weekly digest summaries.
- [ ] **Global pause / mute toggle** — Master control to temporarily mute non-security notifications.
- [ ] **Auto-save feedback** — Immediate auto-save response with subtle `role="status"` visual confirmation.
""",

    "help-center.md": """# Help Center

Platforms: Web app
Tier: Common — assume it applies unless the product relies entirely on direct support channels; state the reason when excluding it.

The self-serve documentation portal where users search articles, browse category guides, and solve issues independently.

- [ ] **Prominent instant search** — Central search input with instant autocomplete suggestions returning matching article titles.
- [ ] **Categorized topic layout** — Grouping documentation by user workflows rather than internal team organizational structures.
- [ ] **Featured and popular articles** — Highlighting frequently accessed guides on the help center landing page.
- [ ] **Structured article formatting** — Clear heading hierarchy, annotated screenshots, and syntax-highlighted code snippets.
- [ ] **Article freshness timestamp** — Displaying "Last updated" dates on articles to establish documentation accuracy.
- [ ] **Content helpfulness rating** — Simple "Was this article helpful?" thumbs-up/down feedback widget at article footers.
- [ ] **Related articles sidebar** — Contextual links to complementary topics and troubleshooting guides.
""",

    "user-management.md": """# User Management

Platforms: Web app
Tier: Conditional — assume it does not apply until multi-user organization accounts or team management capabilities are confirmed present.

The admin dashboard for listing workspace members, sending role-based invitations, and managing user access states.

- [ ] **Searchable member directory** — Data table listing workspace users with name, email, role, and active status columns.
- [ ] **Invite new members flow** — Modal form to send email invites with pre-assigned workspace roles (Admin, Member, Viewer).
- [ ] **Standardized role definitions** — Clear role descriptions explaining permissions without ambiguous custom role titles.
- [ ] **Pending invitation list** — Dedicated tab showing pending invites with options to resend or revoke.
- [ ] **User filter and search** — Real-time filtering by role, status, or search query string.
- [ ] **Access revocation & deactivation** — Pathways to suspend or permanently remove user membership from the workspace.
""",

    "single-item-detail.md": """# Single Item Detail

Platforms: Web app
Tier: Common — assume it applies to web applications featuring list-detail record inspection; state the reason when excluding it.

The comprehensive detail view displaying attributes, activity logs, and actions for a single selected record.

- [ ] **Prominent record header** — Displaying primary record name, unique ID code, and status badge prominently.
- [ ] **Multi-modal status indicator** — Using text labels alongside status badge colors per [WCAG 2.1 SC 1.4.1, Use of Color](https://w3c.github.io/wcag/understanding/use-of-color.html).
- [ ] **Structured key details layout** — Organizing primary attributes in visual summary cards with secondary metadata below.
- [ ] **Inline edit controls** — Pathways to modify fields inline or switch to dedicated edit state.
- [ ] **Linked record references & audit log** — Displaying parent/child relationships and chronological audit history ("Who changed what when").
- [ ] **Breadcrumb navigation** — Accessible breadcrumbs allowing 1-click return to the parent list index.
- [ ] **Destructive action isolation** — Visually separating delete or archive actions from primary workflow buttons.
""",

    "admin-panel.md": """# Admin Panel

Platforms: Web app
Tier: Conditional — assume it does not apply until system administration or organization management capabilities are confirmed present.

The high-level administration suite for platform owners to oversee users, system settings, billing, and security audit logs.

- [ ] **Role-gated route security** — Strict server-side and client-side access control restricting view access to admin roles.
- [ ] **Global user administration** — Directory of all system accounts with controls to manage roles, reset 2FA, or freeze access.
- [ ] **Organization & domain settings** — Controls for configuring SSO SAML, custom domains, and workspace branding.
- [ ] **System usage overview** — High-level metric dashboards tracking API calls, storage usage, and active seats.
- [ ] **Organization billing control** — Centralized view of invoices, contract terms, seat counts, and payment methods.
- [ ] **Comprehensive audit log** — Immutable log recording security events, permission modifications, and admin actions.
- [ ] **Typed confirmation danger zone** — Requiring typed confirmation (e.g. typing workspace name) for destructive admin operations.
""",

    "empty-state.md": """# Empty State

Platforms: Web app
Tier: Fundamental — assume it applies to virtually every web application screen displaying data lists; state the reason if excluding it.

The view presented when a table, dashboard, or list contains zero data items due to new account status, cleared filters, or empty search.

- [ ] **Contextual illustration or icon** — Clear, topic-specific visual element setting tone without visual noise.
- [ ] **Concise heading** — Plain language title naming what is missing (e.g. "No projects yet", not "It's empty").
- [ ] **Explanatory body description** — 1 or 2 sentences explaining how data arrives in this space or why it is empty.
- [ ] **Direct primary call to action** — Prominent CTA button guiding the user to create, import, or connect data (e.g., "Create project").
- [ ] **Filter reset alternative** — Specific empty state variant when filters yield no results, offering a 1-click "Clear filters" action.
""",

    # ---------------------------------------------------------
    # Website only (19)
    # ---------------------------------------------------------
    "security.md": """# Security

Platforms: Website
Tier: Fundamental — assume it applies to virtually every commercial software website to establish customer trust; state the reason if excluding it.

The marketing page documenting compliance standards, data encryption, infrastructure safety, and disclosure policies.

- [ ] **Compliance certifications** — Highlighting verified badges and details for SOC 2 Type II, ISO 27001, GDPR, and HIPAA compliance.
- [ ] **Data encryption standards** — Explaining encryption protocols in plain language (AES-256 at rest, TLS 1.3 in transit).
- [ ] **Data residency disclosures** — Details specifying physical server locations (AWS/GCP regions) and regional storage options.
- [ ] **Strict access controls** — Documenting internal access policies, multi-tenant isolation, and least-privilege administrative safeguards.
- [ ] **Responsible vulnerability disclosure** — Clear security policy page and dedicated contact email (`security@domain.com`) or bug bounty program.
- [ ] **Incident history and status link** — Transparent record of past security updates and direct link to the live status page.
- [ ] **Third-party pentest reports** — Summary of annual third-party penetration testing with request forms for full reports under NDA.
""",

    "about.md": """# About

Platforms: Website
Tier: Common — assume it applies unless the product has no public marketing site; state the reason when excluding it.

The company overview page presenting origin story, core mission, founding team, and key milestones.

- [ ] **Authentic origin story** — Concise narrative explaining why the company was founded and the core problem it solves.
- [ ] **Mission and core values** — Plain language statements defining business principles and product philosophy.
- [ ] **Founding team showcase** — Photos, titles, and short bios of key leadership and team members to humanize the business.
- [ ] **Company milestones & traction** — Key achievements (founding year, customer metrics, funding milestones) building market credibility.
- [ ] **Investors and backers** — Recognized logos of funding partners, advisory boards, or incubator programs.
- [ ] **Clear conversion CTA** — Direct next step inviting visitors to try the product, view open roles, or read the blog.
""",

    "privacy.md": """# Privacy

Platforms: Website
Tier: Fundamental — assume it applies to virtually every website as a legal baseline; state the reason if excluding it.

The legal policy portal covering privacy practices, terms of service, cookie usage, and data subject rights.

- [ ] **Comprehensive privacy policy** — Explaining data collection, storage duration, processing purposes, and deletion rights in plain language.
- [ ] **Terms of service agreement** — Governing rules detailing acceptable use, account liabilities, and limitation of liability clauses.
- [ ] **Cookie policy & consent banner** — Explicit breakdown of essential, analytical, and marketing cookies with opt-in/opt-out toggles.
- [ ] **Effective date timestamp** — Clear "Last updated" date displayed at the top of every legal document.
- [ ] **Version history changelog** — Plain language summary of recent policy revisions to build visitor trust.
- [ ] **Dedicated legal contact** — Specific email address (`privacy@domain.com`) or webform for GDPR/CCPA data access requests.
""",

    "features.md": """# Features

Platforms: Website
Tier: Common — assume it applies unless the website is a single landing page; state the reason when excluding it.

The feature tour page detailing core capabilities, visual product demonstrations, and tangible customer benefits.

- [ ] **Categorized feature sections** — Organizing capabilities into task-oriented categories to prevent wall-of-bullet clutter.
- [ ] **User-centric descriptions** — Explaining each feature in terms of user outcomes rather than system specifications.
- [ ] **Rich visual demonstrations** — High-resolution screenshots, UI walkthrough GIFs, or short video clips showcasing live workflows.
- [ ] **Outcome benefit framing** — Explicitly connecting technical features to saved time, reduced cost, or increased productivity.
- [ ] **Contextual social proof** — Customer quotes placed adjacent to relevant feature sections.
- [ ] **Inline conversion calls to action** — Primary CTA buttons positioned strategically at natural decision points down the page.
""",

    "testimonials.md": """# Testimonials

Platforms: Website
Tier: Common — assume it applies unless the product has zero customers or case studies yet; state the reason when excluding it.

The social proof showcase compiling verified customer reviews, video quotes, case studies, and rating metrics.

- [ ] **Attributed customer quotes** — Direct quotes detailing concrete business outcomes, fully attributed with name, job title, and company logo.
- [ ] **Full customer identity verification** — Complete attribution details eliminating anonymous testimonials.
- [ ] **Diverse use cases** — Quotes representing varied industries, company sizes, and buyer personas.
- [ ] **Short video testimonials** — Embedded video clips for visitors who prefer visual customer proof over text.
- [ ] **Third-party rating badges** — Verified review scores from G2, Capterra, or Trustpilot linking to independent review profiles.
""",

    "affiliate.md": """# Affiliate

Platforms: Website
Tier: Conditional — assume it does not apply until an affiliate or referral payout program is confirmed present.

The partner portal inviting creators and affiliates to join, outlining reward structures and marketing assets.

- [ ] **Program overview** — Clear summary of partner criteria and target audience fit.
- [ ] **Transparent commission structure** — Explicit payout rates (e.g., "20% recurring for 12 months") and payout frequencies without ambiguous fine print.
- [ ] **How it works breakdown** — Simple step-by-step guide explaining signup, referral link creation, tracking, and payout.
- [ ] **Partner resources provided** — Details on promotional banners, copy templates, and tracking dashboard capabilities.
- [ ] **Partner success proof** — Quotes or earnings examples from existing active affiliates.
- [ ] **Application CTA button** — Direct call to action opening the affiliate registration form.
""",

    "compare.md": """# Compare

Platforms: Website
Tier: Conditional — assume it does not apply until competitive comparison positioning pages are confirmed present.

The comparison page evaluating the product against a named competitor to assist prospects during evaluation.

- [ ] **Objective positioning statement** — Clear opening explaining primary architectural or strategic differences without hyperbolic claims.
- [ ] **Feature comparison grid** — Side-by-side matrix with checkmarks and cross marks evaluating key features.
- [ ] **Key differentiator highlights** — Dedicated sections detailing areas where the product genuinely excels.
- [ ] **Competitor switcher social proof** — Quotes from customers who migrated from the specific named competitor.
- [ ] **Transparent pricing comparison** — Honest comparison of total cost of ownership and pricing tiers.
- [ ] **Direct trial or demo CTA** — Clear call to action to start a trial or book a migration demo.
""",

    "status.md": """# Status

Platforms: Website
Tier: Common — assume it applies unless the product has no online infrastructure or APIs; state the reason when excluding it.

The operational dashboard detailing live service availability, incident updates, and scheduled maintenance windows.

- [ ] **Component status breakdown** — Individual operational indicators for Web App, API, Database, Third-party Integrations, and Notifications.
- [ ] **Timestamped live incident updates** — Sequential incident post updates (Investigating → Identified → Monitoring → Resolved).
- [ ] **Incident history archive** — Searchable log of past incidents with dates, durations, and post-mortem links.
- [ ] **90-day uptime metrics** — Historical percentage uptime charts per system component over a rolling 90-day window.
- [ ] **Scheduled maintenance notices** — Advance notifications for planned maintenance windows announced at least 72 hours prior.
- [ ] **Multi-channel update subscriptions** — Options to subscribe to incident alerts via Email, SMS, or Webhook.
- [ ] **Independent domain hosting** — Hosted on an isolated infrastructure domain (e.g., `status.domain.com`) to remain online during core outages.
""",

    "press-media.md": """# Press / Media

Platforms: Website
Tier: Conditional — assume it does not apply until brand media kits or press contact pages are confirmed present.

The media resource center providing brand assets, company boilerplate, executive bios, and press contacts.

- [ ] **Official company boilerplate** — Approved 1-paragraph company summary for editorial media reuse.
- [ ] **High-res brand asset kit** — Downloadable ZIP containing primary logo, wordmark, app icons, and product screenshots in light and dark PNG/SVG formats.
- [ ] **Executive bios and photos** — Headshots and approved biographies of founders and key executives.
- [ ] **Verified company factsheet** — Founding date, headquarters, employee count, and customer scale metrics.
- [ ] **Press contact email** — Dedicated press inbox (`press@domain.com`) distinct from sales and support channels.
- [ ] **Brand usage guidelines** — Rules detailing clear space, primary color codes, and disallowed logo modifications.
""",

    "waitlist.md": """# Waitlist

Platforms: Website
Tier: Conditional — assume it does not apply until pre-launch or limited-access lead capture is confirmed present.

The pre-launch landing page capturing early interest and managing rollout queues before public availability.

- [ ] **Concise value proposition** — Headline and copy explaining what product is coming and why visitors should sign up early.
- [ ] **Minimal signup form** — Short email capture form with 1 or 2 optional segmentation fields.
- [ ] **Clear queue expectations** — Explicit explanation of how access will be granted (chronological waves, invite codes, VIP access).
- [ ] **Interest proof counters** — Live, verified count of waitlist subscribers or interested company logos.
- [ ] **Referral viral mechanic** — Share link giving subscribers priority queue position for inviting friends.
- [ ] **Post-signup confirmation state** — Instant confirmation state with share buttons and expectation setting.
""",

    "team.md": """# Team

Platforms: Website
Tier: Common — assume it applies unless the company prefers to stay anonymous or solo-operated; state the reason when excluding it.

The company culture page showcasing team member profiles, roles, and background bios.

- [ ] **Team directory grid** — Photos, names, and understandable job titles for company team members.
- [ ] **Clear job title labels** — Standardized job titles avoiding confusing internal terminology.
- [ ] **Humanizing short bios** — Concise 2-sentence background highlights for each team member.
- [ ] **Professional social links** — Optional links to individual LinkedIn or X profiles.
- [ ] **Hiring callout banner** — Visual banner indicating active growth with direct link to the Careers page.
""",

    "careers.md": """# Careers

Platforms: Website
Tier: Conditional — assume it does not apply until open job postings or recruiting efforts are confirmed present.

The recruiting portal detailing company culture, employee benefits, open job roles, and application steps.

- [ ] **Searchable open roles list** — Up-to-date listing of active job openings grouped by department (Engineering, Sales, Design) with location indicators (Remote, Hybrid).
- [ ] **Company mission & vision** — Clear statement of core business purpose and problem vision to attract aligned talent.
- [ ] **Culture and values** — Transparent description of day-to-day collaboration, decision-making, and working style.
- [ ] **Employee benefits overview** — Itemized list of benefits (health insurance, 401k match, flexible PTO, home office stipend).
- [ ] **Transparent hiring process** — Step-by-step interview roadmap detailing initial screen, technical assessment, team interview, and offer stage.
- [ ] **Direct application pathway** — Clear "Apply Now" button per job opening leading directly to the application form.
""",

    "blog-post.md": """# Blog Post

Platforms: Website
Tier: Conditional — assume it does not apply until long-form article pages are confirmed present.

The article view designed for long-form reading, content discovery, author credibility, and social sharing.

- [ ] **Clear headline & subtitle** — High-impact title and summary establishing article topic and value.
- [ ] **Author and publish metadata** — Author avatar, name, publish date, estimated reading time, and last updated date.
- [ ] **Ergonomic typography & layout** — Optimal line length (60–75 characters per line), high-contrast text typography, and balanced line-height.
- [ ] **Sticky table of contents** — Interactive table of contents side nav for long articles, highlighting active reading position.
- [ ] **Inline media & code blocks** — Formatted images, diagrams, video embeds, and syntax-highlighted code snippets.
- [ ] **Related articles footer** — Contextual article cards suggesting next reading topics to keep readers engaged.
- [ ] **Non-intrusive share actions** — Unobtrusive social share buttons (X, LinkedIn, Copy Link) that don't cover body text.
""",

    "contact-us.md": """# Contact Us

Platforms: Website
Tier: Fundamental — assume it applies to virtually every commercial website to provide visitor access; state the reason if excluding it.

The contact hub routing incoming inquiries to Sales, Support, Press, or Partnerships with clear expectations.

- [ ] **Intent-based contact routing** — Separate pathways for Support, Sales, Press, and Security to prevent inbox bottlenecks.
- [ ] **Minimal contact form** — Form capturing essential details (Name, Email, Subject, Message, Company size) with clear validation.
- [ ] **Direct communication details** — Official company email address, physical office mailing address, and business phone number where appropriate.
- [ ] **Expected response timeframe** — Stated response window (e.g. "We respond within 24 business hours") setting clear visitor expectations.
- [ ] **Self-serve deflection shortcuts** — Prominent links to Help Center, FAQ, and Status Page above the form to resolve common questions faster.
- [ ] **Submission confirmation message** — Clear confirmation state acknowledging receipt of the message with reference details.
""",

    "pricing.md": """# Pricing

Platforms: Website
Tier: Common — assume it applies unless the product is entirely free or uses custom sales quotes exclusively; state the reason when excluding it.

The pricing page presenting subscription plans, feature comparisons, billing cadence toggles, and conversion CTAs.

- [ ] **Unambiguous plan names & prices** — Distinct tier cards (e.g., Free, Pro, Enterprise) displaying clear price numbers and billing frequency.
- [ ] **Annual vs monthly billing toggle** — Interactive toggle displaying annual discount savings (e.g. "Save 20%").
- [ ] **Detailed feature matrix** — Side-by-side comparison table detailing included quota limits and feature availability across tiers.
- [ ] **Prominent CTA per tier** — Distinct action button on each plan card ("Start 14-day trial", "Buy now", "Contact sales").
- [ ] **Free trial / tier details** — Clear disclosure of what happens when a trial ends or quota limits are reached.
- [ ] **Pricing FAQ section** — Answers addressing common billing, upgrade, seat counting, and cancellation questions.
- [ ] **Enterprise custom quote pathway** — Dedicated Enterprise tier card directing large organizations to book a demo.
""",

    "faq.md": """# FAQ

Platforms: Website
Tier: Common — assume it applies unless pre-purchase questions are addressed fully on product pages; state the reason when excluding it.

The frequently asked questions section addressing common pre-purchase, technical, and billing queries.

- [ ] **Categorized question topics** — Grouping questions into clear tabs or headers (General, Billing, Security, Technical).
- [ ] **Direct, plain-language answers** — Concise answers resolving questions directly without marketing jargon.
- [ ] **Accordion expandable layout** — Collapsible Q&A accordion headers keeping the page compact while preserving quick scannability.
- [ ] **Deep-linkable questions** — Unique URL anchors (`#faq-item-id`) for linking directly to specific answers in support conversations.
- [ ] **Support escalation link** — Clear CTA at the bottom ("Still have questions? Contact support") routing unresolved users to help channels.
""",

    "404.md": """# 404

Platforms: Website
Tier: Fundamental — assume it applies to virtually every website to handle broken links gracefully; state the reason if excluding it.

The custom error page presented when a visitor hits a broken or missing URL, providing recovery paths back to core content.

- [ ] **Clear plain-language message** — Friendly header indicating the page was not found without technical error jargon.
- [ ] **Core navigation recovery links** — Direct links to Home, Pricing, Blog, Help Center, and Product Features pages.
- [ ] **Search bar overlay** — Accessible search input field letting visitors search for their desired destination immediately.
- [ ] **On-brand visual design** — Styled consistently with the site's design system so visitors know they are still on the product website.
- [ ] **Report broken link option** — Secondary link allowing visitors to notify site administrators of broken links.
- [ ] **No dead-end layout** — Always providing at least two explicit clickable conversion pathways to prevent visitor bounce.
""",

    "blog.md": """# Blog

Platforms: Website
Tier: Conditional — assume it does not apply until a content publication index page is confirmed present.

The article index page allowing visitors to browse published articles, filter by topic, and subscribe to updates.

- [ ] **Structured post grid layout** — Article cards presenting featured thumbnail image, title, excerpt, author, date, and reading time.
- [ ] **Category & tag navigation** — Filter bar allowing visitors to narrow articles by topic (Product, Engineering, Design, News).
- [ ] **Featured post hero** — Highlighted lead article display at the top of the grid emphasizing key publication releases.
- [ ] **Instant article search** — Search input field filtering articles by title or keyword.
- [ ] **Clear pagination controls** — Accessible "Previous / Next" pagination or "Load more" button for browsing older content archives.
- [ ] **Newsletter signup CTA** — Prominent conversion form inviting readers to subscribe to email updates.
""",

    "sign-up.md": """# Sign up

Platforms: Website
Tier: Common — assume it applies unless the product has no self-serve account creation; state the reason when excluding it.

The account creation page where prospective users register new accounts and initiate onboarding.

- [ ] **Minimal required fields** — Requesting only essential signup information (Email and Password, or Name) to minimize onboarding friction.
- [ ] **Social / SSO signup buttons** — Single-tap registration options ("Sign up with Google", "Sign up with Apple") eliminating manual form entry.
- [ ] **Clear password criteria guidance** — Displaying strength and character requirements before form submit to prevent trial-and-error errors.
- [ ] **Terms and Privacy acknowledgment** — Explicit text and links to Terms of Service and Privacy Policy adjacent to the submit action.
- [ ] **Visible login link for existing users** — Prominent link ("Already have an account? Log in") for returning users landing on signup by mistake.
- [ ] **Next steps expectation** — Brief notification stating what happens next (e.g. "Check your inbox for a confirmation link").
""",

    # ---------------------------------------------------------
    # Flow only (13)
    # ---------------------------------------------------------
    "adding-to-cart.md": """# Adding to cart

Platforms: Flow
Tier: Conditional — assume it does not apply until an item selection and cart addition moment is confirmed present.

The micro-interaction moment where a user selects item variants and adds a product to their shopping cart.

- [ ] **Explicit variant selection validation** — Ensuring required options (size, color, tier) are selected before enabling cart addition.
- [ ] **Prominent primary CTA button** — Dominant "Add to Cart" button positioned cleanly within viewport on product detail views.
- [ ] **Immediate confirmation feedback** — Visual confirmation state (mini-cart drawer opening, toast banner, button state checkmark) confirming addition without full page reload.
- [ ] **Accessible mini-cart / navigation counter** — Cart badge counter updating dynamically with `aria-live="polite"` feedback per [WCAG 2.1 SC 4.1.3, Status Messages](https://w3c.github.io/wcag/understanding/status-messages.html).
- [ ] **Out-of-stock handling** — Disabling CTA and displaying clear "Out of Stock" status when selected variant inventory is zero.
""",

    "uploading-media.md": """# Uploading media

Platforms: Flow
Tier: Conditional — assume it does not apply until file, image, or document upload capabilities are confirmed present.

The flow for dragging, selecting, validating, and uploading file attachments with real-time feedback.

- [ ] **Drop zone empty state** — Visual drag-and-drop target zone displaying upload icon, supported formats, file size limits, and fallback browse button.
- [ ] **Active drag-over visual indicator** — High-contrast state change on the drop zone when a file is dragged over the browser window.
- [ ] **Real-time progress indicators** — Visual progress bars and percentage counts for ongoing uploads.
- [ ] **Pre-upload constraint validation** — Validating file type extensions and maximum file size client-side before network transfer starts.
- [ ] **Status result indicators** — Clear visual status icons (green checkmark for success, red warning icon for failure) with explicit error text.
- [ ] **Upload management actions** — Controls to retry failed uploads, cancel in-progress transfers, delete uploaded files, or rename items.
- [ ] **Multi-file preview list** — Clean list or thumbnail grid detailing file name, size, and image preview.
""",

    "verifying-account.md": """# Verifying account

Platforms: Flow
Tier: Common — assume it applies unless account creation requires zero identity verification; state the reason when excluding it.

The verification moment where a user confirms ownership of their email address or phone number during onboarding.

- [ ] **Clear verification trigger** — Explaining clearly why verification is required and displaying the exact email address or phone number used.
- [ ] **Verification code input** — Digit input fields supporting autofill (`autocomplete="one-time-code"` on web/iOS) allowing single-tap OTP insertion.
- [ ] **Resend code mechanism** — Visible option to request a new code with a countdown timer preventing API spam.
- [ ] **Actionable verification error states** — Specific error messages for expired codes, incorrect digits, or rate-limited attempt lockouts.
- [ ] **Verification success transition** — Instant visual confirmation upon valid code entry, automatically advancing the user to the next step.
""",

    "canceling-subscription.md": """# Canceling subscription

Platforms: Flow
Tier: Conditional — assume it does not apply until paid subscription cancellation flows are confirmed present.

The workflow allowing users to cancel an active paid subscription self-serve without contacting support.

- [ ] **Accessible cancellation link** — Visible cancellation link in billing settings, avoiding hidden menus.
- [ ] **Intent confirmation step** — Confirming cancellation intent while presenting key features or data benefits that will be lost upon downgrade without manipulative dark patterns.
- [ ] **Optional churn reason survey** — Single-select reason survey (e.g. "Too expensive", "Switching products") to gather feedback.
- [ ] **Clear access retention date** — Explicit statement detailing the exact end date through which paid access remains active.
- [ ] **FTC & legal compliance** — Easy self-serve cancellation meeting FTC click-to-cancel regulations and EU consumer law requirements.
""",

    "filtering-items.md": """# Filtering items

Platforms: Flow
Tier: Conditional — assume it does not apply until collection filtering options are confirmed present.

The flow for applying, displaying, and clearing property filters on large data sets or product catalogs.

- [ ] **Accessible filter triggers** — Filter toggle button placed directly adjacent to the item list or search bar.
- [ ] **Appropriate control types** — Checkboxes for multi-select options, radio buttons for single choice, sliders for range values (price, date).
- [ ] **Active filter badge tags** — Displaying applied filter tags above the collection with individual clear buttons.
- [ ] **Global clear filters action** — Single click control to clear all applied filters simultaneously.
- [ ] **Dynamic result count display** — Displaying matching item count updating in real time as filter criteria change.
- [ ] **Zero result empty state** — Clear empty state explaining no items match the current combination, with a 1-click filter reset action.
""",

    "saving-changes.md": """# Saving changes

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every form edit interaction; state the reason if excluding it.

The state feedback flow accompanying form edits, setting persistence, and content modification.

- [ ] **Disabled save state** — Save action button disabled or hidden until a field is edited from its original value.
- [ ] **Active save indicator** — Save button transitioning to active visual state as soon as form values change.
- [ ] **Loading spinner on submit** — Save button displaying inline loading spinner and `aria-disabled="true"` while API call is in-flight.
- [ ] **Explicit save notification** — Accessible confirmation message (toast or inline notification with `role="status"`) confirming edits were saved.
- [ ] **Unsaved changes navigation warning** — Prompting a warning modal if the user attempts to navigate away with dirty unsaved form fields.
""",

    "entering-promo-code.md": """# Entering promo code

Platforms: Flow
Tier: Conditional — assume it does not apply until promo code discount application features are confirmed present.

The moment where a user inputs, validates, and applies a discount or coupon code at cart or checkout.

- [ ] **Accessible promo code input** — Text field with adjacent "Apply" button positioned near price summary components.
- [ ] **Instant validation success state** — Visual success feedback displaying applied discount amount and hiding code input to indicate one code limit.
- [ ] **Itemized discount impact** — Reflecting price reduction on line items and order grand total clearly.
- [ ] **Clear promo error feedback** — Explaining specific failure reasons (code expired, minimum spend not met, invalid code).
- [ ] **Remove promo code action** — Easy option to remove an applied coupon code to test an alternative code.
""",

    "showing-input-error.md": """# Showing input error

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every form input; state the reason if excluding it.

The validation flow detecting invalid form inputs and communicating errors accessibly to the user.

- [ ] **Post-blur field validation** — Validating field criteria after focus leaves the input, avoiding annoying errors while the user is actively typing.
- [ ] **Accessible error messaging** — Linking error text to input fields using `aria-invalid="true"` and `aria-describedby="error-id"` per [WCAG 2.1 SC 3.3.1, Error Identification](https://w3c.github.io/wcag/understanding/error-identification.html).
- [ ] **Multi-modal error signals** — Combining red border colors with clear error text and warning icons per [WCAG 2.1 SC 1.4.1, Use of Color](https://w3c.github.io/wcag/understanding/use-of-color.html).
- [ ] **Constructive error suggestions** — Providing specific instructions on how to fix the error per [WCAG 2.1 SC 3.3.3, Error Suggestion](https://w3c.github.io/wcag/understanding/error-suggestion.html).
- [ ] **Error clearing on re-focus** — Resetting field error styling while the user edits the field to correct values.
""",

    "resetting-password.md": """# Resetting password

Platforms: Flow
Tier: Common — assume it applies unless the product has no password authentication; state the reason when excluding it.

The self-serve recovery flow allowing users to regain access to their account after forgetting their password.

- [ ] **Accessible forgot password link** — Styled link positioned adjacent to password field on login screens.
- [ ] **Identifier request step** — Input field requesting account email address, prefilled if previously entered on login.
- [ ] **Anti-enumeration confirmation state** — Generic success message ("If an account exists for that email, we sent a reset link") preventing email harvesting.
- [ ] **Instructions email delivery** — Email containing secure, time-limited reset link or single-use verification code.
- [ ] **New password form with strength guidance** — Password input field enforcing security criteria with live strength meter.
- [ ] **Reset success & login redirection** — Clear confirmation state redirecting user directly to login with prefilled email.
""",

    "deleting-account.md": """# Deleting account

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every product storing user personal data; state the reason if excluding it.

The self-serve workflow for permanently closing an account and triggering data erasure compliance.

- [ ] **Accessible deletion location** — Located clearly in account settings, avoiding hidden customer support barriers.
- [ ] **Pre-deletion impact summary** — Explaining clearly what data and access will be permanently destroyed before user confirms.
- [ ] **Re-authentication security check** — Requiring password entry or 2FA verification before permitting deletion request submission.
- [ ] **Typed confirmation safeguard** — Requiring the user to type "DELETE" or their username to confirm irreversible action.
- [ ] **Grace period option** — Optional 14-day or 30-day grace period during which logging in cancels the pending deletion request.
- [ ] **GDPR & regulatory compliance** — Triggering automated erasure of personal data across production databases and backup stores.
""",

    "contacting-support.md": """# Contacting support

Platforms: Flow
Tier: Common — assume it applies unless the product provides no customer support channels; state the reason when excluding it.

The flow guiding a user from a problem moment to the appropriate support communication channel.

- [ ] **Accessible support triggers** — Visible help links in settings, footers, and error state dialogs.
- [ ] **Multi-channel support menu** — Presenting available help channels (Live Chat, Email Form, Knowledge Base) with operating hours.
- [ ] **Ticket context capture** — Automatically attaching browser environment, OS version, and user ID to support requests.
- [ ] **Response timeframe disclosure** — Displaying expected response window (e.g. "Typical response time: under 2 hours").
- [ ] **Confirmation state & ticket tracker** — Instant receipt confirmation displaying unique ticket ID and status tracker link.
""",

    "making-a-card-payment.md": """# Making a card payment

Platforms: Flow
Tier: Common — assume it applies unless the product accepts no direct credit card payments; state the reason when excluding it.

The transaction flow for collecting, validating, processing, and confirming credit or debit card payments.

- [ ] **Form fields for card details** — Input fields for Card Number, Expiration Date, CVV, and Billing Zip Code.
- [ ] **Client-side Luhn validation** — Validating card number formatting and expiration dates before sending API request.
- [ ] **In-flight processing state** — Displaying full overlay or button loading spinner to prevent double submission while payment processes.
- [ ] **Clear transaction success state** — Immediate confirmation view confirming funds were charged with receipt details.
- [ ] **Detailed payment error handling** — Specific messages for declined cards, insufficient funds, or expired cards without exposing raw gateway errors.
""",

    "submitting-a-form.md": """# Submitting a form

Platforms: Flow
Tier: Fundamental — assume it applies to virtually every web and mobile form; state the reason if excluding it.

The end-to-end submit lifecycle handling form validation, submission loading states, and success/error feedback.

- [ ] **Explicit submit button** — Prominent submit button with copy adapted to form intent ("Save changes", "Send message").
- [ ] **In-flight submit loading state** — Disabling submit button and displaying loading spinner during network request.
- [ ] **Accessible success feedback** — Displaying clear success notification or redirecting upon successful submission.
- [ ] **Comprehensive error handling** — Presenting top-level alert summary and focusing the first invalid input on submission failure per [WCAG 2.1 SC 3.3.1, Error Identification](https://w3c.github.io/wcag/understanding/error-identification.html).
- [ ] **Form state preservation** — Retaining user-entered form data upon submission failure so users do not have to retype information.
"""
}

print(f"Total files defined in dict: {len(files_data)}")

for filename, content in files_data.items():
    filepath = os.path.join(references_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("All files written successfully!")
