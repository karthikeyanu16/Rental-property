from components import get_header, get_footer

def build_browse():
    header = get_header("Browse Residential Rentals", "browse")
    footer = get_footer()
    map_script = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // View Switcher logic
      const btnGrid = document.getElementById('view-grid-btn');
      const btnList = document.getElementById('view-list-btn');
      const btnMap = document.getElementById('view-map-btn');
      const gridContainer = document.getElementById('browse-grid-container');
      const mapContainer = document.getElementById('browse-map-container');

      btnGrid?.addEventListener('click', () => {
        btnGrid.classList.add('active');
        btnList?.classList.remove('active');
        btnMap?.classList.remove('active');
        if (gridContainer) { gridContainer.style.display = 'grid'; gridContainer.className = 'grid grid-3'; }
        if (mapContainer) mapContainer.style.display = 'none';
      });

      btnList?.addEventListener('click', () => {
        btnList.classList.add('active');
        btnGrid?.classList.remove('active');
        btnMap?.classList.remove('active');
        if (gridContainer) { gridContainer.style.display = 'grid'; gridContainer.className = 'grid grid-2'; }
        if (mapContainer) mapContainer.style.display = 'none';
      });

      btnMap?.addEventListener('click', () => {
        btnMap.classList.add('active');
        btnGrid?.classList.remove('active');
        btnList?.classList.remove('active');
        if (gridContainer) gridContainer.style.display = 'none';
        if (mapContainer) {
          mapContainer.style.display = 'grid';
          window.dispatchEvent(new Event('resize'));
        }
      });

      // Price slider updates
      const slider = document.getElementById('filter-price-slider');
      const priceDisplay = document.getElementById('filter-price-val');
      slider?.addEventListener('input', e => {
        if (priceDisplay) priceDisplay.textContent = '$' + parseInt(e.target.value, 10).toLocaleString();
      });
    });
  </script>
