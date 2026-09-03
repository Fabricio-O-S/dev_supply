"""
Gerador de Currículo Executivo em PDF (Layout Perfeito em 2 Páginas) - Fabrício Oliveira Silva
Autor: Fabrício Oliveira Silva
Descrição: Script Python usando ReportLab para geração de PDF executivo de alta qualidade gráfica.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY


def gerar_pdf_curriculo(destino_pdf: str = "Curriculo_Fabricio_Silva.pdf"):
    # Configuração de Margens (22pt ~ 0.3 polegadas)
    doc = SimpleDocTemplate(
        destino_pdf,
        pagesize=letter,
        leftMargin=24,
        rightMargin=24,
        topMargin=22,
        bottomMargin=22
    )

    styles = getSampleStyleSheet()

    # Cores do Design System
    COLOR_PRIMARY = colors.HexColor("#0f172a")    # Dark Slate
    COLOR_BLUE = colors.HexColor("#2563eb")       # Electric Blue
    COLOR_EMERALD = colors.HexColor("#059669")    # Emerald Green
    COLOR_TEXT = colors.HexColor("#1e293b")       # Dark Body Text
    COLOR_MUTED = colors.HexColor("#64748b")      # Muted Gray
    COLOR_BG_HEADER = colors.HexColor("#090d16")   # Premium Header BG

    # Estilos de Parágrafos
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=23,
        textColor=colors.white,
        alignment=TA_LEFT
    )

    subtitle_style = ParagraphStyle(
        'SubTitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#60a5fa"),
        alignment=TA_LEFT
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#cbd5e1"),
        alignment=TA_RIGHT
    )

    section_title_style = ParagraphStyle(
        'SectionTitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14,
        textColor=COLOR_PRIMARY,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_TEXT,
        alignment=TA_JUSTIFY
    )

    bold_body_style = ParagraphStyle(
        'BoldBodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_PRIMARY
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=COLOR_TEXT,
        leftIndent=8
    )

    story = []

    # 1. CABEÇALHO EXECUTIVO (HEADER BANNER)
    header_left = [
        Paragraph("FABRÍCIO OLIVEIRA SILVA", name_style),
        Spacer(1, 2),
        Paragraph("SUPRIMENTOS &bull; PROCUREMENT &bull; STRATEGIC SOURCING &bull; DEV & DATA", subtitle_style)
    ]

    header_right = [
        Paragraph("Sertãozinho - SP | (16) 99106-9995", contact_style),
        Paragraph("fabricio_la_gnt@hotmail.com", contact_style),
        Paragraph("linkedin.com/in/compradorfabriciosilva", contact_style),
        Paragraph("github.com/Fabricio-O-S | fabricio-o-s.github.io/dev_supply", contact_style)
    ]

    header_table = Table([[header_left, header_right]], colWidths=[348, 216])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_HEADER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))

    # 2. RESUMO EXECUTIVO (TRAJETÓRIA DUAL)
    story.append(Paragraph("RESUMO EXECUTIVO & TRAJETÓRIA DUAL", section_title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_BLUE, spaceAfter=5, spaceBefore=1))
    
    resumo_text = (
        "Profissional com <b>mais de 10 anos de carreira corporativa</b> atuando na interseção estratégica entre "
        "<b>Gestão de Suprimentos (Procurement / Strategic Sourcing)</b> e <b>Desenvolvimento de Software / Engenharia de Dados</b>. "
        "Comprovada experiência em negociações de grande porte (<b>+R$ 1.2M em saving</b>), gestão de almoxarifados "
        "(curva ABC, acuracidade de inventário), governança de cadastros (PDM/NCM) e conformidade com ERPs (TOTVS, SAP). "
        "Especialista no desenvolvimento de automações em <b>Python (Pandas, Flask, ETL XML)</b>, consultas avançadas em <b>SQL</b>, "
        "inteligência de dados no <b>Power BI (DAX)</b> e fluxos integrados no <b>N8N</b> e <b>Power Automate</b>."
    )
    story.append(Paragraph(resumo_text, body_style))
    story.append(Spacer(1, 8))

    # 3. COMPETÊNCIAS TÉCNICAS E DE NEGÓCIOS (TABELA LADO A LADO)
    story.append(Paragraph("COMPETÊNCIAS CHAVE & STACK TECNOLÓGICA", section_title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_EMERALD, spaceAfter=5, spaceBefore=1))

    col_suprimentos = [
        Paragraph("<b>Pilar Suprimentos & Procurement:</b>", bold_body_style),
        Paragraph("&bull; Strategic Sourcing &amp; Negociação de Alto Impacto", bullet_style),
        Paragraph("&bull; Gestão de Indicadores OTIF (On-Time In-Full)", bullet_style),
        Paragraph("&bull; Almoxarifado: Curva ABC, Inventários &amp; Acuracidade", bullet_style),
        Paragraph("&bull; Governança de PDM &amp; Auditoria Fiscal de NCM", bullet_style),
        Paragraph("&bull; Gestão de Contratos, Homologação &amp; SLAs", bullet_style),
        Paragraph("&bull; Domínio de ERPs: TOTVS, SAP, Senior, Sankhya", bullet_style),
    ]

    col_dev_dados = [
        Paragraph("<b>Pilar Desenvolvimento & Engenharia de Dados:</b>", bold_body_style),
        Paragraph("&bull; Python 3: Pandas, Openpyxl, Flask, Requests ETL", bullet_style),
        Paragraph("&bull; SQL: PostgreSQL (bancos em prod), MySQL, SQLite &amp; JOINs", bullet_style),
        Paragraph("&bull; Power BI Impressionador: DAX Avançado &amp; Star Schema", bullet_style),
        Paragraph("&bull; Automação de Processos: N8N, Webhooks &amp; Power Automate", bullet_style),
        Paragraph("&bull; Parsing de XML de NF-e &amp; Conciliação Fiscal", bullet_style),
        Paragraph("&bull; DevOps &amp; Linux: Servidor próprio (Apps, Sites, Bots 24/7 &amp; PostgreSQL)", bullet_style),
    ]

    skills_table = Table([[col_suprimentos, col_dev_dados]], colWidths=[282, 282])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))

    # 4. EXPERIÊNCIA PROFISSIONAL
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", section_title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_BLUE, spaceAfter=6, spaceBefore=1))

    experiencias = [
        {
            "empresa": "Barra Mansa Alimentos",
            "cargo": "Analista de Compras",
            "periodo": "Fevereiro / 2024 – Setembro / 2025 (1 ano e 8 meses)",
            "local": "Sertãozinho - SP",
            "detalhes": [
                "Gestão de aquisições diretas e indiretas (materiais elétricos, automação, hidráulicos, combustíveis e insumos para caldeiras).",
                "Desenvolvimento de dashboards analíticos em Power BI para suporte a tomadas de decisão da diretoria e otimização do spend.",
                "Homologação técnica de novos fornecedores e controle de SLA de entrega para garantir continuidade fabril."
            ]
        },
        {
            "empresa": "SuperFrio Logística Frigorificada",
            "cargo": "Comprador Corporativo",
            "periodo": "Fevereiro / 2023 – Novembro / 2023 (10 meses)",
            "local": "Ribeirão Preto - SP",
            "detalhes": [
                "Aquisição estratégica de produtos e serviços nas áreas de Tecnologia da Informação, Segurança do Trabalho (EPIs) e Construção Civil.",
                "Responsável pelas compras do plano de expansão nacional, assegurando o abastecimento e prazos de abertura de novas filiais."
            ]
        },
        {
            "empresa": "Resolv",
            "cargo": "Analista de Compras Senior",
            "periodo": "Março / 2022 – Fevereiro / 2023 (1 ano)",
            "local": "Ribeirão Preto - SP",
            "detalhes": [
                "Gestão de suprimentos de alimentos e insumos para o abastecimento de mais de 40 unidades operacionais em nível nacional.",
                "Negociações estratégicas de alto volume de compra (saving) e cotação de materiais para obras em novos restaurantes corporativos."
            ]
        },
        {
            "empresa": "Barra Mansa Alimentos",
            "cargo": "Encarregado de Almoxarifado / Comprador",
            "periodo": "Maio / 2020 – Agosto / 2021 (1 ano e 4 meses)",
            "local": "Sertãozinho - SP",
            "detalhes": [
                "Promovido a Encarregado de Almoxarifado após atuação em compras. Gestão direta de estoque, controle de entradas/saídas e Curva ABC.",
                "Organização e acuracidade de inventário rotativo e apoio direto à logística e áreas de produção."
            ]
        },
        {
            "empresa": "JAB Isolantes Térmicos",
            "cargo": "Comprador",
            "periodo": "Março / 2016 – Janeiro / 2019 (2 anos e 11 meses)",
            "local": "Sertãozinho - SP",
            "detalhes": [
                "Compras de materiais de construção civil e isolamento térmico para usinas sucroalcooleiras e plantas industriais.",
                "Análise de cotações técnicas, gestão de contratos de fornecimento e redução de custos operacionais."
            ]
        },
        {
            "empresa": "Gotherma",
            "cargo": "Analista Administrativo / Compras",
            "periodo": "Fevereiro / 2013 – Fevereiro / 2016 (3 anos e 1 mês)",
            "local": "Sertãozinho - SP",
            "detalhes": [
                "Atuação inicial em rotinas administrativas de RH e financeiro com migração e especialização na gestão de compras e suprimentos."
            ]
        }
    ]

    for exp in experiencias:
        exp_header = Table([
            [Paragraph(f"<b>{exp['empresa']}</b> &bull; <font color='#2563eb'><b>{exp['cargo']}</b></font>", bold_body_style),
             Paragraph(f"<font color='#64748b'>{exp['periodo']}</font>", ParagraphStyle('RightText', parent=contact_style, textColor=COLOR_MUTED, fontSize=7.8))]
        ], colWidths=[384, 180])
        exp_header.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        item_block = [exp_header]
        for det in exp['detalhes']:
            item_block.append(Paragraph(f"&bull; {det}", bullet_style))
        item_block.append(Spacer(1, 4))
        
        story.append(KeepTogether(item_block))

    story.append(Spacer(1, 4))

    # 5. FORMAÇÃO ACADÊMICA E CERTIFICAÇÕES (TABELA LADO A LADO)
    story.append(Paragraph("FORMAÇÃO ACADÊMICA & CERTIFICAÇÕES", section_title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_EMERALD, spaceAfter=5, spaceBefore=1))

    col_formacao = [
        Paragraph("<b>Formação Acadêmica:</b>", bold_body_style),
        Paragraph("<b>Pós-Graduação (Lato Sensu):</b> Gestão de Materiais e Suprimentos<br/><font color='#64748b'>Faculdades Prominas (2022)</font>", bullet_style),
        Spacer(1, 2),
        Paragraph("<b>Graduação (Ensino Superior):</b> Tecnologia da Informação<br/><font color='#64748b'>Universidade de Franca - UNIFRAN (2018 – 2021)</font>", bullet_style)
    ]

    col_certificacoes = [
        Paragraph("<b>Certificações &amp; Especializações:</b>", bold_body_style),
        Paragraph("&bull; <b>Power BI Impressionador:</b> DAX Avançado &amp; Modelagem Star Schema", bullet_style),
        Paragraph("&bull; <b>N8N Impressionador:</b> Automação de APIs &amp; Webhooks", bullet_style),
        Paragraph("&bull; <b>Machine Learning em Python:</b> Algoritmos Preditivos &amp; Pandas", bullet_style),
        Paragraph("&bull; <b>Saúde Mental nas Organizações:</b> Indústria em Foco", bullet_style)
    ]

    edu_table = Table([[col_formacao, col_certificacoes]], colWidths=[282, 282])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
    ]))
    story.append(edu_table)

    # Construir PDF
    doc.build(story)
    print(f"Currículo executivo gerado com sucesso em: {destino_pdf}")

if __name__ == "__main__":
    gerar_pdf_curriculo("Curriculo_Fabricio_Silva.pdf")
