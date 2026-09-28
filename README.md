# Resida — Modern Verified Rental Property Platform

> A clean, responsive, enterprise-grade HTML5/CSS3/Vanilla JS website template engineered for verified residential tenancy listings, digital escrow agreements, and seamless resident-landlord management.

---

## 🌟 Key Highlights & Architecture

- **14 Production-Ready Pages**:
  - `pages/index.html` — **Home 1 (Contemporary Living)**: Hero search bar, key statistics counters, 6 curated featured property cards, 3-step leasing flow, concierge feature banner, and resident testimonials.
  - `pages/home-2.html` — **Home 2 (Executive Skyline & Relocation)**: Twilight skyline hero, curated penthouses, 2-hour digital vetting guarantee, and corporate relocation services.
  - `pages/browse.html` — **Search & Filter Hub with Split Map**: Real-time filters (price range, property type, bedrooms, amenities, furnishing), grid/list toggles, and interactive Leaflet.js / OpenStreetMap map with property pins and preview cards.
  - `pages/property-details.html` — **"The Grandview Skyline Penthouse" Details**: 6-photo hero gallery, 150-point technical certification badge, 24-amenity checklist, walk/transit scores, interactive monthly cost calculator, and sticky tour booking card with modal.
  - `pages/services.html` — **Rental Services & Fee Calculator**: 6 core service modules, dynamic property management fee calculator, and interactive FAQ accordion.
  - `pages/service-details.html` — **150-Point Certified Inspection**: Deep dive into structural, electrical, plumbing/HVAC, and digital lock move-in security audits.
  - `pages/about.html` — **About Resida**: Heritage story, 4 leadership portraits (CEO, Head of Leasing, Chief Surveyor, Resident VP), sustainable living vision, and collaborative workspace.
  - `pages/compare.html` — **Side-by-Side Comparison Matrix**: 3-property comparative audit across 15 criteria with "Highlight Differences" toggle and direct booking actions.
  - `pages/submit-listing.html` — **Multi-Step Listing Submission Wizard**: 4-step progress stepper (General Info, Specs & Pricing, Amenities & Uploads, Final Confirmation) with drag-and-drop media upload simulation.
  - `pages/dashboard.html` — **Landlord & Tenant Portal**: Dual-view switcher, pure HTML5 Canvas revenue & inquiry analytics chart, active listings table with filterable badges, viewing requests queue with instant action triggers, and tenant lease management.
  - `pages/blog.html` — **Editorial Insights & Guides**: 6 comprehensive articles on tenant rights, daylight optimization, waterfront rentals, lease negotiations, pet living, and smart locks.
  - `pages/contact.html` — **Contact & Viewing Concierge**: Multi-department validated inquiry form, 3 flagship global pavilions (New York, San Francisco, London), and 24/7 emergency dispatch.
  - `pages/404.html` — **Custom Error Page**: Architectural visual, instant search bar, and recovery navigation.
  - `pages/coming-soon.html` — **Pre-Launch Page**: Real-time countdown timer, feature badges, and early access waitlist form.
  - `index.html` — **Root Mirror**: Seamless entry point for root server directories.

- **100% Unique Image Guarantee**:
  - Over **90 curated, high-resolution architectural, interior, urban, and professional portrait photographs** from Unsplash.
  - **Zero image duplication** across pages or sections.
  - Strictly no cartoon graphics, no emojis as UI icons, and no unrelated stock imagery.
  - Balanced aspect ratios and responsive image scaling that never obscures typography or interfaces.

- **Theme & Internationalization Engine**:
  - **Dark / Light Theme Toggle**: Persistent via `localStorage`, zero-flash loading, with fallback to system `prefers-color-scheme`.
  - **Full RTL (Right-to-Left) Mirroring**: Comprehensive `assets/css/rtl.css` supporting Arabic, Hebrew, and Persian layouts with instant header toggle.

- **Interactive Zero-Dependency JavaScript**:
  - Client-side form validation with accessible error messaging.
  - Interactive toast notifications (`showToast(msg, type)`).
  - Modal manager with keyboard escape (`Esc`) and outside-click dismissal.
  - Pure HTML5 Canvas line/area chart (no Chart.js or D3 weight required).
  - Favorites shortlist manager with count badge and notification.
  - Property comparison tray.

---

## 📁 Project Directory Structure

