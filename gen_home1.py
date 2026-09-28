from components import get_header, get_footer

def build_home1():
    header = get_header("Home 1 - Contemporary Living", "home")
    footer = get_footer()
    body = """  <main>
    <!-- HERO SECTION (HOME 1) -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-content">
            <div class="section-subtitle">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
              Next-Generation Rental Platform
            </div>
            <h1 class="hero-title">
              Find Verified <span class="highlight">Sanctuary Rentals</span> in Prime Neighborhoods
            </h1>
            <p class="hero-subtitle">
              Discover architect-designed apartments, luxury townhomes, and modern lofts with certified 150-point inspections, digital lease signing, and zero broker markups.
            </p>

            <div class="hero-search-box">
              <div class="search-tabs">
                <button class="search-tab-btn active">All Residences</button>
                <button class="search-tab-btn">Apartments</button>
                <button class="search-tab-btn">Villas</button>
                <button class="search-tab-btn">Urban Lofts</button>
              </div>
              <form action="browse.html" method="GET" class="search-fields-grid" data-no-ajax="true">
                <div class="search-field">
                  <label for="search-location">Location</label>
                  <input type="text" id="search-location" name="location" placeholder="Neighborhood or City" value="Downtown Central">
                </div>
                <div class="search-field">
                  <label for="search-type">Property Type</label>
                  <select id="search-type" name="type">
                    <option value="">Any Type</option>
                    <option value="apartment" selected>Apartment</option>
                    <option value="villa">Luxury Villa</option>
                    <option value="loft">Designer Loft</option>
                    <option value="studio">Modern Studio</option>
                  </select>
                </div>
                <div class="search-field">
                  <label for="search-budget">Monthly Rent</label>
                  <select id="search-budget" name="price">
                    <option value="1500-2500">$1,500 - $2,500</option>
                    <option value="2500-4500" selected>$2,500 - $4,500</option>
                    <option value="4500-8000">$4,500 - $8,000</option>
                    <option value="8000+">$8,000+</option>
                  </select>
                </div>
                <div class="search-field">
                  <label for="search-beds">Bedrooms</label>
                  <select id="search-beds" name="beds">
                    <option value="1">1 Bed</option>
                    <option value="2" selected>2 Beds</option>
                    <option value="3">3 Beds</option>
                    <option value="4+">4+ Beds</option>
                  </select>
                </div>
                <div>
                  <button type="submit" class="btn btn-primary" style="height: 44px; width: 100%;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    Find Rentals
                  </button>
                </div>
              </form>
            </div>
          </div>

          <div class="hero-image-wrap">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80" alt="Sunlit luxury modern villa with pristine swimming pool" class="hero-image-main" width="1200" height="825">
            <div class="hero-float-card top-right">
              <div class="stat-icon" style="width: 44px; height: 44px;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <div>
                <div style="font-weight: 700; font-size: 0.95rem; color: var(--text-main);">100% Escrow Protected</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Deposits held in regulated trust</div>
              </div>
            </div>
            <div class="hero-float-card bottom-left">
              <div class="stat-icon" style="width: 44px; height: 44px; background: var(--accent-light); color: var(--accent);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
              </div>
              <div>
                <div style="font-weight: 700; font-size: 0.95rem; color: var(--text-main);">4.98 / 5 Rating</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">From 4,200+ verified residents</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- KEY STATS STRIP -->
    <section class="section-sm section-bg-surface" style="border-bottom: 1px solid var(--border-color);">
      <div class="container">
        <div class="grid grid-4 text-center">
          <div><div class="stat-val"><span class="counter-val" data-target="18500">18,500</span>+</div><div class="stat-lbl">Active Verified Listings</div></div>
          <div><div class="stat-val"><span class="counter-val" data-target="98">98</span>.4%</div><div class="stat-lbl">Tenant Satisfaction Score</div></div>
          <div><div class="stat-val"><span class="counter-val" data-target="24">24</span>h</div><div class="stat-lbl">Average Fast-Track Approval</div></div>
          <div><div class="stat-val">$<span class="counter-val" data-target="0">0</span></div><div class="stat-lbl">Hidden Broker Markups</div></div>
        </div>
      </div>
    </section>

    <!-- MAIN SERVICE -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1000&q=80" alt="Bright modern Scandinavian apartment living room" class="feature-img" width="1000" height="687">
            <div class="feature-badge-box">
              <div class="num">150</div>
              <div class="lbl">Point Inspection Passed</div>
            </div>
          </div>
          <div>
            <div class="section-subtitle">Core Platform Capability</div>
            <h2 class="section-title">Verified Property Rentals with Certified Quality Standards</h2>
            <p>Every rental residence on Resida undergoes an exhaustive on-site evaluation by certified property inspectors before publication, ensuring complete transparency.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Acoustic & Insulation Audit:</strong> We test sound transmission levels from neighboring units and street noise.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Electrical & Appliance Diagnostics:</strong> HVAC, refrigeration, water pressure, and heating systems are tested under load.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Legal Ownership & Title Verification:</strong> Complete background checks guaranteeing you deal directly with genuine property owners.</div></div>
            </div>
            <div class="flex gap-4 mt-6">
              <a href="service-details.html" class="btn btn-primary">Learn About Our 150-Point Standard</a>
              <a href="browse.html" class="btn btn-outline">Explore Verified Homes</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURED PROPERTIES -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="section-header">
          <div class="section-subtitle">Curated Residences</div>
          <h2 class="section-title">Featured Residential Rentals</h2>
          <p class="section-desc">Hand-picked properties offering the pinnacle of design, comfort, location, and verified tenant terms.</p>
        </div>
        <div class="grid grid-3">
          <article class="property-card">
            <div class="property-thumb-wrap">
              <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80" alt="The Skyline Penthouse glass balcony" class="property-thumb" width="800" height="500">
              <div class="property-badges"><span class="badge badge-featured">Featured</span><span class="badge badge-verified">Verified</span></div>
              <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
              <div class="property-price-tag">$4,850<span>/mo</span></div>
            </div>
            <div class="property-body">
              <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Downtown Financial District</div>
              <h3 class="property-title"><a href="property-details.html">The Grandview Skyline Penthouse</a></h3>
              <div class="property-specs">
                <div class="spec-item">3 Beds</div><div class="spec-item">3 Baths</div><div class="spec-item">2,450 sq ft</div>
              </div>
              <div class="property-footer">
                <div class="property-agent"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=80" alt="Marcus Vance" class="agent-avatar" width="32" height="32"><span class="agent-name">Marcus Vance</span></div>
                <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-1" data-title="The Grandview Skyline Penthouse"> Compare</label>
              </div>
            </div>
          </article>
          <article class="property-card">
            <div class="property-thumb-wrap">
              <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80" alt="Greenwich Garden Loft interior" class="property-thumb" width="800" height="500">
              <div class="property-badges"><span class="badge badge-hot">Popular</span><span class="badge badge-verified">Verified</span></div>
              <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
              <div class="property-price-tag">$3,200<span>/mo</span></div>
            </div>
            <div class="property-body">
              <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Arts Quarter, West End</div>
              <h3 class="property-title"><a href="property-details.html">Greenwich Garden Loft Residence</a></h3>
              <div class="property-specs">
                <div class="spec-item">2 Beds</div><div class="spec-item">2 Baths</div><div class="spec-item">1,620 sq ft</div>
              </div>
              <div class="property-footer">
                <div class="property-agent"><img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=100&q=80" alt="Elena Rostova" class="agent-avatar" width="32" height="32"><span class="agent-name">Elena Rostova</span></div>
                <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-2" data-title="Greenwich Garden Loft Residence"> Compare</label>
              </div>
            </div>
          </article>
          <article class="property-card">
            <div class="property-thumb-wrap">
              <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=800&q=80" alt="The Azure Waterfront Villa" class="property-thumb" width="800" height="500">
              <div class="property-badges"><span class="badge badge-featured">Featured</span><span class="badge badge-verified">Verified</span></div>
              <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
              <div class="property-price-tag">$6,500<span>/mo</span></div>
            </div>
            <div class="property-body">
              <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Coastal Marina Bay</div>
              <h3 class="property-title"><a href="property-details.html">The Azure Waterfront Villa</a></h3>
              <div class="property-specs">
                <div class="spec-item">4 Beds</div><div class="spec-item">4 Baths</div><div class="spec-item">3,800 sq ft</div>
              </div>
              <div class="property-footer">
                <div class="property-agent"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&q=80" alt="Julian Thorne" class="agent-avatar" width="32" height="32"><span class="agent-name">Julian Thorne</span></div>
                <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-3" data-title="The Azure Waterfront Villa"> Compare</label>
              </div>
            </div>
          </article>
        </div>
        <div class="text-center mt-12" style="margin-top: 48px;">
          <a href="browse.html" class="btn btn-outline btn-lg">View All 1,480+ Available Listings</a>
        </div>
      </div>
    </section>

    <!-- KEY BENEFITS -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Unmatched Rental Security</div>
            <h2 class="section-title">Zero Hidden Fees & Instant Digital Keyless Leases</h2>
            <p>We eliminated bureaucratic paperwork, arbitrary broker commissions, and predatory deposit deductions. Every lease on Resida is legally binding, transparently governed, and smartphone accessible.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Regulated Deposit Escrow:</strong> Your security deposit is securely held in an interest-bearing escrow account governed by local tenancy statutes.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Keyless Smartphone Move-In:</strong> Pre-programmed encrypted smart access codes dispatched directly to your authenticated device upon lease activation.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Transparent Price Breakdown:</strong> Clear, upfront line items for monthly rent, building HOA dues, high-speed fiber internet, and parking.</div></div>
            </div>
            <a href="services.html" class="btn btn-primary mt-4">Discover Resident Protections</a>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1000&q=80" alt="Smart keyless digital lock on modern apartment door" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="section-header">
          <div class="section-subtitle">Simple 3-Step Process</div>
          <h2 class="section-title">How Resida Works for Renters</h2>
          <p class="section-desc">From initial discovery to unlocking your new front door in as little as 48 hours.</p>
        </div>
        <div class="steps-grid">
          <div class="step-card">
            <div class="step-num">1</div>
            <div class="step-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
            <h4>Search & Filter</h4>
            <p>Filter by exact neighborhood, monthly budget, pet policy, floor level, and specific amenities with real-time availability updates.</p>
          </div>
          <div class="step-card">
            <div class="step-num">2</div>
            <div class="step-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg></div>
            <h4>Tour in 3D or In-Person</h4>
            <p>Book instant guided VIP walk-throughs with licensed Resida neighborhood specialists or explore high-res spatial 360° virtual tours.</p>
          </div>
          <div class="step-card">
            <div class="step-num">3</div>
            <div class="step-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div>
            <h4>Digital Sign & Move-In</h4>
            <p>Complete fast-track screening, sign digital lease documents in minutes, and receive encrypted smart-key door access codes.</p>
          </div>
        </div>

        <div class="feature-split mt-16" style="margin-top: 64px;">
          <div><img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1000&q=80" alt="Professional real estate agent showing digital tour on tablet to client" class="feature-img" width="1000" height="687"></div>
          <div>
            <div class="section-subtitle">Dedicated Resident Experience</div>
            <h3 class="mb-4">Personalized Leasing Guidance on Every Step</h3>
            <p>Whether you are relocating across town or moving from another country, our team of dedicated residential advisors coordinates viewing schedules, handles utility setup, and ensures your transition into your new home is seamless.</p>
            <a href="contact.html" class="btn btn-primary mt-2">Book a Consultation</a>
          </div>
        </div>
      </div>
    </section>

    <!-- WHY CHOOSE US -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Peace of Mind</div>
            <h2 class="section-title">Why Renters & Owners Choose Resida</h2>
            <p>We bridge the gap between quality-conscious tenants and responsible property owners with unmatched technology, verified inventory, and 24/7 localized support.</p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>24/7 On-Demand Maintenance:</strong> Submit maintenance tickets directly via the resident dashboard with guaranteed emergency dispatch within 60 minutes.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>No Surprise Rent Hikes:</strong> Multi-year lease stability agreements with pre-agreed inflation caps protect your long-term household budget.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Tenant Concierge Desk:</strong> From dry-cleaning parcel collection to booked private amenity spaces, enjoy hotel-grade residential service.</div></div>
            </div>
            <div class="flex gap-4 mt-6">
              <a href="about.html" class="btn btn-primary">Our Company Story</a>
              <a href="dashboard.html" class="btn btn-outline">Preview Resident Portal</a>
            </div>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80" alt="Uniformed residential concierge welcoming guest in marble foyer" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>

    <!-- CUSTOMER EXPERIENCE -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="section-header">
          <div class="section-subtitle">Real Resident Stories</div>
          <h2 class="section-title">Experiences That Speak For Themselves</h2>
          <p class="section-desc">Read how Resida transformed the rental experience for thousands of city dwellers.</p>
        </div>
        <div class="grid grid-2 items-center mb-12">
          <div><img src="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1000&q=80" alt="Delighted residents relaxing in their new sunlit living room" class="feature-img" width="1000" height="687"></div>
          <div class="flex flex-col gap-6">
            <div class="testimonial-card">
              <div class="stars">★★★★★</div>
              <p class="testimonial-text">"Finding an apartment in downtown used to be an exhausting nightmare of fake photos and hidden fees. Resida was a breath of fresh air. The 3D tour was 100% accurate, the lease took 10 minutes to sign on my phone, and my deposit is safely escrowed."</p>
              <div class="testimonial-author">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=120&q=80" alt="Sarah Jenkins" class="author-avatar" width="50" height="50">
                <div><div style="font-weight: 700; color: var(--text-main);">Sarah Jenkins</div><div style="font-size: 0.85rem; color: var(--text-muted);">Resident at The Grandview Penthouse</div></div>
              </div>
            </div>
            <div class="testimonial-card">
              <div class="stars">★★★★★</div>
              <p class="testimonial-text">"As an owner of 8 boutique rental units, listing on Resida reduced my vacant days from 45 to just 4. Their tenant screening is thorough, and the automated rent disbursement in the dashboard gives me total visibility."</p>
              <div class="testimonial-author">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80" alt="David Sterling" class="author-avatar" width="50" height="50">
                <div><div style="font-weight: 700; color: var(--text-main);">David Sterling</div><div style="font-size: 0.85rem; color: var(--text-muted);">Property Owner & Asset Manager</div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FLOATING COMPARE BOTTOM BAR -->
    <div id="compare-float-bar" class="compare-float-bar">
      <span><strong id="compare-count">0</strong> properties selected</span>
      <a href="compare.html" class="btn btn-primary btn-sm">Compare Now</a>
    </div>

    <!-- CTA BANNER -->
    <section class="section" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff;">
      <div class="container text-center">
        <h2 style="color: #ffffff; margin-bottom: 16px;">Ready to Find Your Next Sanctuary?</h2>
        <p style="color: #e0f2fe; max-width: 600px; margin: 0 auto 32px auto; font-size: 1.1rem;">
          Join over 18,000 satisfied tenants and property owners experiencing verified, seamless residential rentals today.
        </p>
        <div class="flex flex-center gap-4">
          <a href="browse.html" class="btn btn-white btn-lg">Browse Listings Now</a>
          <a href="submit-listing.html" class="btn btn-secondary btn-lg" style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255,255,255,0.3);">List Your Property</a>
        </div>
      </div>
    </section>
  </main>"""
    return header + body + footer

with open("pages/index.html", "w", encoding="utf-8") as f:
    f.write(build_home1())

print("pages/index.html built successfully!")
