from components import get_header, get_footer

def build_about():
    header = get_header("About Resida | Company & Mission", "about")
    footer = get_footer()
    body = """  <main>
    <!-- HERO SECTION -->
    <section class="section section-bg-surface" style="padding-top: 60px; padding-bottom: 60px; border-bottom: 1px solid var(--border-color);">
      <div class="container text-center">
        <div class="section-subtitle">Our Story & Heritage</div>
        <h1 class="section-title">Reimagining the Residential Tenancy Experience</h1>
        <p class="section-desc" style="max-width: 720px; margin: 0 auto;">
          Founded on the principle that renting a home should inspire dignity, transparency, and architectural joy, Resida is building the global gold standard for residential leasing.
        </p>
      </div>
    </section>

    <!-- HEADQUARTERS & STORY -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1000&q=80" alt="Resida headquarters architectural design office" class="feature-img" width="1000" height="687">
          </div>
          <div>
            <div class="section-subtitle">Born in 2021</div>
            <h2 class="section-title">From Frustration to Fiduciary Tenancy Standards</h2>
            <p>
              In 2021, our founders set out to dismantle the legacy rental market: deceptive listing bait-and-switches, predatory withheld deposits, and zero responsiveness when essential heating failed.
            </p>
            <p>
              We constructed a technology platform grounded in mandatory on-site physical inspections, legal deposit escrow protection, and a white-glove human concierge team that treats every renter as a valued resident, not a transaction.
            </p>
            <div class="grid grid-3 text-center mt-6">
              <div class="stat-card flex-col">
                <div class="stat-val" style="color: var(--primary);">40+</div>
                <div class="stat-lbl">Major Metros</div>
              </div>
              <div class="stat-card flex-col">
                <div class="stat-val" style="color: var(--accent);">$1.2B</div>
                <div class="stat-lbl">Leases Managed</div>
              </div>
              <div class="stat-card flex-col">
                <div class="stat-val" style="color: var(--secondary);">120+</div>
                <div class="stat-lbl">Team Members</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MODERN WORKSPACE & CULTURE -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">Collaborative Culture</div>
            <h2 class="section-title">Passionate Specialists in Architecture, Law & Hospitality</h2>
            <p>
              Our multidisciplinary team combines licensed building surveyors, real estate attorneys, software architects, and five-star hospitality veterans. We believe great service begins with a caring, empowered team culture.
            </p>
            <div class="check-list">
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Licensed Building Inspectors:</strong> Dedicated field surveyors inspecting properties in person every day.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>Tenant Legal Protections:</strong> Certified attorneys ensuring lease terms comply with tenant rights.</div></div>
              <div class="check-item"><div class="check-icon">✓</div><div><strong>24/7 Human Concierge:</strong> Responsive customer success advisors located in every active metro.</div></div>
            </div>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1000&q=80" alt="Resida team collaborating in modern conference room" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>

    <!-- MISSION & VISION -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=1000&q=80" alt="Sustainable modern residential living community" class="feature-img" width="1000" height="687">
          </div>
          <div>
            <div class="section-subtitle">Our Vision</div>
            <h2 class="section-title">Homes That Nurture Well-Being & Environmental Harmony</h2>
            <p>
              We actively prioritize energy-efficient buildings, certified green communities, solar infrastructure, and properties within walkable distance of clean rapid transit.
            </p>
            <p>
              By setting high structural benchmarks, we incentivize property owners to upgrade insulation, install heat pumps, and transition to smart, eco-conscious amenities.
            </p>
            <a href="browse.html" class="btn btn-primary mt-4">Explore Eco-Certified Rentals</a>
          </div>
        </div>
      </div>
    </section>

    <!-- LEADERSHIP & TEAM -->
    <section class="section section-bg-surface">
      <div class="container">
        <div class="section-header">
          <div class="section-subtitle">Executive Team</div>
          <h2 class="section-title">Meet the Leaders Guiding Resida</h2>
          <p class="section-desc">Decades of combined experience in high-end real estate, technology, and tenancy advocacy.</p>
        </div>

        <div class="grid grid-4">
          <!-- Member 1 -->
          <div class="step-card" style="text-align: center; padding: 24px;">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80" alt="Marcus Vance" style="width: 120px; height: 120px; border-radius: 9999px; object-fit: cover; margin: 0 auto 16px auto;" width="120" height="120">
            <h4 style="margin-bottom: 4px;">Marcus Vance</h4>
            <div style="font-size: 0.85rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">Founder & Chief Executive</div>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin: 0;">Former senior partner in metropolitan residential development with 18 years in urban asset management.</p>
          </div>

          <!-- Member 2 -->
          <div class="step-card" style="text-align: center; padding: 24px;">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=300&q=80" alt="Elena Rostova" style="width: 120px; height: 120px; border-radius: 9999px; object-fit: cover; margin: 0 auto 16px auto;" width="120" height="120">
            <h4 style="margin-bottom: 4px;">Elena Rostova</h4>
            <div style="font-size: 0.85rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">Head of Leasing Operations</div>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin: 0;">Oversees verified property inventory and broker partnerships across 40 metropolitan regions.</p>
          </div>

          <!-- Member 3 -->
          <div class="step-card" style="text-align: center; padding: 24px;">
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80" alt="Julian Thorne" style="width: 120px; height: 120px; border-radius: 9999px; object-fit: cover; margin: 0 auto 16px auto;" width="120" height="120">
            <h4 style="margin-bottom: 4px;">Julian Thorne</h4>
            <div style="font-size: 0.85rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">Chief Property Surveyor</div>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin: 0;">Chartered structural engineer directing our proprietary 150-Point Physical Inspection Protocols.</p>
          </div>

          <!-- Member 4 -->
          <div class="step-card" style="text-align: center; padding: 24px;">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80" alt="Chloe Bennett" style="width: 120px; height: 120px; border-radius: 9999px; object-fit: cover; margin: 0 auto 16px auto;" width="120" height="120">
            <h4 style="margin-bottom: 4px;">Chloe Bennett</h4>
            <div style="font-size: 0.85rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">VP Resident Experience</div>
            <p style="font-size: 0.82rem; color: var(--text-muted); margin: 0;">Hospitality specialist maintaining our 98.4% tenant satisfaction and on-demand concierge desk.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FIELD OPERATIONS & WORK WITH CLIENTS -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="feature-split">
          <div>
            <div class="section-subtitle">On-The-Ground Presence</div>
            <h2 class="section-title">Human Warmth Behind Modern Digital Convenience</h2>
            <p>
              Technology streamlines paperwork, but human care creates homes. Our field advisors meet tenants at the front door, walk through every lighting circuit and thermostat setting, and remain your dedicated point of contact throughout your entire lease.
            </p>
            <a href="contact.html" class="btn btn-primary mt-4">Contact Our Local Team</a>
          </div>
          <div class="feature-media">
            <img src="https://images.unsplash.com/photo-1577495508048-b635879837f1?auto=format&fit=crop&w=1000&q=80" alt="Resida specialist warmly greeting tenant at residence entrance" class="feature-img" width="1000" height="687">
          </div>
        </div>
      </div>
    </section>
  </main>"""
    return header + body + footer

