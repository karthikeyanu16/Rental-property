from components import get_header, get_footer

def build_services():
    header = get_header("Our Rental & Management Services", "services")
    footer = get_footer()
    body = """  <main>
    <!-- HERO SECTION -->
    <section class="section section-bg-surface" style="padding-top: 60px; padding-bottom: 60px; border-bottom: 1px solid var(--border-color);">
      <div class="container text-center">
        <div class="section-subtitle">Comprehensive Solutions</div>
        <h1 class="section-title">Specialized Services for Discerning Tenants & Property Owners</h1>
        <p class="section-desc" style="margin: 0 auto; max-width: 680px;">
          From verified tenant placement and immersive spatial tours to 24/7 emergency dispatch and fiduciary escrow management.
        </p>
      </div>
    </section>

    <!-- 6 CORE SERVICE CATEGORIES -->
    <section class="section section-bg-muted">
      <div class="container">
        <div class="grid grid-3">
          <!-- Service 1 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1560520653-9e0e4c89eb11?auto=format&fit=crop&w=800&q=80" alt="Agent passing keys into tenant hands" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Tenancy Advisory</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">Residential Tenant Placement</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                Tailored matching connecting pre-qualified tenants with vetted boutique landlords. Rapid 2-hour digital screening and zero arbitrary application charges.
              </p>
              <a href="service-details.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Service Details →</a>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1593508512255-86ab42a8e620?auto=format&fit=crop&w=800&q=80" alt="High-tech 3D camera setup in sleek apartment" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Virtual Reality</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">360° Virtual & Guided VIP Tours</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                Explore every square inch with accurate LiDAR spatial scans and interactive floorplan measurement tools, or schedule a personal private walk-through.
              </p>
              <a href="contact.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Schedule VIP Tour →</a>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&q=80" alt="Executive signing legal contract with fountain pen" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Legal Escrow</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">Digital Lease & Deposit Escrow</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                Legally binding digital lease agreements authenticated via cryptographic signatures. Security deposits are safeguarded in audited escrow accounts.
              </p>
              <a href="service-details.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Escrow Guarantees →</a>
            </div>
          </div>

          <!-- Service 4 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=800&q=80" alt="Certified technician inspecting air conditioning unit" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Maintenance</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">24/7 On-Demand Property Repairs</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                Rapid dispatch network of certified electricians, plumbers, and HVAC specialists available around the clock with a 60-minute emergency SLA.
              </p>
              <a href="contact.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Emergency Support →</a>
            </div>
          </div>

          <!-- Service 5 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" alt="Financial performance graphs and real estate portfolio analysis" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Asset Management</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">End-to-End Landlord Asset Care</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                Complete portfolio administration: automated rent collection, yield optimization, tenant communication, regulatory filings, and tax reporting.
              </p>
              <a href="dashboard.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Owner Solutions →</a>
            </div>
          </div>

          <!-- Service 6 -->
          <div class="service-feature-card">
            <div class="card-media">
              <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=800&q=80" alt="Interior designer styling luxury furniture and decor" width="800" height="500">
            </div>
            <div class="card-content">
              <div class="badge badge-light badge-pill mb-2" style="align-self: flex-start;">Concierge</div>
              <h3 style="font-size: 1.25rem; margin-bottom: 8px;">White-Glove Relocation & Staging</h3>
              <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 16px;">
                From bespoke furniture rental packages to utility concierge and moving day coordination, settle effortlessly into your new city.
              </p>
              <a href="contact.html" class="btn btn-outline btn-sm mt-auto" style="align-self: flex-start;">Relocation Help →</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SERVICE FEE CALCULATOR WIDGET -->
    <section class="section section-bg-surface">
      <div class="container" style="max-width: 800px;">
        <div class="section-header">
          <div class="section-subtitle">Transparent Pricing</div>
          <h2 class="section-title">Rental Service Fee Estimator</h2>
          <p class="section-desc">Estimate your transparent leasing & management fees with zero hidden clauses.</p>
        </div>

        <div style="background: var(--bg-muted); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 32px;">
          <div class="mb-4">
            <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Expected Monthly Rent</label>
            <input type="number" id="calc-rent" value="3500" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface); font-size: 1.1rem; font-weight: 700;">
          </div>
          <div class="mb-6">
            <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Service Plan</label>
            <select id="calc-plan" style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface); font-size: 0.95rem;">
              <option value="tenant">Tenant Move-In Protection ($0 Fee - Free for Renters)</option>
              <option value="owner-placement">Owner: Tenant Placement Only (50% of first month rent)</option>
              <option value="owner-full" selected>Owner: Full Asset Management (6% of monthly rent)</option>
            </select>
          </div>
          <div class="flex-between items-center pt-4" style="border-top: 1px solid var(--border-color);">
            <div>
              <div style="font-size: 0.85rem; color: var(--text-muted);">Estimated Management Cost</div>
              <div id="calc-result" style="font-size: 1.8rem; font-weight: 800; color: var(--primary); font-family: var(--font-heading);">$210 / mo</div>
            </div>
            <a href="submit-listing.html" class="btn btn-primary">Get Started</a>
          </div>
        </div>
      </div>
    </section>

    <!-- FREQUENTLY ASKED QUESTIONS ACCORDION -->
    <section class="section section-bg-muted">
      <div class="container" style="max-width: 800px;">
        <div class="section-header">
          <div class="section-subtitle">Common Questions</div>
          <h2 class="section-title">Rental Services FAQ</h2>
        </div>

        <div class="flex flex-col gap-3">
          <div class="accordion-item" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 10px; overflow: hidden;">
            <button class="accordion-header flex-between items-center" style="width: 100%; padding: 18px 24px; text-align: left; font-weight: 700; font-size: 1rem; color: var(--text-main);">
              <span>How does the regulated escrow deposit protection work?</span>
              <span style="font-size: 1.2rem;">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 24px 20px 24px; color: var(--text-secondary); font-size: 0.95rem;">
              Your security deposit is deposited directly into a government-regulated, third-party trust account rather than the landlord's personal bank account. Deductions upon move-out must be verified with dated photographic evidence and approved by an independent Resida dispute arbiter.
            </div>
          </div>

          <div class="accordion-item" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 10px; overflow: hidden;">
            <button class="accordion-header flex-between items-center" style="width: 100%; padding: 18px 24px; text-align: left; font-weight: 700; font-size: 1rem; color: var(--text-main);">
              <span>Can I complete the entire lease signing process online?</span>
              <span style="font-size: 1.2rem;">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 24px 20px 24px; color: var(--text-secondary); font-size: 0.95rem;">
              Yes. You can take a 3D virtual tour, submit income verification, review standard tenancy agreements, sign digitally with biometric authentication, and receive your encrypted smart key access codes without printing a single sheet of paper.
            </div>
          </div>

          <div class="accordion-item" style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 10px; overflow: hidden;">
            <button class="accordion-header flex-between items-center" style="width: 100%; padding: 18px 24px; text-align: left; font-weight: 700; font-size: 1rem; color: var(--text-main);">
              <span>What happens if an appliance breaks after I move in?</span>
              <span style="font-size: 1.2rem;">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 24px 20px 24px; color: var(--text-secondary); font-size: 0.95rem;">
              Simply snap a photo and submit a ticket via your resident portal. A verified technician is scheduled within your preferred time window. For emergency heating, plumbing, or electrical failures, dispatch occurs within 60 minutes guaranteed.
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>"""
    return header + body + footer

