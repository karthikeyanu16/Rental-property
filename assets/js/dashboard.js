/**
 * RESIDA - DASHBOARD JAVASCRIPT (dashboard.js)
 * Landlord & Tenant Portal Management Logic & Interactive Charts
 */

document.addEventListener('DOMContentLoaded', () => {
  initDashboardRoleSwitcher();
  initAnalyticsChart();
  initListingsFilter();
  initViewingActions();
});

/* --- Role Switcher (Landlord vs Tenant View) --- */
function initDashboardRoleSwitcher() {
  const landlordTab = document.getElementById('role-landlord-btn');
  const tenantTab = document.getElementById('role-tenant-btn');
  const landlordView = document.getElementById('landlord-view-container');
  const tenantView = document.getElementById('tenant-view-container');

  if (!landlordTab || !tenantTab) return;

  landlordTab.addEventListener('click', () => {
    landlordTab.classList.add('active');
    tenantTab.classList.remove('active');
    if (landlordView) landlordView.style.display = 'block';
    if (tenantView) tenantView.style.display = 'none';
    showToast('Switched to Landlord & Agent Management Portal');
  });

  tenantTab.addEventListener('click', () => {
    tenantTab.classList.add('active');
    landlordTab.classList.remove('active');
    if (tenantView) tenantView.style.display = 'block';
    if (landlordView) landlordView.style.display = 'none';
    showToast('Switched to Tenant & Resident Hub');
  });
}

/* --- Interactive Canvas Analytics Chart --- */
function initAnalyticsChart() {
  const canvas = document.getElementById('revenue-chart-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

  // Responsive canvas sizing
  function resizeCanvas() {
    const parent = canvas.parentElement;
    canvas.width = parent.clientWidth;
    canvas.height = 280;
    drawChart();
  }

  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const revenueData = [28500, 31000, 34200, 32800, 37500, 41200, 39800, 44000, 42800, 46500, 48200, 52000];
  const inquiriesData = [18, 22, 28, 25, 34, 42, 38, 48, 45, 52, 58, 64];

  function drawChart() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const padding = { top: 30, right: 30, bottom: 40, left: 60 };
    const chartWidth = canvas.width - padding.left - padding.right;
    const chartHeight = canvas.height - padding.top - padding.bottom;

    // Grid lines & labels
    const maxRev = 60000;
    const gridRows = 4;
    ctx.strokeStyle = isDark ? '#24304f' : '#e2e8f0';
    ctx.lineWidth = 1;
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = isDark ? '#94a3b8' : '#64748b';

    for (let i = 0; i <= gridRows; i++) {
      const y = padding.top + (chartHeight / gridRows) * i;
      const val = Math.round(maxRev - (maxRev / gridRows) * i);
      ctx.beginPath();
      ctx.moveTo(padding.left, y);
      ctx.lineTo(canvas.width - padding.right, y);
      ctx.stroke();
      ctx.fillText('$' + (val / 1000) + 'k', 12, y + 4);
    }

    // X Axis Month Labels
    const stepX = chartWidth / (months.length - 1);
    months.forEach((m, idx) => {
      const x = padding.left + stepX * idx;
      ctx.fillText(m, x - 10, canvas.height - 15);
    });

    // Draw Smooth Area Gradient
    const gradient = ctx.createLinearGradient(0, padding.top, 0, padding.top + chartHeight);
    gradient.addColorStop(0, 'rgba(2, 132, 199, 0.35)');
    gradient.addColorStop(1, 'rgba(2, 132, 199, 0.01)');

    ctx.beginPath();
    revenueData.forEach((val, idx) => {
      const x = padding.left + stepX * idx;
      const y = padding.top + chartHeight - (val / maxRev) * chartHeight;
      if (idx === 0) ctx.moveTo(x, y);
      else {
        const prevX = padding.left + stepX * (idx - 1);
        const prevY = padding.top + chartHeight - (revenueData[idx - 1] / maxRev) * chartHeight;
        const cpX = (prevX + x) / 2;
        ctx.bezierCurveTo(cpX, prevY, cpX, y, x, y);
      }
    });

    // Close path for fill
    ctx.lineTo(padding.left + stepX * (months.length - 1), padding.top + chartHeight);
    ctx.lineTo(padding.left, padding.top + chartHeight);
    ctx.closePath();
    ctx.fillStyle = gradient;
    ctx.fill();

    // Draw Line
    ctx.beginPath();
    revenueData.forEach((val, idx) => {
      const x = padding.left + stepX * idx;
      const y = padding.top + chartHeight - (val / maxRev) * chartHeight;
      if (idx === 0) ctx.moveTo(x, y);
      else {
        const prevX = padding.left + stepX * (idx - 1);
        const prevY = padding.top + chartHeight - (revenueData[idx - 1] / maxRev) * chartHeight;
        const cpX = (prevX + x) / 2;
        ctx.bezierCurveTo(cpX, prevY, cpX, y, x, y);
      }
    });
    ctx.strokeStyle = '#0284c7';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Draw Points
    revenueData.forEach((val, idx) => {
      const x = padding.left + stepX * idx;
      const y = padding.top + chartHeight - (val / maxRev) * chartHeight;
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#ffffff';
      ctx.fill();
      ctx.strokeStyle = '#0284c7';
      ctx.lineWidth = 2;
      ctx.stroke();
    });
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);
}

/* --- Filter Table by Status --- */
function initListingsFilter() {
  const tabs = document.querySelectorAll('.table-filter-tab');
  const rows = document.querySelectorAll('.listing-row');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const filter = tab.dataset.filter;

      rows.forEach(row => {
        if (filter === 'all' || row.dataset.status === filter) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });
}

/* --- Viewing Request Actions --- */
function initViewingActions() {
  document.addEventListener('click', e => {
    // Approve viewing
    const approveBtn = e.target.closest('.btn-approve-viewing');
    if (approveBtn) {
      e.preventDefault();
      const card = approveBtn.closest('.viewing-request-card');
      const badge = card?.querySelector('.status-badge');
      if (badge) {
        badge.className = 'badge badge-verified';
        badge.textContent = 'Confirmed';
      }
      approveBtn.parentElement.innerHTML = '<span style="color: var(--accent); font-weight: 600; font-size: 0.85rem;">✓ Confirmed & Calendar Invite Sent</span>';
      showToast('Viewing request approved. Resident has been notified.');
    }

    // Decline viewing
    const declineBtn = e.target.closest('.btn-decline-viewing');
    if (declineBtn) {
      e.preventDefault();
      const card = declineBtn.closest('.viewing-request-card');
      const badge = card?.querySelector('.status-badge');
      if (badge) {
        badge.className = 'badge badge-hot';
        badge.textContent = 'Declined';
      }
      declineBtn.parentElement.innerHTML = '<span style="color: var(--text-muted); font-size: 0.85rem;">Declined</span>';
      showToast('Viewing appointment declined.');
    }
  });
}
