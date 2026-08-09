import os
import re

references_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references")

expected_table = [
    # Cross-cutting
    ("Account", "Common", "Mobile, Web app", "account.md"),
    ("Settings", "Common", "Mobile, Web app", "settings.md"),
    ("Search", "Conditional", "Mobile, Website", "search.md"),
    ("Cart", "Conditional", "Mobile, Website", "cart.md"),

    # Mobile app only
    ("Gesture navigation", "Common", "Mobile", "gesture-navigation.md"),
    ("Splash Screen", "Fundamental", "Mobile", "splash-screen.md"),
    ("Checkout", "Common", "Mobile", "checkout.md"),
    ("Tab Bar Navigation", "Common", "Mobile", "tab-bar-navigation.md"),
    ("In-App Notifications", "Common", "Mobile", "in-app-notifications.md"),
    ("Action Sheet", "Common", "Mobile", "action-sheet.md"),
    ("Camera", "Conditional", "Mobile", "camera.md"),
    ("Map View", "Conditional", "Mobile", "map-view.md"),
    ("Onboarding Checklist", "Conditional", "Mobile", "onboarding-checklist.md"),
    ("Paywall", "Conditional", "Mobile", "paywall.md"),
    ("Onboarding", "Common", "Mobile", "onboarding.md"),
    ("Chat", "Conditional", "Mobile", "chat.md"),
    ("In-App Browser", "Conditional", "Mobile", "in-app-browser.md"),
    ("Invite", "Conditional", "Mobile", "invite.md"),

    # Web app only
    ("2FA", "Common", "Web app", "2fa.md"),
    ("Notification Settings", "Common", "Web app", "notification-settings.md"),
    ("Help Center", "Common", "Web app", "help-center.md"),
    ("User Management", "Conditional", "Web app", "user-management.md"),
    ("Single Item Detail", "Common", "Web app", "single-item-detail.md"),
    ("Admin Panel", "Conditional", "Web app", "admin-panel.md"),
    ("Empty State", "Fundamental", "Web app", "empty-state.md"),

    # Website only
    ("Security", "Fundamental", "Website", "security.md"),
    ("About", "Common", "Website", "about.md"),
    ("Privacy", "Fundamental", "Website", "privacy.md"),
    ("Features", "Common", "Website", "features.md"),
    ("Testimonials", "Common", "Website", "testimonials.md"),
    ("Affiliate", "Conditional", "Website", "affiliate.md"),
    ("Compare", "Conditional", "Website", "compare.md"),
    ("Status", "Common", "Website", "status.md"),
    ("Press / Media", "Conditional", "Website", "press-media.md"),
    ("Waitlist", "Conditional", "Website", "waitlist.md"),
    ("Team", "Common", "Website", "team.md"),
    ("Careers", "Conditional", "Website", "careers.md"),
    ("Blog Post", "Conditional", "Website", "blog-post.md"),
    ("Contact Us", "Fundamental", "Website", "contact-us.md"),
    ("Pricing", "Common", "Website", "pricing.md"),
    ("FAQ", "Common", "Website", "faq.md"),
    ("404", "Fundamental", "Website", "404.md"),
    ("Blog", "Conditional", "Website", "blog.md"),
    ("Sign up", "Common", "Website", "sign-up.md"),

    # Flow only
    ("Adding to cart", "Conditional", "Flow", "adding-to-cart.md"),
    ("Uploading media", "Conditional", "Flow", "uploading-media.md"),
    ("Verifying account", "Common", "Flow", "verifying-account.md"),
    ("Canceling subscription", "Conditional", "Flow", "canceling-subscription.md"),
    ("Filtering items", "Conditional", "Flow", "filtering-items.md"),
    ("Saving changes", "Fundamental", "Flow", "saving-changes.md"),
    ("Entering promo code", "Conditional", "Flow", "entering-promo-code.md"),
    ("Showing input error", "Fundamental", "Flow", "showing-input-error.md"),
    ("Resetting password", "Common", "Flow", "resetting-password.md"),
    ("Deleting account", "Fundamental", "Flow", "deleting-account.md"),
    ("Contacting support", "Common", "Flow", "contacting-support.md"),
    ("Making a card payment", "Common", "Flow", "making-a-card-payment.md"),
    ("Submitting a form", "Fundamental", "Flow", "submitting-a-form.md"),
]

errors = []

for name, tier, platforms, filename in expected_table:
    filepath = os.path.join(references_dir, filename)
    if not os.path.exists(filepath):
        errors.append(f"Missing file: {filename}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    
    # Check title
    expected_h1 = f"# {name}"
    if lines[0] != expected_h1:
        errors.append(f"{filename}: Title mismatch. Expected '{expected_h1}', got '{lines[0]}'")
    
    # Check platforms
    expected_plat = f"Platforms: {platforms}"
    if lines[1] != expected_plat:
        errors.append(f"{filename}: Platforms mismatch. Expected '{expected_plat}', got '{lines[1]}'")
    
    # Check tier
    if not lines[2].startswith(f"Tier: {tier} — "):
        errors.append(f"{filename}: Tier mismatch. Expected start 'Tier: {tier} — ', got '{lines[2]}'")
    
    # Check items
    items = [l for l in lines if l.startswith("- [ ]")]
    if len(items) < 5 or len(items) > 15:
        errors.append(f"{filename}: Item count out of range (5-15): got {len(items)}")
    
    for item in items:
        if not re.match(r"^- \[ \] \*\*[^\*]+\*\* — .+$", item):
            errors.append(f"{filename}: Item format mismatch: '{item[:50]}...'")

print(f"Checked {len(expected_table)} files.")
if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for err in errors:
        print(" -", err)
else:
    print("ALL 57 FILES PASSED VERIFICATION PERFECTLY!")
