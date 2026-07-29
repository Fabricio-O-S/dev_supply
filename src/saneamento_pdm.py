"""
Algoritmo de Saneamento de Cadastro de Materiais (PDM & NCM)
Autor: Fabrício Oliveira Silva
Descrição: Higienização de nomenclaturas de insumos MRO e padronização da árvore descritiva.
"""

import re
import pandas as pd
from typing import List, Dict


def padronizar_descricao_pdm(descricao_bruta: str) -> str:
    """
    Aplica regras de higienização de texto para padronização no padrão PDM (Nome Fundamental + Modificadores).
    """
    if not descricao_bruta:
        return ""
    
    # Converte para maiúsculas e remove caracteres especiais desnecessários
    texto = descricao_bruta.upper().strip()
    texto = re.sub(r'\s+', ' ', texto)
    
    # Substituições comuns de abreviações legadas
    substituicoes = {
        r'\bPARAF\b': 'PARAFUSO',
        r'\bSEXT\b': 'SEXTAVADO',
        r'\bZINC\b': 'ZINCADO',
        r'\bMOTOB\b': 'MOTOBOMBA',
        r'\bVALV\b': 'VÁLVULA',
        r'\bELET\b': 'ELÉTRICO'
    }
    
    for padrao, substituto in substituicoes.items():
        texto = re.sub(padrao, substituto, texto)
        
    return texto


def identificar_duplicidades(df_materiais: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa materiais pela descrição PDM limpa para identificar códigos duplicados no estoque.
    """
    df_materiais['descricao_pdm'] = df_materiais['descricao_bruta'].apply(padronizar_descricao_pdm)
    contagem = df_materiais.groupby('descricao_pdm')['codigo_material'].transform('count')
    df_materiais['duplicado'] = contagem > 1
    return df_materiais


if __name__ == "__main__":
    print("=== EXECUTANDO SANEAMENTO DE CADASTRO PDM ===")
    amostra_materiais = pd.DataFrame([
        {"codigo_material": "001", "descricao_bruta": "PARAF SEXT ZINC 1/2X2"},
        {"codigo_material": "002", "descricao_bruta": "PARAFUSO SEXTAVADO ZINCADO 1/2 X 2 UNC"},
        {"codigo_material": "003", "descricao_bruta": "MOTOB WEG 10CV 380V"}
    ])
    
    df_resultado = identificar_duplicidades(amostra_materiais)
    for _, row in df_resultado.iterrows():
        print(f"Código: {row['codigo_material']} | PDM Higienizado: {row['descricao_pdm']} | Duplicado: {row['duplicado']}")
