# Map View

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
