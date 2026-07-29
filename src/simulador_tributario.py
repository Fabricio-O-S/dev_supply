"""
Simulador Tributário Interestadual (ICMS-ST & DIFAL)
Autor: Fabrício Oliveira Silva
Descrição: Módulo de cálculo automatizado de impostos interestaduais para cotações de compras.
"""

import os
from typing import Dict, Any


def calcular_difal(valor_operacao: float, aliq_interestadual: float, aliq_interna_destino: float) -> float:
    """
    Calcula o valor do Diferencial de Alíquota (DIFAL) incidente na operação.
    
    :param valor_operacao: Valor base da mercadoria (R$)
    :param aliq_interestadual: Alíquota da UF de origem (%)
    :param aliq_interna_destino: Alíquota interna da UF de destino (%)
    :return: Valor do DIFAL em reais (R$)
    """
    if valor_operacao <= 0:
        return 0.0
    
    diferenca_aliquota = (aliq_interna_destino - aliq_interestadual) / 100.0
    valor_difal = valor_operacao * max(0.0, diferenca_aliquota)
    return round(valor_difal, 2)


def calcular_icms_st(valor_operacao: float, mva: float, aliq_interestadual: float, aliq_interna_destino: float) -> Dict[str, float]:
    """
    Calcula a Substituição Tributária (ICMS-ST) com base na MVA (Margem de Valor Agregado).
    
    :param valor_operacao: Valor dos produtos (R$)
    :param mva: Margem de Valor Agregado ajustada (%)
    :param aliq_interestadual: Alíquota interestadual (%)
    :param aliq_interna_destino: Alíquota interna do estado de destino (%)
    :return: Dicionário contendo a Base ST, ICMS Próprio, ICMS ST e Custo Total da Compra
    """
    icms_proprio = valor_operacao * (aliq_interestadual / 100.0)
    base_st = valor_operacao * (1 + (mva / 100.0))
    icms_substitutuicao_bruto = base_st * (aliq_interna_destino / 100.0)
    icms_st_liquido = max(0.0, icms_substitutuicao_bruto - icms_proprio)
    custo_total = valor_operacao + icms_st_liquido

    return {
        "valor_operacao": round(valor_operacao, 2),
        "base_st": round(base_st, 2),
        "icms_proprio": round(icms_proprio, 2),
        "icms_st": round(icms_st_liquido, 2),
        "custo_total_compra": round(custo_total, 2)
    }


if __name__ == "__main__":
    print("=== TESTE DO SIMULADOR TRIBUTÁRIO (SP -> MG) ===")
    resultado = calcular_icms_st(valor_operacao=50000.00, mva=40.0, aliq_interestadual=12.0, aliq_interna_destino=18.0)
    print(f"Valor da Mercadoria: R$ {resultado['valor_operacao']:,.2f}")
    print(f"Base de Cálculo ST: R$ {resultado['base_st']:,.2f}")
    print(f"ICMS-ST Calculado:  R$ {resultado['icms_st']:,.2f}")
    print(f"Custo Total Final:  R$ {resultado['custo_total_compra']:,.2f}")
