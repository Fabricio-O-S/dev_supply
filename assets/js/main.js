/**
 * Portfólio Executivo - Fabrício Silva
 * Lógica principal de interatividade, tema escuro/claro, filtros e modais.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initProjectFilters();
  initMobileMenu();
});

/* -------------------------------------------------------------------------- */
/*  1. GESTÃO DE TEMA (DARK / LIGHT MODE)                                      */
/* -------------------------------------------------------------------------- */
function initTheme() {
  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
  applyTheme(savedTheme);

  const toggleButtons = document.querySelectorAll('.theme-toggle-btn');
  toggleButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentTheme = document.body.classList.contains('light-mode') ? 'light' : 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      localStorage.setItem('portfolio-theme', newTheme);
    });
  });
}

function applyTheme(theme) {
  if (theme === 'light') {
    document.body.classList.add('light-mode');
    document.documentElement.classList.remove('dark');
  } else {
    document.body.classList.remove('light-mode');
    document.documentElement.classList.add('dark');
  }
}

/* -------------------------------------------------------------------------- */
/*  2. FILTROS DA GRADE DE PROJETOS                                          */
/* -------------------------------------------------------------------------- */
function initProjectFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  if (!filterBtns.length || !projectCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active', 'bg-blue-600', 'text-white'));
      filterBtns.forEach(b => b.classList.add('bg-slate-800', 'text-slate-300'));
      
      btn.classList.add('active', 'bg-blue-600', 'text-white');
      btn.classList.remove('bg-slate-800', 'text-slate-300');

      const category = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (category === 'all' || cardCategory === category) {
          card.style.display = 'block';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.95)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });
}

/* -------------------------------------------------------------------------- */
/*  3. MODAL DE PRÉ-VISUALIZAÇÃO DE PROJETOS (SWEETALERT2)                    */
/* -------------------------------------------------------------------------- */
function openProjectModal(title, description, image, pageUrl, techStack) {
  if (typeof Swal === 'undefined') {
    window.location.href = pageUrl;
    return;
  }

  const techBadges = techStack.map(t => `<span class="inline-block bg-slate-700 text-blue-300 text-xs px-2.5 py-1 rounded-md font-medium mr-1.5 mb-1.5">${t}</span>`).join('');

  Swal.fire({
    title: `<span class="text-xl font-bold text-slate-100">${title}</span>`,
    html: `
      <div class="text-left font-sans">
        <img src="${image}" alt="${title}" class="w-full h-48 object-cover rounded-lg mb-4 border border-slate-700">
        <div class="mb-3 flex flex-wrap">${techBadges}</div>
        <p class="text-slate-300 text-sm leading-relaxed mb-4">${description}</p>
      </div>
    `,
    background: '#1e293b',
    color: '#f8fafc',
    showCancelButton: true,
    confirmButtonText: 'Ver Detalhes Completos',
    cancelButtonText: 'Fechar',
    confirmButtonColor: '#2563eb',
    cancelButtonColor: '#475569',
    customClass: {
      popup: 'border border-slate-700 rounded-xl shadow-2xl'
    }
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = pageUrl;
    }
  });
}

/* -------------------------------------------------------------------------- */
/*  4. MENU MOBILE                                                            */
/* -------------------------------------------------------------------------- */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileNav = document.getElementById('mobile-nav');

  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', () => {
      mobileNav.classList.toggle('hidden');
    });
  }
}