def build_service_details():
    header = get_header("150-Point Certified Inspection Guarantee", "services")
    footer = get_footer()
    body = """  <main class="section-bg-surface" style="padding: 40px 0 80px 0;">
    <div class="container">
      <!-- Breadcrumb & Header -->
      <div class="mb-8 text-center" style="max-width: 800px; margin-left: auto; margin-right: auto;">
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 6px;">
          <a href="index.html">Home</a> / <a href="services.html">Services</a> / <span style="color: var(--text-main);">150-Point Certified Inspection</span>
        </div>
        <h1 style="font-size: clamp(2rem, 3.5vw, 2.8rem); margin-bottom: 12px;">Certified 150-Point Inspection & Move-In Guarantee</h1>
        <p style="color: var(--text-secondary); font-size: 1.1rem;">
          How our rigorous engineering and environmental inspection ensures complete peace of mind before you ever unpack a box.
        </p>
      </div>

      <!-- Hero Inspection Scene -->
      <div class="mb-12">
        <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&q=80" alt="Professional engineer conducting structural property inspection" style="width: 100%; border-radius: var(--radius-xl); box-shadow: var(--shadow-xl); aspect-ratio: 21/9; object-fit: cover;" width="1200" height="514">
      </div>

      <!-- The 4 Inspection Stages -->
      <div class="section-header">
        <div class="section-subtitle">Scientific Evaluation</div>
        <h2 class="section-title">The 4 Pillars of Property Certification</h2>
        <p class="section-desc">Every residence must score 100% compliance across all 4 critical categories to receive the Resida Verified Badge.</p>
      </div>

      <div class="grid grid-2 mb-16" style="gap: 40px;">
        <!-- Pillar 1 -->
        <div class="flex gap-4">
          <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=320&q=80" alt="Structural diagnostics team" style="width: 160px; height: 160px; border-radius: var(--radius-lg); object-fit: cover; flex-shrink: 0;" width="160" height="160">
          <div>
            <h3 style="font-size: 1.25rem; margin-bottom: 8px;">1. Structural & Moisture Diagnostics</h3>
            <p style="font-size: 0.92rem; color: var(--text-secondary);">
              Infrared thermal sensors check behind drywall for hidden moisture penetration, cold air leaks, and window gasket integrity.
            </p>
          </div>
        </div>

        <!-- Pillar 2 -->
        <div class="flex gap-4">
          <img src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?auto=format&fit=crop&w=320&q=80" alt="Inspector examining electrical breaker panel" style="width: 160px; height: 160px; border-radius: var(--radius-lg); object-fit: cover; flex-shrink: 0;" width="160" height="160">
          <div>
            <h3 style="font-size: 1.25rem; margin-bottom: 8px;">2. Electrical, HVAC & Safety Audit</h3>
            <p style="font-size: 0.92rem; color: var(--text-secondary);">
              Multimeter circuit breaker testing, GFCI safety verification in wet zones, smart thermostat calibration, and carbon monoxide detector tests.
            </p>
          </div>
        </div>

        <!-- Pillar 3 -->
        <div class="flex gap-4">
          <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=320&q=80" alt="Plumbing test on modern fixtures" style="width: 160px; height: 160px; border-radius: var(--radius-lg); object-fit: cover; flex-shrink: 0;" width="160" height="160">
          <div>
            <h3 style="font-size: 1.25rem; margin-bottom: 8px;">3. Hydraulic Pressure & Water Quality</h3>
            <p style="font-size: 0.92rem; color: var(--text-secondary);">
              Water pressure measured at all faucets, water filtration tested for mineral purity, drain flow rates verified, and silent leak detection.
            </p>
          </div>
        </div>

        <!-- Pillar 4 -->
        <div class="flex gap-4">
          <img src="https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=320&q=80" alt="Certified Move-In Guarantee report on clipboard" style="width: 160px; height: 160px; border-radius: var(--radius-lg); object-fit: cover; flex-shrink: 0;" width="160" height="160">
          <div>
            <h3 style="font-size: 1.25rem; margin-bottom: 8px;">4. Certified Move-In Guarantee</h3>
            <p style="font-size: 0.92rem; color: var(--text-secondary);">
              If any inspected component fails within your first 30 days of residency, Resida covers repair costs immediately with zero deductible.
            </p>
          </div>
        </div>
      </div>

      <!-- Action Box -->
      <div style="background: var(--bg-muted); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: 48px; text-align: center;">
        <h2 style="margin-bottom: 12px;">Are You a Landlord Ready to Certify Your Property?</h2>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto 24px auto;">
          Properties with the Resida 150-Point Certified Badge rent 4x faster at a 12% rental premium. Schedule an inspection today.
        </p>
        <div class="flex flex-center gap-4">
          <a href="submit-listing.html" class="btn btn-primary btn-lg">Schedule Certified Inspection</a>
          <a href="browse.html" class="btn btn-outline btn-lg">Browse Certified Homes</a>
        </div>
      </div>
    </div>
  </main>"""
    return header + body + footer

with open("pages/services.html", "w", encoding="utf-8") as f:
    f.write(build_services())

with open("pages/service-details.html", "w", encoding="utf-8") as f:
    f.write(build_service_details())

print("pages/services.html and pages/service-details.html built successfully!")
