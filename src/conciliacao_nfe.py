"""
Motor de Conciliação Fiscal de NF-e (XML vs ERP)
Autor: Fabrício Oliveira Silva
Descrição: Leitura e extração de alíquotas e impostos de XMLs de fornecedores e comparação contra o ERP.
"""

import xml.etree.ElementTree as ET
import pandas as pd
from typing import List, Dict, Any


def extrair_dados_xml_nfe(xml_content: str) -> Dict[str, Any]:
    """
    Realiza o parsing das tags estruturadas da Nota Fiscal Eletrônica (NFe).
    """
    root = ET.fromstring(xml_content)
    namespace = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    
    # Extração de Chave e Dados do Emitente
    chave_access = root.find('.//nfe:infNFe', namespace).attrib.get('Id', '').replace('NFe', '')
    cnpj_emit = root.find('.//nfe:emit/nfe:CNPJ', namespace).text if root.find('.//nfe:emit/nfe:CNPJ', namespace) is not None else ""
    raz_social = root.find('.//nfe:emit/nfe:xNome', namespace).text if root.find('.//nfe:emit/nfe:xNome', namespace) is not None else ""
    
    # Totais da Nota
    v_prod = float(root.find('.//nfe:ICMSTot/nfe:vProd', namespace).text or 0.0)
    v_icms = float(root.find('.//nfe:ICMSTot/nfe:vICMS', namespace).text or 0.0)
    v_ipi = float(root.find('.//nfe:ICMSTot/nfe:vIPI', namespace).text or 0.0)
    v_nf = float(root.find('.//nfe:ICMSTot/nfe:vNF', namespace).text or 0.0)
    
    return {
        "chave_nfe": chave_access,
        "cnpj_emitente": cnpj_emit,
        "razao_social": raz_social,
        "valor_produtos": v_prod,
        "valor_icms_xml": v_icms,
        "valor_ipi_xml": v_ipi,
        "valor_total_xml": v_nf
    }


def conciliar_contra_erp(dados_xml: Dict[str, Any], pedido_erp: Dict[str, Any]) -> Dict[str, Any]:
    """
    Cruza as informações extraídas do XML contra os dados gravados na Ordem de Compra do ERP.
    """
    divergencia_preco = abs(dados_xml["valor_total_xml"] - pedido_erp["valor_total_erp"]) > 0.05
    divergencia_icms = abs(dados_xml["valor_icms_xml"] - pedido_erp["valor_icms_erp"]) > 0.05
    
    status = "APROVADO"
    if divergencia_preco or divergencia_icms:
        status = "DIVERGÊNCIA IDENTIFICADA"
        
    return {
        "chave_nfe": dados_xml["chave_nfe"],
        "fornecedor": dados_xml["razao_social"],
        "valor_xml": dados_xml["valor_total_xml"],
        "valor_erp": pedido_erp["valor_total_erp"],
        "status_conciliacao": status,
        "divergencia_precos": divergencia_preco,
        "divergencia_impostos": divergencia_icms
    }


if __name__ == "__main__":
    print("=== MOTOR DE CONCILIAÇÃO FISCAL XML vs ERP ===")
    dados_exemplo_xml = {
        "chave_nfe": "35230800012345678901234567890123456789012345",
        "cnpj_emitente": "12.345.578/0001-80",
        "razao_social": "FORNECEDOR DE EMBALAGENS SA",
        "valor_produtos": 1250.00,
        "valor_icms_xml": 225.00,
        "valor_ipi_xml": 0.00,
        "valor_total_xml": 1256.50
    }
    
    pedido_exemplo_erp = {
        "valor_total_erp": 1256.50,
        "valor_icms_erp": 225.00
    }
    
    resultado = conciliar_contra_erp(dados_exemplo_xml, pedido_exemplo_erp)
    print(f"Status da Nota: {resultado['status_conciliacao']}")
    print(f"Fornecedor: {resultado['fornecedor']}")
    print(f"Valor XML: R$ {resultado['valor_xml']:.2f} | Valor ERP: R$ {resultado['valor_erp']:.2f}")
