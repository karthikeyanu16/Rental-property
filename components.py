# Shared Layout Components for Resida Rental Property Platform

def get_header(title, active="home1", rel=".."):
    home1_active = "active" if active in ["home", "home1", "index"] else ""
    home2_active = "active" if active in ["home2", "home-2"] else ""
    properties_active = "active" if active in ["properties", "property-details", "browse"] else ""
    services_active = "active" if active in ["services", "service-details"] else ""
    about_active = "active" if active == "about" else ""
    blog_active = "active" if active in ["blog", "guides", "advice"] else ""
    contact_active = "active" if active == "contact" else ""

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Resida Rentals</title>
  <meta name="description" content="Discover, compare, and lease verified residential rental properties with instant digital contracts, zero hidden fees, and dedicated resident concierge.">
  <link rel="stylesheet" href="{rel}/assets/css/style.css">
  <link rel="stylesheet" href="{rel}/assets/css/dark-mode.css">
  <link rel="stylesheet" href="{rel}/assets/css/rtl.css">
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="topbar">
    <div class="container flex-between items-center">
      <div class="topbar-tools">
        <span class="topbar-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          +1 (800) 555-NEST
        </span>
        <span class="topbar-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          concierge@resida-rentals.com
        </span>
      </div>
      <div class="topbar-tools">
        <span>Verified Escrow Protection Guarantee</span>
        <span class="topbar-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          24/7 Tenancy Support
        </span>
      </div>
    </div>
  </div>

  <!-- Header Navigation -->
  <header class="site-header">
    <div class="container">
      <div class="nav-wrapper">
        <a href="{rel}/pages/index.html" class="brand-logo" aria-label="Resida Home">
          <div class="brand-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          </div>
          <span class="brand-text">Resida<span>.</span></span>
        </a>

        <!-- Main Navigation Links: Exactly 7 Clear Visible Items -->
        <nav class="main-nav" aria-label="Primary Navigation">
          <a href="{rel}/pages/index.html" class="nav-link {home1_active}">Home Page 1</a>
          <a href="{rel}/pages/home-2.html" class="nav-link {home2_active}">Home Page 2</a>
          <a href="{rel}/pages/properties.html" class="nav-link {properties_active}">Properties</a>
          <a href="{rel}/pages/services.html" class="nav-link {services_active}">Services</a>
          <a href="{rel}/pages/about.html" class="nav-link {about_active}">About</a>
          <a href="{rel}/pages/blog.html" class="nav-link {blog_active}">Blogs</a>
          <a href="{rel}/pages/contact.html" class="nav-link {contact_active}">Contact</a>
        </nav>

        <!-- Header Actions -->
        <div class="header-actions">
          <button id="rtl-toggle-btn" class="rtl-toggle-btn" title="Toggle Right-to-Left Layout" aria-label="Toggle RTL">RTL</button>
          <button id="theme-toggle-btn" class="theme-toggle-btn" title="Toggle Theme" aria-label="Toggle Theme">
            <span id="theme-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            </span>
          </button>
          <a href="{rel}/pages/properties.html" class="btn btn-primary btn-sm header-cta">Explore Properties</a>
          <button id="mobile-toggle-btn" class="mobile-toggle" aria-label="Open Navigation Menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Navigation -->
  <div id="mobile-drawer-overlay" class="mobile-drawer-overlay"></div>
  <aside id="mobile-drawer" class="mobile-drawer">
    <div class="flex-between items-center mb-6">
      <span class="brand-text">Resida<span>.</span></span>
      <button id="close-drawer-btn" class="btn-icon" aria-label="Close Navigation">✕</button>
    </div>
    <nav class="flex flex-col gap-2">
      <a href="{rel}/pages/index.html" class="nav-link {home1_active}">Home Page 1</a>
      <a href="{rel}/pages/home-2.html" class="nav-link {home2_active}">Home Page 2</a>
      <a href="{rel}/pages/properties.html" class="nav-link {properties_active}">Properties</a>
      <a href="{rel}/pages/services.html" class="nav-link {services_active}">Services</a>
      <a href="{rel}/pages/about.html" class="nav-link {about_active}">About</a>
      <a href="{rel}/pages/blog.html" class="nav-link {blog_active}">Blogs</a>
      <a href="{rel}/pages/contact.html" class="nav-link {contact_active}">Contact</a>
    </nav>
    <div style="margin-top: auto; padding-top: 24px;">
      <a href="{rel}/pages/properties.html" class="btn btn-primary" style="width: 100%;">Explore Properties</a>
    </div>
  </aside>
"""

def get_footer(rel=".."):
    return f"""  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a href="{rel}/pages/index.html" class="brand-logo mb-4" style="display: inline-flex;">
            <div class="brand-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            </div>
            <span class="brand-text" style="color: #ffffff;">Resida<span>.</span></span>
          </a>
          <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6; max-width: 320px;">
            The premier verified residential rental property platform. Connecting discerning tenants with authenticated residences with digital ease, transparency, and trust.
          </p>
        </div>

        <div class="footer-col">
          <h5>Quick Navigation</h5>
          <div class="footer-links">
            <a href="{rel}/pages/index.html">Home (Contemporary)</a>
            <a href="{rel}/pages/home-2.html">Home 2 (Skyline Living)</a>
            <a href="{rel}/pages/browse.html">Browse All Rentals</a>
            <a href="{rel}/pages/compare.html">Property Comparison</a>
            <a href="{rel}/pages/submit-listing.html">List Your Property</a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Services & Hub</h5>
          <div class="footer-links">
            <a href="{rel}/pages/services.html">Our Services</a>
            <a href="{rel}/pages/service-details.html">150-Point Inspection</a>
            <a href="{rel}/pages/about.html">About Resida</a>
            <a href="{rel}/pages/blog.html">Blogs & Rental Guides</a>
            <a href="{rel}/pages/contact.html">Contact Us</a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Stay Updated</h5>
          <p style="font-size: 0.88rem; color: #94a3b8; margin-bottom: 12px;">Subscribe for exclusive off-market rental drops and city market guides.</p>
          <form class="flex gap-2" action="#" method="POST">
            <input type="email" placeholder="Your email address" required style="padding: 10px 14px; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: #fff; font-size: 0.88rem; width: 100%;">
            <button type="submit" class="btn btn-primary btn-sm">Join</button>
          </form>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2026 Resida Properties Inc. All rights reserved. Registered Tenancy Platform.</div>
        <div class="flex gap-4">
          <a href="#" style="color: #94a3b8;">Privacy Policy</a>
          <a href="#" style="color: #94a3b8;">Terms of Service</a>
          <a href="#" style="color: #94a3b8;">Security & Escrow</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="{rel}/assets/js/main.js"></script>
</body>
</html>
"""
