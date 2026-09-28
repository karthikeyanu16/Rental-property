from components import get_header, get_footer

def build_submit_listing():
    header = get_header("List Your Property", "submit")
    footer = get_footer()
    # Add wizard step switcher script
    wizard_script = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      let currentStep = 1;
      const totalSteps = 4;

      function updateWizard(step) {
        document.querySelectorAll('.wizard-panel').forEach(p => p.style.display = 'none');
        const activePanel = document.getElementById(`step-panel-${step}`);
        if (activePanel) activePanel.style.display = 'block';

        document.querySelectorAll('.wizard-step-node').forEach((node, idx) => {
          if (idx + 1 === step) {
            node.className = 'wizard-step-node active';
          } else if (idx + 1 < step) {
            node.className = 'wizard-step-node completed';
          } else {
            node.className = 'wizard-step-node';
          }
        });
      }

      window.nextStep = function() {
        if (currentStep < totalSteps) {
          currentStep++;
          updateWizard(currentStep);
          window.scrollTo({ top: 120, behavior: 'smooth' });
        }
      };

      window.prevStep = function() {
        if (currentStep > 1) {
          currentStep--;
          updateWizard(currentStep);
          window.scrollTo({ top: 120, behavior: 'smooth' });
        }
      };

      document.getElementById('listing-wizard-form')?.addEventListener('submit', (e) => {
        e.preventDefault();
        openModal('submission-modal');
      });
    });
  </script>
