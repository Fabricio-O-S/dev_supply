/**
 * Tema Switcher para o Portfólio
 * Gerencia a troca entre modo claro e modo escuro com persistência
 */

(function() {
    // 1. Verificar se há preferência salva ou se o sistema prefere dark
    const savedTheme = localStorage.getItem('portfolio-theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // 2. Aplicar o tema inicial (antes do DOM carregar para evitar flash de cor)
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.body.classList.add('dark-mode');
    }
})();

document.addEventListener('DOMContentLoaded', () => {
    const header = document.getElementById('header');
    if (!header) return;

    // 3. Criar o botão de toggle
    const toggleBtn = document.createElement('div');
    toggleBtn.id = 'theme-toggle';
    toggleBtn.className = 'theme-toggle-btn';
    toggleBtn.innerHTML = `
        <i class="fas fa-moon moon-icon"></i>
        <i class="fas fa-sun sun-icon"></i>
    `;
    
    // Inserir no início do cabeçalho
    const iconsUl = header.querySelector('.icons');
    if (iconsUl) {
        const li = document.createElement('li');
        li.appendChild(toggleBtn);
        iconsUl.insertBefore(li, iconsUl.firstChild);
    }

    // 4. Lógica de clique
    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('portfolio-theme', isDark ? 'dark' : 'light');
        
        // Feedback visual imediato
        toggleBtn.classList.add('clicked');
        setTimeout(() => toggleBtn.classList.remove('clicked'), 300);
    });
});
