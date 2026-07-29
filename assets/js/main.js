/**
 * Portfólio Executivo - Fabrício Silva
 * Lógica principal de interatividade, filtros de projetos, modais e abas de trajetória dual.
 */

document.addEventListener('DOMContentLoaded', () => {
  initProjectFilters();
  initPillarTabs();
  initMobileMenu();
});

/* -------------------------------------------------------------------------- */
/*  1. FILTROS DA GRADE DE PROJETOS                                          */
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
          card.style.display = 'flex';
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
/*  2. ABAS DE TRAJETÓRIA DUAL (SUPRIMENTOS VS DESENVOLVEDOR)                */
/* -------------------------------------------------------------------------- */
function switchPillarTab(targetPillar) {
  const tabBtns = document.querySelectorAll('.pillar-tab-trigger');
  const tabContents = document.querySelectorAll('.pillar-tab-content');

  if (!tabBtns.length || !tabContents.length) return;

  tabBtns.forEach(b => {
    b.classList.remove('active', 'bg-blue-600', 'bg-emerald-600', 'text-white');
    b.classList.add('bg-slate-800/80', 'text-slate-400');
    
    if (b.getAttribute('data-pillar') === targetPillar) {
      if (targetPillar === 'dev') {
        b.classList.add('active', 'bg-blue-600', 'text-white');
      } else {
        b.classList.add('active', 'bg-emerald-600', 'text-white');
      }
      b.classList.remove('bg-slate-800/80', 'text-slate-400');
    }
  });

  tabContents.forEach(content => {
    if (content.getAttribute('id') === `pillar-${targetPillar}`) {
      content.classList.remove('hidden');
      content.classList.add('block');
    } else {
      content.classList.add('hidden');
      content.classList.remove('block');
    }
  });
}

function initPillarTabs() {
  const tabBtns = document.querySelectorAll('.pillar-tab-trigger');
  if (!tabBtns.length) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetPillar = btn.getAttribute('data-pillar');
      switchPillarTab(targetPillar);
    });
  });

  // Verificar se há hash na URL (ex: #dev ou #compras)
  const hash = window.location.hash.toLowerCase();
  if (hash.includes('dev')) {
    switchPillarTab('dev');
  } else if (hash.includes('compras')) {
    switchPillarTab('compras');
  }

  // Ouvir mudanças dinâmicas de hash na mesma página
  window.addEventListener('hashchange', () => {
    const currentHash = window.location.hash.toLowerCase();
    if (currentHash.includes('dev')) {
      switchPillarTab('dev');
    } else if (currentHash.includes('compras')) {
      switchPillarTab('compras');
    }
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

  const techBadges = techStack.map(t => `<span class="inline-block bg-slate-800 text-blue-300 text-xs px-2.5 py-1 rounded-md font-medium mr-1.5 mb-1.5 border border-slate-700">${t}</span>`).join('');

  Swal.fire({
    title: `<span class="text-xl font-bold text-slate-100">${title}</span>`,
    html: `
      <div class="text-left font-sans">
        <img src="${image}" alt="${title}" class="w-full h-48 object-cover rounded-xl mb-4 border border-slate-700">
        <div class="mb-3 flex flex-wrap">${techBadges}</div>
        <p class="text-slate-300 text-sm leading-relaxed mb-4">${description}</p>
      </div>
    `,
    background: '#0f172a',
    color: '#f8fafc',
    showCancelButton: true,
    confirmButtonText: 'Ver Detalhes Completos',
    cancelButtonText: 'Fechar',
    confirmButtonColor: '#2563eb',
    cancelButtonColor: '#334155',
    customClass: {
      popup: 'border border-slate-800 rounded-2xl shadow-2xl backdrop-blur-xl'
    }
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = pageUrl;
    }
  });
}