def build_compare():
    header = get_header("Compare Rental Properties", "compare")
    footer = get_footer()
    # Add highlight differences toggle script
    toggle_script = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggleDiffBtn = document.getElementById('toggle-diff-btn');
      let diffOnly = false;

      toggleDiffBtn?.addEventListener('click', () => {
        diffOnly = !diffOnly;
        toggleDiffBtn.classList.toggle('active');
        const rows = document.querySelectorAll('.compare-table tbody tr');

        rows.forEach(row => {
          const cells = Array.from(row.querySelectorAll('td:not(:first-child)'));
          const texts = cells.map(c => c.textContent.trim());
          const isSame = texts.every(t => t === texts[0]);

          if (diffOnly && isSame) {
            row.style.opacity = '0.35';
          } else {
            row.style.opacity = '1';
          }
        });

        showToast(diffOnly ? 'Highlighting property differences' : 'Showing all features');
      });
    });
  </script>
</body>
</html>"""
    footer = footer.replace('</body>\n</html>', toggle_script)

    body = """  <main class="section-bg-muted" style="padding: 40px 0 80px 0;">
    <div class="container">
      <!-- Page Header -->
      <div class="flex-between items-center mb-8" style="flex-wrap: wrap; gap: 16px;">
        <div>
          <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 6px;">
            <a href="index.html">Home</a> / <span style="color: var(--text-main);">Property Comparison</span>
          </div>
          <h1 style="font-size: 2rem; margin-bottom: 4px;">Side-by-Side Property Comparison</h1>
          <p style="color: var(--text-secondary); margin: 0;">Comparing 3 selected residential rental properties across 15 crucial criteria.</p>
        </div>

        <div class="flex gap-3">
          <button id="toggle-diff-btn" class="btn btn-outline btn-sm">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            Highlight Differences
          </button>
          <a href="browse.html" class="btn btn-primary btn-sm">+ Add Another Property</a>
        </div>
      </div>

      <!-- Comparison Matrix Table -->
      <div class="compare-table-wrap">
        <table class="compare-table">
          <thead>
            <tr>
              <th style="vertical-align: bottom;">Feature / Metric</th>
              <!-- Property 1 -->
              <th class="compare-prop-header">
                <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=400&q=80" alt="The Grandview Skyline Penthouse" class="compare-prop-thumb">
                <h4 style="font-size: 1.05rem; margin-bottom: 4px;"><a href="property-details.html">The Grandview Penthouse</a></h4>
                <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary);">$4,850 <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">/ mo</span></div>
                <a href="property-details.html" class="btn btn-primary btn-sm mt-3" style="width: 100%;">Book Viewing</a>
              </th>

              <!-- Property 2 -->
              <th class="compare-prop-header">
                <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=400&q=80" alt="Greenwich Garden Loft Residence" class="compare-prop-thumb">
                <h4 style="font-size: 1.05rem; margin-bottom: 4px;"><a href="property-details.html">Greenwich Garden Loft</a></h4>
                <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary);">$3,200 <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">/ mo</span></div>
                <a href="property-details.html" class="btn btn-primary btn-sm mt-3" style="width: 100%;">Book Viewing</a>
              </th>

              <!-- Property 3 -->
              <th class="compare-prop-header">
                <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=400&q=80" alt="The Azure Waterfront Villa" class="compare-prop-thumb">
                <h4 style="font-size: 1.05rem; margin-bottom: 4px;"><a href="property-details.html">Azure Waterfront Villa</a></h4>
                <div style="font-size: 1.25rem; font-weight: 800; color: var(--primary);">$6,500 <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">/ mo</span></div>
                <a href="property-details.html" class="btn btn-primary btn-sm mt-3" style="width: 100%;">Book Viewing</a>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Security Deposit</td>
              <td>$4,850 (Escrow Protected)</td>
              <td>$3,200 (Escrow Protected)</td>
              <td>$6,500 (Escrow Protected)</td>
            </tr>
            <tr>
              <td>Property Type</td>
              <td>Penthouse Apartment</td>
              <td>Urban Industrial Loft</td>
              <td>Luxury Coastal Villa</td>
            </tr>
            <tr>
              <td>Bedrooms / Bathrooms</td>
              <td>3 Beds / 3 Baths</td>
              <td>2 Beds / 2 Baths</td>
              <td>4 Beds / 4 Baths</td>
            </tr>
            <tr>
              <td>Square Footage</td>
              <td>2,450 sq ft</td>
              <td>1,620 sq ft</td>
              <td>3,800 sq ft</td>
            </tr>
            <tr>
              <td>Neighborhood</td>
              <td>Downtown Financial Core</td>
              <td>Arts & Design Quarter</td>
              <td>Coastal Marina Bay</td>
            </tr>
            <tr>
              <td>Furnishing</td>
              <td>Designer Furnished</td>
              <td>Semi-Furnished</td>
              <td>Fully Furnished</td>
            </tr>
            <tr>
              <td>Pet Policy</td>
              <td>✓ Cats & Dogs (Up to 2)</td>
              <td>✓ Small Dogs Allowed</td>
              <td>✓ All Pets Welcome</td>
            </tr>
            <tr>
              <td>Parking Spaces</td>
              <td>2 Underground EV Stalls</td>
              <td>1 Dedicated Space</td>
              <td>Private 2-Car Garage</td>
            </tr>
            <tr>
              <td>Swimming Pool</td>
              <td>✓ Heated Rooftop Infinity</td>
              <td>✕ Not Included</td>
              <td>✓ Private Heated Pool</td>
            </tr>
            <tr>
              <td>Gym / Fitness</td>
              <td>✓ On-Site Wellness Spa</td>
              <td>✓ Boutique Resident Gym</td>
              <td>✓ Private Gym Studio</td>
            </tr>
            <tr>
              <td>Private Balcony/Terrace</td>
              <td>✓ Panoramic Skyline Wrap</td>
              <td>✓ Garden Courtyard Deck</td>
              <td>✓ Expansive Ocean Terrace</td>
            </tr>
            <tr>
              <td>WalkScore / TransitScore</td>
              <td><strong>98</strong> / <strong>95</strong></td>
              <td><strong>94</strong> / <strong>88</strong></td>
              <td><strong>76</strong> / <strong>70</strong></td>
            </tr>
            <tr>
              <td>Acoustic Quiet Score</td>
              <td>91/100 (Triple Paned)</td>
              <td>86/100 (Exposed Brick)</td>
              <td>96/100 (Private Grounds)</td>
            </tr>
            <tr>
              <td>Move-in Availability</td>
              <td><span class="badge badge-verified">Immediate</span></td>
              <td><span class="badge badge-verified">Immediate</span></td>
              <td><span class="badge badge-light">In 14 Days</span></td>
            </tr>
            <tr>
              <td>Action</td>
              <td><a href="property-details.html" class="btn btn-outline btn-sm" style="width: 100%;">View Full Listing</a></td>
              <td><a href="property-details.html" class="btn btn-outline btn-sm" style="width: 100%;">View Full Listing</a></td>
              <td><a href="property-details.html" class="btn btn-outline btn-sm" style="width: 100%;">View Full Listing</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>"""
    return header + body + footer

with open("pages/about.html", "w", encoding="utf-8") as f:
    f.write(build_about())

with open("pages/compare.html", "w", encoding="utf-8") as f:
    f.write(build_compare())

print("pages/about.html and pages/compare.html built successfully!")