```
rental-property-platform/
│
├── index.html                   # Root landing page (Home 1 mirror)
├── robots.txt                   # Search engine crawler directives
├── sitemap.xml                  # XML sitemap indexing all 14 pages
├── README.md                    # Root overview and quick start guide
│
├── assets/
│   ├── css/
│   │   ├── style.css            # Core design system, variables, layouts & components
│   │   ├── dark-mode.css        # High-contrast dark theme variables and overrides
│   │   └── rtl.css              # Bidirectional RTL mirror styles
│   │
│   └── js/
│       ├── main.js              # Theme switcher, RTL toggle, modals, toasts, drawer, counters
│       └── dashboard.js         # Landlord/tenant switcher, HTML5 canvas chart, inquiry queue
│
├── pages/
│   ├── index.html               # Home 1 - Contemporary Living
│   ├── home-2.html              # Home 2 - Executive Skyline & Relocation
│   ├── browse.html              # Search & Filter with Split Interactive Map
│   ├── property-details.html    # Listing showcase, specs, calculator & booking modal
│   ├── services.html            # 6 services, dynamic fee calculator & FAQ accordion
│   ├── service-details.html     # 150-Point Certified Inspection technical overview
│   ├── about.html               # Company narrative, leadership team & eco pillars
│   ├── compare.html             # 3-property comparative matrix with diff highlight
│   ├── submit-listing.html      # 4-step property owner onboarding wizard
│   ├── dashboard.html           # Dual-portal landlord/tenant analytics & actions
│   ├── blog.html                # Editorial guides, tenant legal rights & advice
│   ├── contact.html             # Multi-department contact form & flagship offices
│   ├── 404.html                 # Custom 404 error page with search bar
│   └── coming-soon.html         # Pre-launch countdown timer & waitlist capture
│
└── documentation/
    └── README.md                # Comprehensive developer & designer specification manual
```

---

## 🎨 Design System & Variables

The styling framework is organized around modular CSS custom properties defined in `assets/css/style.css`:

```css
:root {
  --primary: #2563eb;          /* Trust Blue */
  --primary-hover: #1d4ed8;
  --secondary: #0f172a;        /* Deep Slate */
  --accent: #f59e0b;           /* Warm Amber */
  --bg-main: #f8fafc;          /* Light Cloud */
  --bg-surface: #ffffff;       /* Pure White */
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --border-color: #e2e8f0;
  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Inter', sans-serif;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.1);
}
```

---

## 📱 Responsive Breakpoints

The template has been tested and tuned for four device tiers:

| Breakpoint | Target Form Factor | Layout Behaviors |
| :--- | :--- | :--- |
| `< 640px` | Mobile Phones | 1-column stack, mobile drawer nav, full-width buttons, touch-friendly 44px tap targets |
| `640px – 1024px` | Tablets & Portrait Displays | 2-column property cards, collapsible filter drawer on browse, responsive tables with horizontal scroll |
| `1024px – 1280px` | Laptops & Desktop Monitors | Full navigation menu with dropdowns, 3-column grids, split-screen interactive map layout |
| `> 1280px` | Ultra-Wide & 4K Displays | Max-width content container (1240px) centered with comfortable margins |

---

## 🚀 Getting Started & Local Preview

No build step or Node.js server is required. To view the website locally:

### Option A: Direct Browser File Launch
Simply double-click `index.html` or any page inside `pages/` (e.g. `pages/index.html`) in any modern web browser (Chrome, Edge, Firefox, Safari).

### Option B: Local HTTP Server (Python)
Run the following in PowerShell from the project root:

```powershell
python -m http.server 8000
```
Then navigate to:
```
http://localhost:8000
```

### Option C: VS Code Live Server
Right-click `index.html` and choose **"Open with Live Server"**.

---

## 🛡️ License & Attributions

- **Code & Architecture**: © 2026 Resida Properties Inc.
- **Typography**: Google Fonts ([Inter](https://fonts.google.com/specimen/Inter), [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans)).
- **Imagery**: Curated professional architectural, interior, and portrait photography from [Unsplash](https://unsplash.com) under the Unsplash License (free for commercial and personal use).
- **Mapping**: [Leaflet.js](https://leafletjs.com/) and [OpenStreetMap](https://www.openstreetmap.org/) contributors.