/* -------------------------------------------------------------------------- */
/*  4. SIMULADOR INTERATIVO TRIBUTÁRIO AO VIVO (SWEETALERT2)                  */
/* -------------------------------------------------------------------------- */
function abrirSimuladorTributario() {
  if (typeof Swal === 'undefined') return;

  Swal.fire({
    title: '<span class="text-xl font-bold text-slate-100 flex items-center gap-2 justify-center"><span class="material-symbols-outlined text-cyan-400">calculate</span> Simulador Tributário ao Vivo (Python Engine)</span>',
    html: `
      <div class="text-left font-sans space-y-4 pt-2">
        <div>
          <label class="text-xs font-semibold text-slate-300 block mb-1">UF Origem -> UF Destino</label>
          <select id="swal-uf" class="w-full bg-slate-950 border border-slate-700 text-slate-100 rounded-xl p-2.5 text-xs focus:ring-2 focus:ring-cyan-500 outline-none">
            <option value="SP-MG">SP -> MG (Interestadual 12% | Interna 18% | MVA 40%)</option>
            <option value="SP-RJ">SP -> RJ (Interestadual 12% | Interna 20% | MVA 45%)</option>
            <option value="PR-SP">PR -> SP (Interestadual 12% | Interna 18% | MVA 35%)</option>
          </select>
        </div>
        <div>
          <label class="text-xs font-semibold text-slate-300 block mb-1">Valor da Mercadoria (R$)</label>
          <input type="number" id="swal-valor" value="50000" class="w-full bg-slate-950 border border-slate-700 text-slate-100 rounded-xl p-2.5 text-xs focus:ring-2 focus:ring-cyan-500 outline-none">
        </div>
        <div id="swal-resultado" class="bg-slate-950 p-4 rounded-xl border border-slate-800 hidden">
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div><span class="text-slate-400 block">DIFAL Estimado:</span><strong id="res-difal" class="text-cyan-400 text-sm">R$ 0,00</strong></div>
            <div><span class="text-slate-400 block">ICMS-ST Estimado:</span><strong id="res-st" class="text-emerald-400 text-sm">R$ 0,00</strong></div>
            <div class="col-span-2 pt-2 border-t border-slate-800 mt-2">
              <span class="text-slate-400 block">Custo Total Desembolsado:</span>
              <strong id="res-total" class="text-slate-100 text-base">R$ 0,00</strong>
            </div>
          </div>
        </div>
      </div>
    `,
    background: '#090d16',
    color: '#f8fafc',
    showCancelButton: true,
    confirmButtonText: 'Calcular Imposto',
    cancelButtonText: 'Fechar',
    confirmButtonColor: '#06b6d4',
    cancelButtonColor: '#334155',
    customClass: {
      popup: 'border border-slate-800 rounded-2xl shadow-2xl backdrop-blur-xl'
    },
    preConfirm: () => {
      const uf = document.getElementById('swal-uf').value;
      const valor = parseFloat(document.getElementById('swal-valor').value) || 0;
      
      let aliqInter = 12.0, aliqDest = 18.0, mva = 40.0;
      if (uf === 'SP-RJ') { aliqDest = 20.0; mva = 45.0; }
      if (uf === 'PR-SP') { aliqDest = 18.0; mva = 35.0; }

      const difal = valor * ((aliqDest - aliqInter) / 100);
      const icmsProprio = valor * (aliqInter / 100);
      const baseSt = valor * (1 + (mva / 100));
      const stBruto = baseSt * (aliqDest / 100);
      const icmsSt = Math.max(0, stBruto - icmsProprio);
      const total = valor + icmsSt;

      document.getElementById('res-difal').innerText = `R$ ${difal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
      document.getElementById('res-st').innerText = `R$ ${icmsSt.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
      document.getElementById('res-total').innerText = `R$ ${total.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
      document.getElementById('swal-resultado').classList.remove('hidden');

      return false; // Manter modal aberto para ver o resultado
    }
  });
}

/* -------------------------------------------------------------------------- */
/*  5. MENU MOBILE                                                            */
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