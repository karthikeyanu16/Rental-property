/**
 * RESIDA - PREMIUM RENTAL PROPERTY LISTING PLATFORM
 * Global JavaScript (main.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initRTL();
  initNavigation();
  initFavorites();
  initComparisonTracker();
  initModals();
  initAccordions();
  initForms();
  initCounters();
});

/* --- Theme Switching (Dark/Light with System Detection) --- */
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle-btn');
  const storedTheme = localStorage.getItem('resida-theme');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  const currentTheme = storedTheme || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', currentTheme);
  updateThemeIcon(currentTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const activeTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('resida-theme', newTheme);
      updateThemeIcon(newTheme);
      showToast(newTheme === 'dark' ? 'Dark mode enabled' : 'Light mode enabled');
    });
  }

  // System preference change listener
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      if (!localStorage.getItem('resida-theme')) {
        const theme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        updateThemeIcon(theme);
      }
    });
  }
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('theme-icon');
  if (!icon) return;
  if (theme === 'dark') {
    icon.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
  } else {
    icon.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }
}

/* --- Right-to-Left (RTL) Layout Toggle --- */
function initRTL() {
  const rtlBtn = document.getElementById('rtl-toggle-btn');
  const storedDir = localStorage.getItem('resida-dir');

  if (storedDir === 'rtl') {
    document.documentElement.setAttribute('dir', 'rtl');
    if (rtlBtn) rtlBtn.textContent = 'LTR';
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
    if (rtlBtn) rtlBtn.textContent = 'RTL';
  }

  if (rtlBtn) {
    rtlBtn.addEventListener('click', () => {
      const currentDir = document.documentElement.getAttribute('dir');
      const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
      document.documentElement.setAttribute('dir', newDir);
      localStorage.setItem('resida-dir', newDir);
      rtlBtn.textContent = newDir === 'rtl' ? 'LTR' : 'RTL';
      showToast(newDir === 'rtl' ? 'RTL layout enabled' : 'LTR layout enabled');
    });
  }
}

/* --- Navigation & Mobile Drawer --- */
function initNavigation() {
  const header = document.querySelector('.site-header');
  const mobileToggle = document.getElementById('mobile-toggle-btn');
  const drawer = document.getElementById('mobile-drawer');
  const overlay = document.getElementById('mobile-drawer-overlay');
  const closeDrawerBtn = document.getElementById('close-drawer-btn');

  // Sticky header on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  function openDrawer() {
    drawer?.classList.add('open');
    overlay?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer?.classList.remove('open');
    overlay?.classList.remove('open');
    document.body.style.overflow = '';
  }

  mobileToggle?.addEventListener('click', openDrawer);
  closeDrawerBtn?.addEventListener('click', closeDrawer);
  overlay?.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && drawer?.classList.contains('open')) {
      closeDrawer();
    }
  });

  drawer?.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

/* --- Property Favorites / Save --- */
function initFavorites() {
  document.addEventListener('click', e => {
    const btn = e.target.closest('.property-fav-btn');
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();

    btn.classList.toggle('active');
    const isSaved = btn.classList.contains('active');
    const propTitle = btn.closest('.property-card')?.querySelector('.property-title')?.textContent || 'Property';

    if (isSaved) {
      btn.style.color = '#f43f5e';
      showToast('Added to shortlisted favorites: ' + propTitle.trim());
    } else {
      btn.style.color = '';
      showToast('Removed from favorites: ' + propTitle.trim());
    }
  });
}

/* --- Property Comparison Tracker --- */
let selectedCompareProperties = [];

function initComparisonTracker() {
  const floatBar = document.getElementById('compare-float-bar');
  const countEl = document.getElementById('compare-count');

  document.addEventListener('change', e => {
    if (!e.target.classList.contains('compare-checkbox')) return;
    const propId = e.target.dataset.id;
    const propTitle = e.target.dataset.title;

    if (e.target.checked) {
      if (selectedCompareProperties.length >= 3) {
        e.target.checked = false;
        showToast('You can compare a maximum of 3 properties at a time.', 'warning');
        return;
      }
      selectedCompareProperties.push({ id: propId, title: propTitle });
      showToast('Added to comparison (' + selectedCompareProperties.length + '/3): ' + propTitle);
    } else {
      selectedCompareProperties = selectedCompareProperties.filter(item => item.id !== propId);
      showToast('Removed from comparison: ' + propTitle);
    }

    if (floatBar && countEl) {
      countEl.textContent = selectedCompareProperties.length;
      if (selectedCompareProperties.length > 0) {
        floatBar.classList.add('visible');
      } else {
        floatBar.classList.remove('visible');
      }
    }
  });
}

/* --- Toast Notification System --- */
function showToast(message, type = 'info') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  
  let iconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>';
  if (type === 'warning') {
    iconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>';
  }

  toast.innerHTML = iconSvg + ' <span>' + message + '</span>';
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

/* --- Modal Dialogs --- */
function initModals() {
  document.addEventListener('click', e => {
    const trigger = e.target.closest('[data-modal-target]');
    if (trigger) {
      e.preventDefault();
      const modalId = trigger.getAttribute('data-modal-target');
      openModal(modalId);
    }

    const closeBtn = e.target.closest('[data-modal-close]');
    if (closeBtn) {
      e.preventDefault();
      const modal = closeBtn.closest('.modal-overlay');
      if (modal) closeModal(modal.id);
    }
  });

  // Close modal when clicking outside dialog
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', e => {
      if (e.target === overlay) {
        closeModal(overlay.id);
      }
    });
  });

  // ESC key listener
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay.open').forEach(modal => {
        closeModal(modal.id);
      });
    }
  });
}

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.remove('open');
  document.body.style.overflow = '';
}

/* --- Accordions --- */
function initAccordions() {
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      const isOpen = item.classList.contains('active');
      
      // Close other accordion items in same group
      item.parentElement.querySelectorAll('.accordion-item').forEach(el => {
        el.classList.remove('active');
      });

      if (!isOpen) {
        item.classList.add('active');
      }
    });
  });
}

/* --- Form Validation & Submission Handling --- */
function initForms() {
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', e => {
      if (form.getAttribute('data-no-ajax') !== null) return;
      e.preventDefault();

      let isValid = true;
      const requiredInputs = form.querySelectorAll('[required]');

      requiredInputs.forEach(input => {
        if (!input.value.trim()) {
          isValid = false;
          input.style.borderColor = '#f43f5e';
          input.addEventListener('input', () => {
            input.style.borderColor = '';
          }, { once: true });
        }
      });

      if (!isValid) {
        showToast('Please fill in all required fields.', 'warning');
        return;
      }

      // Simulated success feedback
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Processing...';
      }

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
        form.reset();
        
        // Check if modal was open
        const modal = form.closest('.modal-overlay');
        if (modal) closeModal(modal.id);

        showToast('Thank you! Your request has been submitted successfully.');
      }, 1000);
    });
  });
}

/* --- Animated Stat Counters --- */
function initCounters() {
  const counters = document.querySelectorAll('.counter-val');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-target') || '0', 10);
        let current = 0;
        const step = Math.ceil(target / 40);
        const timer = setInterval(() => {
          current += step;
          if (current >= target) {
            el.textContent = target.toLocaleString();
            clearInterval(timer);
          } else {
            el.textContent = current.toLocaleString();
          }
        }, 30);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}
