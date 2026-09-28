from components import get_header, get_footer

def build_home2():
    header = get_header("Home 2 - Executive Skyline & Luxury Living", "home")
    footer = get_footer()
    body = """  <main>
    <!-- HERO SECTION (HOME 2 - EXECUTIVE SKYLINE LIVING) -->
    <section class="hero-executive">
      <div class="container">
        <div class="hero-grid">
          <div>
            <div class="badge badge-pill badge-featured mb-4" style="background: rgba(2, 132, 199, 0.3); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8;">
              Executive & Relocation Portfolio
            </div>
            <h1 class="hero-title" style="color: #ffffff;">
              Metropolitan High-Rise Residences & Corporate Penthouses
            </h1>
            <p class="hero-subtitle" style="color: #94a3b8;">
              Curated long-term luxury residences for executives, creative visionaries, and relocating families. Fully furnished or bespoke empty sanctuaries with private concierge.
            </p>
            
            <div class="luxury-pills-bar">
              <div class="luxury-pill">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Doorman & Valet Included
              </div>
              <div class="luxury-pill">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Gigabit Symmetrical WiFi
              </div>
              <div class="luxury-pill">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
                Private Wellness Spa & Gym
              </div>
            </div>

            <div class="flex gap-4 mt-8" style="margin-top: 32px;">
              <a href="browse.html?type=penthouse" class="btn btn-primary btn-lg">Explore Skyline Residences</a>
              <a href="contact.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.3); color: #ffffff;">Book Private Tour</a>
            </div>
          </div>

          <div class="hero-image-wrap">
            <img src="../assets/images/executive-skyline-hero.jpg" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=1200&q=80';" alt="Modern luxury high-rise residential apartment towers and penthouses at twilight with illuminated skyline" class="hero-image-main" width="1200" height="675">
            <div class="hero-float-card bottom-left" style="background: rgba(15, 23, 42, 0.95); border-color: rgba(255,255,255,0.15);">
              <div class="stat-icon" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
              </div>
              <div>
                <div style="font-weight: 700; color: #ffffff;">Private Executive Concierge</div>
                <div style="font-size: 0.8rem; color: #94a3b8;">White-glove relocation assistance</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: CURATED COLLECTIONS -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Bespoke Living Spaces</div>
            <h2 class="section-title">Designed for Elevated Living & Productivity</h2>
            <p>Each executive residence features soundproof acoustic windows, architectural lighting, temperature-zoned suites, and custom Italian millwork engineered for peaceful rejuvenation.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Bespoke Interior Staging:</strong> Choose between designer-curated furniture packages or unfurnished blank canvases.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Dedicated Executive Home Offices:</strong> Ergonomic workstation setups with dual 4K monitor compatibility and private high-speed networking.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Panoramic City Horizons:</strong> Floor-to-ceiling glass expanses framing dramatic sunrise and twilight vistas.</div></div>
            </div>
            <a href="browse.html" class="btn btn-primary mt-4">View Curated Penthouse Collection</a>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf?auto=format&fit=crop&w=1000&q=80" alt="Minimalist luxury master bedroom with panoramic city views" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: SMART AMENITIES -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&w=1000&q=80" alt="Rooftop infinity swimming pool with urban skyline vista" class="feature-img" width="1000" height="687">
          </div>
          <div>
            <div class="section-subtitle">Resort-Grade Amenities</div>
            <h2 class="section-title">Rooftop Wellness Decks, Infinity Pools & Private Lounges</h2>
            <p>Access high-caliber community amenities that enrich your routine. From heated rooftop infinity pools overlooking the city skyline to infrared saunas and private boardrooms.</p>
            <div class="grid grid-2 mt-6">
              <div class="stat-card">
                <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/></svg></div>
                <div><div style="font-weight: 700;">Resident Skylounge</div><div style="font-size: 0.85rem; color: var(--text-muted);">Craft espresso & sommelier nights</div></div>
              </div>
              <div class="stat-card">
                <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
                <div><div style="font-weight: 700;">EV Fast Charging</div><div style="font-size: 0.85rem; color: var(--text-muted);">Dedicated stalls with auto-billing</div></div>
              </div>
            </div>
            <a href="services.html" class="btn btn-primary mt-6">Explore All Amenities</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: RAPID TENANT SCREENING -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Frictionless Approval</div>
            <h2 class="section-title">Rapid Digital Verification in 2 Hours or Less</h2>
            <p>We believe applying for a home should be as swift and respectful as modern banking. Our proprietary screening engine verifies income, identity, and tenancy track record in minutes without impacting credit scores.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Open Banking Integration:</strong> Secure read-only income verification without printing months of paper statements.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Soft Credit Inquiries:</strong> Your credit rating remains 100% protected throughout the pre-qualification phase.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>International Tenant Friendly:</strong> Expatriates and global professionals can qualify seamlessly with passport authentication.</div></div>
            </div>
            <a href="submit-listing.html" class="btn btn-primary mt-4">Pre-Qualify Now</a>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1000&q=80" alt="Professional young woman working in contemporary business lounge" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: NEIGHBORHOOD LIFE -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div class="feature-media">
            <img src="../assets/images/walkable-city-living.jpg" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=1000&q=80';" alt="Lively modern metropolitan pedestrian boulevard with cafes, sidewalks, trees and modern residential buildings" class="feature-img" width="1000" height="687">
          </div>
          <div>
            <div class="section-subtitle">Walkable City Living</div>
            <h2 class="section-title">Discover Neighborhoods by WalkScore & Transit Access</h2>
            <p>Location is everything. Every Resida listing includes detailed transit proximity ratings, walking times to artisan bakeries, green parks, international schools, and metro hubs.</p>
            <div class="flex gap-4 mt-6">
              <div class="spec-badge-box"><strong>98/100</strong> Walker's Paradise</div>
              <div class="spec-badge-box"><strong>95/100</strong> Transit Hub</div>
              <div class="spec-badge-box"><strong>88/100</strong> Biker's Dream</div>
            </div>
            <a href="blog.html" class="btn btn-outline mt-6">Read Neighborhood Guides</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: LANDLORD ADVISORY -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Asset Performance</div>
            <h2 class="section-title">Maximize Rental Yields with Professional Asset Management</h2>
            <p>Property owners and family offices partner with Resida to minimize vacancy rates, automate legal compliance, and attract reliable high-net-worth tenants.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>96.5% Average Occupancy:</strong> Zero long gap months between tenancies through predictive marketing.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Guaranteed On-Time Rent Payouts:</strong> Automated direct ACH disbursements on the 1st of every month.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Comprehensive Landlord Dashboard:</strong> Real-time tax reports, maintenance invoices, and lease renewal tracking.</div></div>
            </div>
            <a href="dashboard.html" class="btn btn-primary mt-4">Explore Landlord Portal</a>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=1000&q=80" alt="Experienced property consultant presenting investment insights" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>
  </main>"""
    return header + body + footer

with open("pages/home-2.html", "w", encoding="utf-8") as f:
    f.write(build_home2())

print("pages/home-2.html built successfully!")
