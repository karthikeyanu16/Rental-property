from components import get_header, get_footer

def build_details():
    header = get_header("The Grandview Skyline Penthouse", "browse")
    footer = get_footer()
    body = """  <main class="section-bg-surface" style="padding: 32px 0 80px 0;">
    <div class="container">
      <!-- Breadcrumb & Title Header -->
      <div class="flex-between items-center mb-6" style="flex-wrap: wrap; gap: 16px;">
        <div>
          <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 6px;">
            <a href="index.html">Home</a> / <a href="browse.html">Browse Rentals</a> / <span style="color: var(--text-main);">The Grandview Skyline Penthouse</span>
          </div>
          <h1 style="font-size: clamp(1.8rem, 3vw, 2.5rem); margin-bottom: 6px;">The Grandview Skyline Penthouse</h1>
          <div class="property-location" style="font-size: 0.95rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            742 Grandview Boulevard, Downtown Central, Metro Core 10001
          </div>
        </div>

        <div class="flex items-center gap-3">
          <button class="btn btn-outline btn-sm property-fav-btn" style="position: static; width: auto; height: 42px; border-radius: 8px; padding: 0 16px; gap: 6px;" aria-label="Save Property">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            Save to Favorites
          </button>
          <a href="compare.html" class="btn btn-outline btn-sm" style="height: 42px; padding: 0 16px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            Compare Property
          </a>
        </div>
      </div>

      <!-- High-Resolution Showcase Photo Gallery -->
      <div class="property-hero-gallery">
        <div class="gallery-main">
          <img src="https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=1200&q=80" alt="The Grandview Penthouse architectural exterior" width="1200" height="440">
          <span class="badge badge-featured" style="position: absolute; top: 16px; left: 16px; z-index: 2;">Architectural Showcase</span>
        </div>
        <div class="gallery-sub">
          <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=600&q=80" alt="Sunlit open-concept designer living room" width="600" height="220">
        </div>
        <div class="gallery-sub">
          <img src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=600&q=80" alt="Gourmet chef kitchen with marble island" width="600" height="220">
          <div class="gallery-more-overlay" onclick="openModal('gallery-modal')">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
            View All 24 Photos
          </div>
        </div>
      </div>

      <!-- Specs Badges -->
      <div class="specs-badge-list">
        <div class="spec-badge-box"><strong>3</strong> Bedrooms</div>
        <div class="spec-badge-box"><strong>3.0</strong> Bathrooms</div>
        <div class="spec-badge-box"><strong>2,450</strong> Sq Ft</div>
        <div class="spec-badge-box"><strong>24th</strong> Floor Penthouse</div>
        <div class="spec-badge-box"><strong>Furnished</strong> Designer Interior</div>
        <div class="spec-badge-box"><strong>Immediate</strong> Move-In Ready</div>
        <div class="badge badge-verified badge-pill" style="align-self: center; font-size: 0.85rem; padding: 6px 16px;">
          ✓ Certified 150-Point Inspected
        </div>
      </div>

      <!-- Main Content & Sticky Tour Booking -->
      <div class="property-detail-grid">
        <div>
          <!-- Description -->
          <section class="mb-8">
            <h3 class="mb-4">About This Residence</h3>
            <p>
              Perched atop the prestigious 24th floor of The Grandview Tower, this extraordinary 2,450-square-foot corner penthouse combines dramatic metropolitan views with refined minimalist luxury. Designed by award-winning architects, the residence features 11-foot acoustic ceilings, wide-plank white oak flooring, and floor-to-ceiling curtain wall glass framing panoramic city skylines.
            </p>
            <p>
              The bespoke custom kitchen features honed Calacatta quartz countertops, Miele integrated induction cooktops, dual wine refrigeration, and a waterfall breakfast island. The master suite is a private sanctuary offering custom walk-in dressing rooms, motorized blackout drapery, and a spa-grade bathroom with a freestanding stone soaking tub and Hansgrohe rain shower.
            </p>
          </section>

          <!-- Verified Rental Terms Table -->
          <section class="mb-8">
            <h3 class="mb-4">Verified Rental Terms & Policies</h3>
            <div style="background: var(--bg-muted); border-radius: var(--radius-lg); padding: 24px; border: 1px solid var(--border-color);">
              <div class="grid grid-2" style="gap: 16px; font-size: 0.95rem;">
                <div><strong>Monthly Rent:</strong> $4,850 / month</div>
                <div><strong>Security Deposit:</strong> $4,850 (Escrow Protected)</div>
                <div><strong>Lease Term:</strong> 12 - 24 Months Flexible</div>
                <div><strong>Utilities Included:</strong> Fiber Internet, Water, Trash</div>
                <div><strong>Pet Policy:</strong> Cats & Dogs Welcome (Up to 2 pets)</div>
                <div><strong>Parking:</strong> 2 Dedicated Underground EV Stalls</div>
              </div>
            </div>
          </section>

          <!-- Comprehensive Amenities Checklist -->
          <section class="mb-8">
            <h3 class="mb-4">Features & Building Amenities</h3>
            <div class="amenities-grid">
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Heated Infinity Pool</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> 24/7 Concierge & Valet</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Wellness Gym & Pilates</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Private Wrap Balcony</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> In-Unit Miele Washer/Dryer</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Keyless Smartphone Entry</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Dedicated EV Charging</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Pet Washing Station</div>
              <div class="amenity-chip"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Central Multi-Zone HVAC</div>
            </div>
          </section>

          <!-- Location & Transit Proximity -->
          <section class="mb-8">
            <h3 class="mb-4">Neighborhood & Transit Accessibility</h3>
            <div class="grid grid-3 text-center mb-6">
              <div class="stat-card flex-col" style="text-align: center;">
                <div class="stat-val" style="color: var(--primary);">98/100</div>
                <div class="stat-lbl">WalkScore: Walker's Paradise</div>
              </div>
              <div class="stat-card flex-col" style="text-align: center;">
                <div class="stat-val" style="color: var(--primary);">95/100</div>
                <div class="stat-lbl">TransitScore: Rider's Dream</div>
              </div>
              <div class="stat-card flex-col" style="text-align: center;">
                <div class="stat-val" style="color: var(--accent);">91/100</div>
                <div class="stat-lbl">SoundScore: Acoustic Quiet</div>
              </div>
            </div>

            <div class="grid grid-2" style="font-size: 0.9rem; gap: 12px;">
              <div>🚇 <strong>Metro Red & Blue Line Station:</strong> 2 mins walk (180m)</div>
              <div>🥑 <strong>Whole Foods Organic Market:</strong> 4 mins walk (350m)</div>
              <div>🏥 <strong>Metropolitan University Hospital:</strong> 8 mins drive (2.4km)</div>
              <div>🌳 <strong>Highland Botanical Green Park:</strong> 5 mins walk (400m)</div>
            </div>
          </section>
        </div>

        <!-- Sticky Booking Card -->
        <aside>
          <div class="sticky-booking-card">
            <div class="flex-between items-center mb-4">
              <div>
                <span style="font-size: 1.8rem; font-weight: 800; font-family: var(--font-heading); color: var(--text-main);">$4,850</span>
                <span style="color: var(--text-muted); font-size: 0.9rem;">/ month</span>
              </div>
              <span class="badge badge-verified">Available Now</span>
            </div>

            <form action="#" method="POST" id="tour-booking-form">
              <div class="mb-4">
                <label style="font-size: 0.85rem; font-weight: 600; display: block; margin-bottom: 6px;">Select Tour Type</label>
                <div class="flex gap-2">
                  <label class="btn btn-outline btn-sm" style="flex: 1; cursor: pointer;">
                    <input type="radio" name="tour_type" value="in-person" checked> In-Person VIP
                  </label>
                  <label class="btn btn-outline btn-sm" style="flex: 1; cursor: pointer;">
                    <input type="radio" name="tour_type" value="virtual"> 3D Virtual Tour
                  </label>
                </div>
              </div>

              <div class="mb-4">
                <label for="tour-date" style="font-size: 0.85rem; font-weight: 600; display: block; margin-bottom: 6px;">Preferred Date</label>
                <input type="date" id="tour-date" required style="width: 100%; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface);">
              </div>

              <div class="mb-4">
                <label for="tour-time" style="font-size: 0.85rem; font-weight: 600; display: block; margin-bottom: 6px;">Preferred Time Slot</label>
                <select id="tour-time" required style="width: 100%; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface);">
                  <option value="10:00">10:00 AM - Morning VIP</option>
                  <option value="12:30">12:30 PM - Midday Tour</option>
                  <option value="15:00" selected>03:00 PM - Afternoon Light</option>
                  <option value="17:30">05:30 PM - Twilight Sunset</option>
                </select>
              </div>

              <div class="mb-4">
                <label for="tour-phone" style="font-size: 0.85rem; font-weight: 600; display: block; margin-bottom: 6px;">Your Phone Number</label>
                <input type="tel" id="tour-phone" placeholder="+1 (555) 000-0000" required style="width: 100%; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface);">
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%; margin-bottom: 12px;">Request Tour Appointment</button>
            </form>

            <!-- Monthly Cost Calculator -->
            <div style="border-top: 1px solid var(--border-color); padding-top: 16px; margin-top: 16px;">
              <div style="font-weight: 700; font-size: 0.95rem; margin-bottom: 8px;">Estimated Monthly Cost</div>
              <table class="cost-breakdown-table">
                <tr><td>Base Monthly Rent</td><td>$4,850</td></tr>
                <tr><td>Building Maintenance & HOA</td><td>$0 (Included)</td></tr>
                <tr><td>Gigabit Fiber Internet</td><td>$0 (Included)</td></tr>
                <tr><td>Underground Parking (2 stalls)</td><td>$250</td></tr>
                <tr class="total"><td>Total Monthly Estimate</td><td>$5,100 / mo</td></tr>
              </table>
            </div>

            <!-- Agent Contact Strip -->
            <div class="flex items-center gap-3 pt-4" style="border-top: 1px solid var(--border-color); margin-top: 16px;">
              <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=80" alt="Marcus Vance" class="agent-avatar" width="44" height="44">
              <div>
                <div style="font-weight: 700; font-size: 0.9rem;">Marcus Vance</div>
                <div style="font-size: 0.8rem; color: var(--text-muted);">Licensed Senior Leasing Broker #48912</div>
              </div>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </main>

  <!-- Photo Gallery Modal -->
  <div id="gallery-modal" class="modal-overlay">
    <div class="modal-dialog" style="max-width: 900px;">
      <div class="flex-between items-center mb-4">
        <h3 style="margin: 0;">The Grandview Penthouse Gallery</h3>
        <button data-modal-close class="btn-icon" aria-label="Close Gallery">✕</button>
      </div>
      <div class="grid grid-2" style="gap: 16px;">
        <img src="https://images.unsplash.com/photo-1560185007-cde436f6a4d0?auto=format&fit=crop&w=600&q=80" alt="Master suite king bedroom" style="border-radius: 8px; width: 100%;">
        <img src="https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=600&q=80" alt="Spa ensuite bathroom" style="border-radius: 8px; width: 100%;">
        <img src="https://images.unsplash.com/photo-1512915922686-57c11dde9b6b?auto=format&fit=crop&w=600&q=80" alt="Private wrap terrace" style="border-radius: 8px; width: 100%;">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" alt="Building amenities pool" style="border-radius: 8px; width: 100%;">
      </div>
    </div>
  </div>"""
    return header + body + footer

with open("pages/property-details.html", "w", encoding="utf-8") as f:
    f.write(build_details())

print("pages/property-details.html built successfully!")