</body>
</html>"""
    footer = footer.replace('</body>\n</html>', map_script)

    body = """  <main class="section-bg-muted" style="padding: 40px 0 80px 0;">
    <div class="container">
      <!-- Breadcrumb & Page Title -->
      <div class="mb-6">
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 6px;">
          <a href="index.html">Home</a> / <span style="color: var(--text-main);">Browse Rentals</span>
        </div>
        <h1 style="font-size: 2rem;">Discover Residential Rentals</h1>
        <p style="color: var(--text-secondary); margin-bottom: 0;">Showing 1,480 verified apartments, villas, and urban lofts available for immediate lease.</p>
      </div>

      <div class="browse-layout">
        <!-- Filter Sidebar -->
        <aside class="filter-sidebar">
          <div class="flex-between items-center mb-4">
            <h3 style="font-size: 1.15rem; margin: 0;">Filters</h3>
            <button type="reset" style="font-size: 0.85rem; color: var(--primary); font-weight: 600;" onclick="showToast('Filters reset')">Reset All</button>
          </div>

          <div class="filter-group">
            <div class="filter-title">Location</div>
            <input type="text" placeholder="City, neighborhood, or zip" value="Downtown Central" style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: 6px; background: var(--bg-surface); font-size: 0.9rem;">
          </div>

          <div class="filter-group">
            <div class="filter-title">Monthly Budget</div>
            <div class="range-wrap">
              <input type="range" id="filter-price-slider" class="range-slider" min="1000" max="12000" step="250" value="4850">
              <div class="range-values">
                <span>$1,000</span>
                <span id="filter-price-val" style="color: var(--primary);">$4,850</span>
                <span>$12,000+</span>
              </div>
            </div>
          </div>

          <div class="filter-group">
            <div class="filter-title">Property Type</div>
            <label class="checkbox-label"><input type="checkbox" checked> Apartment (842)</label>
            <label class="checkbox-label"><input type="checkbox" checked> Luxury Villa (194)</label>
            <label class="checkbox-label"><input type="checkbox"> Urban Loft (156)</label>
            <label class="checkbox-label"><input type="checkbox"> Studio Sanctuary (210)</label>
            <label class="checkbox-label"><input type="checkbox"> Garden Duplex (78)</label>
          </div>

          <div class="filter-group">
            <div class="filter-title">Bedrooms</div>
            <div class="flex gap-2" style="flex-wrap: wrap;">
              <button class="btn btn-sm btn-outline active" style="padding: 6px 12px;">Any</button>
              <button class="btn btn-sm btn-outline" style="padding: 6px 12px;">Studio</button>
              <button class="btn btn-sm btn-outline" style="padding: 6px 12px;">1</button>
              <button class="btn btn-sm btn-outline" style="padding: 6px 12px;">2</button>
              <button class="btn btn-sm btn-outline" style="padding: 6px 12px;">3+</button>
            </div>
          </div>

          <div class="filter-group">
            <div class="filter-title">Furnishing Status</div>
            <label class="checkbox-label"><input type="checkbox" checked> Fully Furnished</label>
            <label class="checkbox-label"><input type="checkbox"> Semi-Furnished</label>
            <label class="checkbox-label"><input type="checkbox"> Unfurnished</label>
          </div>

          <div class="filter-group">
            <div class="filter-title">Amenities & Features</div>
            <label class="checkbox-label"><input type="checkbox" checked> Swimming Pool</label>
            <label class="checkbox-label"><input type="checkbox" checked> Wellness Gym / Spa</label>
            <label class="checkbox-label"><input type="checkbox" checked> Pet-Friendly</label>
            <label class="checkbox-label"><input type="checkbox"> EV Charger Stall</label>
            <label class="checkbox-label"><input type="checkbox"> Balcony / Skyline Deck</label>
            <label class="checkbox-label"><input type="checkbox"> 24/7 Concierge / Doorman</label>
          </div>

          <button class="btn btn-primary" style="width: 100%;" onclick="showToast('Applied 6 filters: 18 matching properties')">Apply Filters</button>
        </aside>

        <!-- Listings Content Area -->
        <div>
          <!-- Control Bar -->
          <div class="browse-controls">
            <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-secondary);">
              Showing <span style="color: var(--text-main); font-weight: 700;">8</span> of 1,480 Rentals
            </div>

            <div class="flex items-center gap-4">
              <div class="flex items-center gap-2">
                <label for="sort-select" style="font-size: 0.85rem; color: var(--text-muted);">Sort By:</label>
                <select id="sort-select" style="padding: 6px 10px; border-radius: 6px; border: 1px solid var(--border-color); background: var(--bg-surface); font-size: 0.85rem;">
                  <option>Featured & Recommended</option>
                  <option>Price: Low to High</option>
                  <option>Price: High to Low</option>
                  <option>Newest Listed</option>
                  <option>Highest Tenant Rating</option>
                </select>
              </div>

              <!-- View Switchers -->
              <div class="view-switchers">
                <button id="view-grid-btn" class="view-btn active" title="Grid View" aria-label="Grid View">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
                </button>
                <button id="view-list-btn" class="view-btn" title="Detailed List View" aria-label="Detailed List View">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
                </button>
                <button id="view-map-btn" class="view-btn" title="Split Map View" aria-label="Split Map View">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Standard Grid of Properties -->
          <div id="browse-grid-container" class="grid grid-3">
            <!-- Property 1 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80" alt="The Grandview Skyline Penthouse" class="property-thumb" width="800" height="500">
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

            <!-- Property 2 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80" alt="Greenwich Garden Loft Residence" class="property-thumb" width="800" height="500">
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

            <!-- Property 3 -->
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

            <!-- Property 4 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=800&q=80" alt="Scandinavian Minimalist Studio" class="property-thumb" width="800" height="500">
                <div class="property-badges"><span class="badge badge-verified">Verified</span></div>
                <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
                <div class="property-price-tag">$2,100<span>/mo</span></div>
              </div>
              <div class="property-body">
                <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Midtown Innovation District</div>
                <h3 class="property-title"><a href="property-details.html">Scandinavian Minimalist Studio</a></h3>
                <div class="property-specs">
                  <div class="spec-item">1 Bed</div><div class="spec-item">1 Bath</div><div class="spec-item">750 sq ft</div>
                </div>
                <div class="property-footer">
                  <div class="property-agent"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80" alt="Chloe Bennett" class="agent-avatar" width="32" height="32"><span class="agent-name">Chloe Bennett</span></div>
                  <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-4" data-title="Scandinavian Minimalist Studio"> Compare</label>
                </div>
              </div>
            </article>

            <!-- Property 5 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=800&q=80" alt="Kensington Heritage Townhome" class="property-thumb" width="800" height="500">
                <div class="property-badges"><span class="badge badge-featured">Featured</span><span class="badge badge-verified">Verified</span></div>
                <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
                <div class="property-price-tag">$5,200<span>/mo</span></div>
              </div>
              <div class="property-body">
                <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Historic Heights District</div>
                <h3 class="property-title"><a href="property-details.html">Kensington Heritage Townhome</a></h3>
                <div class="property-specs">
                  <div class="spec-item">4 Beds</div><div class="spec-item">3.5 Baths</div><div class="spec-item">3,100 sq ft</div>
                </div>
                <div class="property-footer">
                  <div class="property-agent"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=80" alt="Marcus Vance" class="agent-avatar" width="32" height="32"><span class="agent-name">Marcus Vance</span></div>
                  <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-5" data-title="Kensington Heritage Townhome"> Compare</label>
                </div>
              </div>
            </article>

            <!-- Property 6 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80" alt="The Highline Modern Eco-Duplex" class="property-thumb" width="800" height="500">
                <div class="property-badges"><span class="badge badge-hot">Eco-Certified</span><span class="badge badge-verified">Verified</span></div>
                <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
                <div class="property-price-tag">$3,800<span>/mo</span></div>
              </div>
              <div class="property-body">
                <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Uptown Green Promenade</div>
                <h3 class="property-title"><a href="property-details.html">The Highline Modern Eco-Duplex</a></h3>
                <div class="property-specs">
                  <div class="spec-item">2 Beds</div><div class="spec-item">2.5 Baths</div><div class="spec-item">1,850 sq ft</div>
                </div>
                <div class="property-footer">
                  <div class="property-agent"><img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=100&q=80" alt="Elena Rostova" class="agent-avatar" width="32" height="32"><span class="agent-name">Elena Rostova</span></div>
                  <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-6" data-title="The Highline Modern Eco-Duplex"> Compare</label>
                </div>
              </div>
            </article>

            <!-- Property 7 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80" alt="Cedar Point Mid-Century Residence" class="property-thumb" width="800" height="500">
                <div class="property-badges"><span class="badge badge-verified">Verified</span></div>
                <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
                <div class="property-price-tag">$4,100<span>/mo</span></div>
              </div>
              <div class="property-body">
                <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Pinecrest Foothills</div>
                <h3 class="property-title"><a href="property-details.html">Cedar Point Mid-Century Villa</a></h3>
                <div class="property-specs">
                  <div class="spec-item">3 Beds</div><div class="spec-item">2 Baths</div><div class="spec-item">2,150 sq ft</div>
                </div>
                <div class="property-footer">
                  <div class="property-agent"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&q=80" alt="Julian Thorne" class="agent-avatar" width="32" height="32"><span class="agent-name">Julian Thorne</span></div>
                  <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-7" data-title="Cedar Point Mid-Century Villa"> Compare</label>
                </div>
              </div>
            </article>

            <!-- Property 8 -->
            <article class="property-card">
              <div class="property-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80" alt="Lakeside Glass Pavilion" class="property-thumb" width="800" height="500">
                <div class="property-badges"><span class="badge badge-featured">Featured</span><span class="badge badge-verified">Verified</span></div>
                <button class="property-fav-btn" title="Save property" aria-label="Save Property"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></button>
                <div class="property-price-tag">$5,900<span>/mo</span></div>
              </div>
              <div class="property-body">
                <div class="property-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Crystal Lake Vista</div>
                <h3 class="property-title"><a href="property-details.html">Lakeside Contemporary Pavilion</a></h3>
                <div class="property-specs">
                  <div class="spec-item">4 Beds</div><div class="spec-item">4 Baths</div><div class="spec-item">3,400 sq ft</div>
                </div>
                <div class="property-footer">
                  <div class="property-agent"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=80" alt="Chloe Bennett" class="agent-avatar" width="32" height="32"><span class="agent-name">Chloe Bennett</span></div>
                  <label class="property-compare-check"><input type="checkbox" class="compare-checkbox" data-id="prop-8" data-title="Lakeside Contemporary Pavilion"> Compare</label>
                </div>
              </div>
            </article>
          </div>

          <!-- Split Map Container (Hidden by default, shown when Map view is clicked) -->
          <div id="browse-map-container" class="map-split-container" style="display: none;">
            <div class="map-listings-pane">
              <div class="grid grid-2">
                <article class="property-card">
                  <div class="property-thumb-wrap">
                    <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" alt="Penthouse" class="property-thumb">
                    <div class="property-price-tag">$4,850/mo</div>
                  </div>
                  <div class="property-body">
                    <h4 style="font-size: 1rem;"><a href="property-details.html">The Grandview Penthouse</a></h4>
                    <p style="font-size: 0.82rem; margin: 0;">3 Beds • 3 Baths • 2,450 sq ft</p>
                  </div>
                </article>
                <article class="property-card">
                  <div class="property-thumb-wrap">
                    <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=600&q=80" alt="Loft" class="property-thumb">
                    <div class="property-price-tag">$3,200/mo</div>
                  </div>
                  <div class="property-body">
                    <h4 style="font-size: 1rem;"><a href="property-details.html">Greenwich Garden Loft</a></h4>
                    <p style="font-size: 0.82rem; margin: 0;">2 Beds • 2 Baths • 1,620 sq ft</p>
                  </div>
                </article>
                <article class="property-card">
                  <div class="property-thumb-wrap">
                    <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=600&q=80" alt="Villa" class="property-thumb">
                    <div class="property-price-tag">$6,500/mo</div>
                  </div>
                  <div class="property-body">
                    <h4 style="font-size: 1rem;"><a href="property-details.html">Azure Waterfront Villa</a></h4>
                    <p style="font-size: 0.82rem; margin: 0;">4 Beds • 4 Baths • 3,800 sq ft</p>
                  </div>
                </article>
                <article class="property-card">
                  <div class="property-thumb-wrap">
                    <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=600&q=80" alt="Studio" class="property-thumb">
                    <div class="property-price-tag">$2,100/mo</div>
                  </div>
                  <div class="property-body">
                    <h4 style="font-size: 1rem;"><a href="property-details.html">Minimalist Studio</a></h4>
                    <p style="font-size: 0.82rem; margin: 0;">1 Bed • 1 Bath • 750 sq ft</p>
                  </div>
                </article>
              </div>
            </div>
            <div class="map-view-pane" style="height: 100%; min-height: 540px; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color);">
              <iframe title="Manhattan Rental Properties Interactive Map" src="https://maps.google.com/maps?q=Manhattan,%20New%20York,%20NY&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0; width: 100%; height: 100%; min-height: 540px;" allowfullscreen="" loading="lazy"></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>"""
    return header + body + footer

with open("pages/browse.html", "w", encoding="utf-8") as f:
    f.write(build_browse())

print("pages/browse.html built successfully!")
