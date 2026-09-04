# Contexto do Projeto — Portfólio Dual (Dev & Suprimentos)

## 1. Visão Geral
Site estático (HTML + Tailwind CDN + JS Vanilla) que apresenta a trajetória profissional de Fabrício Oliveira Silva em dois pilares: **Desenvolvimento de Software/Automação/Dados** e **Gestão de Suprimentos & Compras**. Serve como portfólio público (GitHub Pages) para recrutadores e clientes, com estudos de caso individuais por projeto.

## 2. Stack & Setup
- **Frontend:** HTML5, Tailwind CSS via CDN, JavaScript Vanilla, Google Material Symbols, FontAwesome, SweetAlert2.
- **Backend/Automação (scripts em `src/`):** Python 3 — `conciliacao_nfe.py`, `gerar_curriculo_pdf.py`, `rotina_backup.py`, `saneamento_pdm.py`, `simulador_tributario.py`.
- **Sem servidor/banco em produção** — o site é estático; os scripts em `src/` são as automações que embasam os estudos de caso, não rodam integrados ao site.
- **Comandos úteis:**
  - Servir localmente: `python -m http.server 8000` na raiz do projeto.
  - Rodar um script isolado: `python src/<script>.py` (checar dependências em `requirements.txt`).

## 3. Diário de Desenvolvimento

### Concluído
- Estrutura dual (`index.html` + `curriculo.html`) com abas Dev/Suprimentos.
- 8 páginas de estudo de caso (`projeto_*.html`) com CTA de WhatsApp no rodapé de cada uma.
- Currículo executivo em PDF de página única (`Curriculo_Fabricio_Silva.pdf`) linkado em `curriculo.html`.
- Grade de 27 repositórios do GitHub em `curriculo.html` com títulos traduzidos/descritivos (não usa mais o nome técnico do repo como título do card — 2026-09-04).
- Substituição das imagens antigas do template (`pic01.jpg`...`saneamento.png`) por thumbnails `.webp` reais dos dashboards de cada projeto.
- Rodapé padronizado em todas as páginas com "Fabrício Oliveira Silva" (2026-09-04).

### Pendências conhecidas
- `Profile.pdf` na raiz estava órfão (não referenciado em nenhum HTML) — avaliar remoção definitiva ou uso.
- `tests/` e `config/` vazios — sem testes automatizados e sem `.env.example` (aceitável enquanto o site for 100% estático, sem backend).
- Sem `robots.txt`/`sitemap.xml` (opcional, melhoria de SEO).

### Lições aprendidas
- Títulos de cards de portfólio não devem repetir o slug técnico do repositório GitHub (ex.: `devops-api-cloud`) — usar nome de negócio/descritivo para leitura humana, mantendo o link técnico como CTA separado ("Acessar no GitHub").

## 4. Regras de Negócio e Padrões
- Design fixo "Obsidian Glass 2.0" (fundo `#090d16`), não alterar paleta sem pedido explícito.
- Toda página de projeto (`projeto_*.html`) segue o mesmo layout: header, corpo do case, CTA de WhatsApp + "Ver Outros Projetos", footer padrão.
- Repositórios corporativos privados na grade de `curriculo.html` **não** recebem link para GitHub (só a tag "Repositório Corporativo Privado") — não adicionar `href` para eles.