</body>
</html>"""
    footer = footer.replace('</body>\n</html>', wizard_script)

    body = """  <main class="section-bg-muted" style="padding: 40px 0 80px 0;">
    <div class="container" style="max-width: 900px;">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="section-subtitle">Owner & Agent Portal</div>
        <h1 style="font-size: 2.2rem; margin-bottom: 8px;">List Your Rental Property on Resida</h1>
        <p style="color: var(--text-secondary); margin: 0 auto; max-width: 600px;">
          Reach verified, high-credit tenants. Fast-track your listing to certified status with our 150-Point Inspection team.
        </p>
      </div>

      <!-- Header Visual Banner -->
      <div class="mb-8">
        <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=80" alt="Architectural blueprint and property planning desk" style="width: 100%; border-radius: var(--radius-lg); height: 180px; object-fit: cover;" width="1200" height="180">
      </div>

      <!-- Multi-Step Wizard Progress -->
      <div class="wizard-progress">
        <div class="wizard-step-node active">
          <div class="node-circle">1</div>
          <div class="node-label">Basic Info</div>
        </div>
        <div class="wizard-step-node">
          <div class="node-circle">2</div>
          <div class="node-label">Specs & Rent</div>
        </div>
        <div class="wizard-step-node">
          <div class="node-circle">3</div>
          <div class="node-label">Amenities</div>
        </div>
        <div class="wizard-step-node">
          <div class="node-circle">4</div>
          <div class="node-label">Media & Verify</div>
        </div>
      </div>

      <form id="listing-wizard-form" class="wizard-card">
        <!-- Step 1: Basic Info -->
        <div id="step-panel-1" class="wizard-panel">
          <h3 class="mb-4">Step 1: Property Identification & Location</h3>
          <div class="mb-4">
            <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Listing Title</label>
            <input type="text" placeholder="e.g. The Grandview Modern Skyline Penthouse" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
          </div>
          <div class="grid grid-2 mb-4">
            <div>
              <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Property Category</label>
              <select style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
                <option>Apartment / Flat</option>
                <option>Luxury Penthouse</option>
                <option>Urban Industrial Loft</option>
                <option>Detached Villa</option>
                <option>Townhouse / Duplex</option>
              </select>
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Available Move-In Date</label>
              <input type="date" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
          </div>
          <div class="mb-6">
            <label style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Street Address & City</label>
            <input type="text" placeholder="742 Grandview Blvd, Downtown, NY 10001" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
          </div>
          <div class="flex justify-between">
            <div></div>
            <button type="button" class="btn btn-primary" onclick="nextStep()">Continue to Step 2 →</button>
          </div>
        </div>

        <!-- Step 2: Specs & Pricing -->
        <div id="step-panel-2" class="wizard-panel" style="display: none;">
          <h3 class="mb-4">Step 2: Property Specifications & Rental Pricing</h3>
          <div class="grid grid-3 mb-4">
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Monthly Rent ($ USD)</label>
              <input type="number" placeholder="4500" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Security Deposit ($ USD)</label>
              <input type="number" placeholder="4500" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Total Square Footage</label>
              <input type="number" placeholder="2200" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
          </div>
          <div class="grid grid-3 mb-6">
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Bedrooms</label>
              <select style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
                <option>Studio</option>
                <option>1 Bedroom</option>
                <option>2 Bedrooms</option>
                <option selected>3 Bedrooms</option>
                <option>4+ Bedrooms</option>
              </select>
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Bathrooms</label>
              <select style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
                <option>1.0 Bath</option>
                <option>1.5 Baths</option>
                <option>2.0 Baths</option>
                <option selected>3.0 Baths</option>
              </select>
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Furnishing Status</label>
              <select style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
                <option>Fully Furnished</option>
                <option>Semi-Furnished</option>
                <option>Unfurnished</option>
              </select>
            </div>
          </div>
          <div class="flex justify-between">
            <button type="button" class="btn btn-outline" onclick="prevStep()">← Back</button>
            <button type="button" class="btn btn-primary" onclick="nextStep()">Continue to Step 3 →</button>
          </div>
        </div>

        <!-- Step 3: Amenities -->
        <div id="step-panel-3" class="wizard-panel" style="display: none;">
          <h3 class="mb-4">Step 3: Features & Building Amenities</h3>
          <p style="color: var(--text-secondary); margin-bottom: 20px;">Select all features that apply to your rental property:</p>
          <div class="grid grid-3 mb-6" style="gap: 12px;">
            <label class="checkbox-label"><input type="checkbox" checked> Swimming Pool</label>
            <label class="checkbox-label"><input type="checkbox" checked> Fitness Center / Gym</label>
            <label class="checkbox-label"><input type="checkbox" checked> Private Balcony / Terrace</label>
            <label class="checkbox-label"><input type="checkbox" checked> In-Unit Washer & Dryer</label>
            <label class="checkbox-label"><input type="checkbox" checked> Central Air Conditioning</label>
            <label class="checkbox-label"><input type="checkbox" checked> EV Charging Stations</label>
            <label class="checkbox-label"><input type="checkbox" checked> Pet-Friendly</label>
            <label class="checkbox-label"><input type="checkbox"> Concierge / Doorman</label>
            <label class="checkbox-label"><input type="checkbox"> High-Speed Fiber Internet</label>
          </div>
          <div class="flex justify-between">
            <button type="button" class="btn btn-outline" onclick="prevStep()">← Back</button>
            <button type="button" class="btn btn-primary" onclick="nextStep()">Continue to Final Step →</button>
          </div>
        </div>

        <!-- Step 4: Media Upload & Submit -->
        <div id="step-panel-4" class="wizard-panel" style="display: none;">
          <h3 class="mb-4">Step 4: Photography & Owner Verification</h3>
          <div class="upload-dropzone mb-6">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--primary); margin: 0 auto 12px auto;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <div style="font-weight: 700; margin-bottom: 4px;">Drag and drop high-resolution photographs here</div>
            <div style="font-size: 0.85rem; color: var(--text-muted);">Supports JPG, PNG, WEBP (Min. 1920x1080 resolution, up to 25MB each)</div>
            <button type="button" class="btn btn-outline btn-sm mt-4">Browse Files</button>
          </div>

          <div class="grid grid-2 mb-6">
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Owner / Agent Full Name</label>
              <input type="text" placeholder="David Sterling" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
            <div>
              <label style="font-size: 0.85rem; font-weight: 700;">Direct Contact Telephone</label>
              <input type="tel" placeholder="+1 (555) 234-5678" required style="width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-surface); margin-top: 4px;">
            </div>
          </div>

          <div class="flex justify-between">
            <button type="button" class="btn btn-outline" onclick="prevStep()">← Back</button>
            <button type="submit" class="btn btn-primary btn-lg">Publish Listing & Book Inspection</button>
          </div>
        </div>
      </form>
    </div>
  </main>

  <!-- Submission Success Modal -->
  <div id="submission-modal" class="modal-overlay">
    <div class="modal-dialog text-center">
      <div style="width: 60px; height: 60px; background: var(--accent-light); color: var(--accent); border-radius: 9999px; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px auto; font-size: 1.8rem;">
        ✓
      </div>
      <h3 style="margin-bottom: 8px;">Listing Submitted Successfully!</h3>
      <p style="color: var(--text-secondary); margin-bottom: 24px;">
        Your listing has been submitted for review. Our physical inspection team will reach out within 4 business hours to schedule the 150-Point Certification walk-through.
      </p>
      <div class="flex flex-center gap-3">
        <a href="dashboard.html" class="btn btn-primary">Go to Owner Dashboard</a>
        <button data-modal-close class="btn btn-outline">Close</button>
      </div>
    </div>
  </div>"""
    return header + body + footer

def build_dashboard():
    header = get_header("Management Dashboard", "dashboard")
    footer = get_footer()
    # Add dashboard.js script
    footer = footer.replace('<script src="../assets/js/main.js"></script>', '<script src="../assets/js/main.js"></script>\n  <script src="../assets/js/dashboard.js"></script>')

    body = """  <main class="dashboard-layout">
    <!-- Sidebar -->
    <aside class="dashboard-sidebar">
      <div class="mb-6">
        <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); margin-bottom: 12px; font-weight: 700;">Account Portal</div>
        <div class="flex gap-2 mb-4" style="background: var(--bg-muted); padding: 4px; border-radius: 8px;">
          <button id="role-landlord-btn" class="btn btn-sm btn-primary active" style="flex: 1; padding: 6px 8px; font-size: 0.8rem;">Owner View</button>
          <button id="role-tenant-btn" class="btn btn-sm btn-outline" style="flex: 1; padding: 6px 8px; font-size: 0.8rem; border: none;">Tenant View</button>
        </div>
      </div>

      <nav>
        <a href="#" class="dashboard-nav-item active">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          Overview & Stats
        </a>
        <a href="#" class="dashboard-nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          Managed Properties (14)
        </a>
        <a href="#" class="dashboard-nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          Viewing Inquiries (28)
        </a>
        <a href="#" class="dashboard-nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          Financial Disbursals
        </a>
        <a href="#" class="dashboard-nav-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          Account Settings
        </a>
      </nav>

      <div style="margin-top: 40px; padding: 16px; background: var(--bg-muted); border-radius: 8px; font-size: 0.85rem;">
        <strong>Need Assistance?</strong>
        <p style="margin: 4px 0 12px 0; color: var(--text-muted);">24/7 dedicated property concierge is standing by.</p>
        <a href="contact.html" class="btn btn-outline btn-sm" style="width: 100%;">Contact Support</a>
      </div>
    </aside>

    <!-- Main Content Area -->
    <div class="dashboard-content">
      <!-- LANDLORD VIEW -->
      <div id="landlord-view-container">
        <!-- Stats Row -->
        <div class="stats-card-grid">
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></div>
            <div><div class="stat-val">14</div><div class="stat-lbl">Active Properties</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
            <div><div class="stat-val">$42,800</div><div class="stat-lbl">Monthly Gross Rent</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
            <div><div class="stat-val">94.2%</div><div class="stat-lbl">Portfolio Occupancy</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></div>
            <div><div class="stat-val">28</div><div class="stat-lbl">Active Inquiries</div></div>
          </div>
        </div>

        <!-- Monthly Revenue Chart -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 32px;">
          <div class="flex-between items-center mb-4">
            <div>
              <h3 style="font-size: 1.15rem; margin-bottom: 2px;">Rental Revenue & Inquiries Trend</h3>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">12-month performance telemetry</p>
            </div>
            <span class="badge badge-verified">+18.4% Year-over-Year</span>
          </div>
          <div style="width: 100%; height: 280px;">
            <canvas id="revenue-chart-canvas"></canvas>
          </div>
        </div>

        <!-- Managed Listings Table -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 32px;">
          <div class="flex-between items-center mb-4" style="flex-wrap: wrap; gap: 12px;">
            <h3 style="font-size: 1.15rem; margin: 0;">Managed Rental Portfolio</h3>
            <div class="flex gap-2">
              <button class="btn btn-sm btn-primary active table-filter-tab" data-filter="all">All (14)</button>
              <button class="btn btn-sm btn-outline table-filter-tab" data-filter="active">Active (12)</button>
              <button class="btn btn-sm btn-outline table-filter-tab" data-filter="pending">Pending (2)</button>
            </div>
          </div>

          <div style="overflow-x: auto;">
            <table class="dashboard-table">
              <thead>
                <tr>
                  <th>Property</th>
                  <th>Monthly Rent</th>
                  <th>Tenant</th>
                  <th>Lease Expiry</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr class="listing-row" data-status="active">
                  <td>
                    <strong>The Grandview Skyline Penthouse</strong><br>
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Downtown Central</span>
                  </td>
                  <td>$4,850/mo</td>
                  <td>Sarah Jenkins</td>
                  <td>Oct 2027</td>
                  <td><span class="badge badge-verified">Active Lease</span></td>
                  <td><a href="property-details.html" class="btn btn-outline btn-sm">Inspect</a></td>
                </tr>
                <tr class="listing-row" data-status="active">
                  <td>
                    <strong>Greenwich Garden Loft</strong><br>
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Arts District</span>
                  </td>
                  <td>$3,200/mo</td>
                  <td>Liam O'Connor</td>
                  <td>Jan 2027</td>
                  <td><span class="badge badge-verified">Active Lease</span></td>
                  <td><a href="property-details.html" class="btn btn-outline btn-sm">Inspect</a></td>
                </tr>
                <tr class="listing-row" data-status="pending">
                  <td>
                    <strong>The Azure Waterfront Villa</strong><br>
                    <span style="font-size: 0.8rem; color: var(--text-muted);">Coastal Marina</span>
                  </td>
                  <td>$6,500/mo</td>
                  <td>Pending Placement</td>
                  <td>Vacant</td>
                  <td><span class="badge badge-hot">Under Review</span></td>
                  <td><a href="property-details.html" class="btn btn-outline btn-sm">Review</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Recent Viewing Requests Queue -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px;">
          <h3 style="font-size: 1.15rem; margin-bottom: 16px;">Pending Viewing Appointments</h3>
          <div class="flex flex-col gap-4">
            <div class="viewing-request-card flex-between items-center" style="background: var(--bg-muted); padding: 16px; border-radius: 8px; border: 1px solid var(--border-color);">
              <div>
                <span class="status-badge badge badge-light mb-2">Pending Approval</span>
                <div style="font-weight: 700;">Jonathan Miller requested In-Person Tour</div>
                <div style="font-size: 0.85rem; color: var(--text-muted);">For The Grandview Penthouse • Tomorrow at 03:00 PM • Credit: 780</div>
              </div>
              <div class="flex gap-2">
                <button class="btn btn-primary btn-sm btn-approve-viewing">Approve</button>
                <button class="btn btn-outline btn-sm btn-decline-viewing">Decline</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TENANT VIEW (Hidden by default, switchable via tab) -->
      <div id="tenant-view-container" style="display: none;">
        <div class="stats-card-grid">
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
            <div><div class="stat-val">3</div><div class="stat-lbl">Saved Residences</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
            <div><div class="stat-val">1</div><div class="stat-lbl">Upcoming Tour</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
            <div><div class="stat-val">$4,850</div><div class="stat-lbl">Escrow Balance</div></div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>
            <div><div class="stat-val">Current</div><div class="stat-lbl">Rent Status Paid</div></div>
          </div>
        </div>

        <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 32px;">
          <h3 class="mb-4">My Current Active Lease</h3>
          <div class="feature-split">
            <div>
              <h4>The Grandview Skyline Penthouse #2401</h4>
              <p style="color: var(--text-secondary); margin-bottom: 12px;">742 Grandview Blvd • Monthly Rent: $4,850 • Next Due: Nov 1, 2026</p>
              <div class="flex gap-3">
                <button class="btn btn-primary btn-sm" onclick="showToast('Payment portal simulated: Next cycle auto-pay is active')">Pay Rent Now</button>
                <button class="btn btn-outline btn-sm" onclick="showToast('Downloading Encrypted Digital Lease (PDF)...')">Download Lease Agreement</button>
              </div>
            </div>
            <div style="background: var(--bg-muted); padding: 16px; border-radius: 8px;">
              <div style="font-weight: 700; margin-bottom: 6px;">Need Maintenance?</div>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px;">Report any fixture or appliance issue for 60-min emergency dispatch.</p>
              <button class="btn btn-outline btn-sm" onclick="showToast('Maintenance request ticket created. Technician dispatched.')">+ Create Ticket</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>"""
    return header + body + footer

with open("pages/submit-listing.html", "w", encoding="utf-8") as f:
    f.write(build_submit_listing())

with open("pages/dashboard.html", "w", encoding="utf-8") as f:
    f.write(build_dashboard())

print("pages/submit-listing.html and pages/dashboard.html built successfully!")
