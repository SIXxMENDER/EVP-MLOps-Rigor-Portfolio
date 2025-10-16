# 02-Data-Quality-Auditor/outlier_detection.py
# MÓDULO II: DATA QUALITY AUDITOR (DQA) - Detección de Anomalías
# Rigor: Uso de la Regla 3-Sigma (Desviación Estándar) para marcar extremos.

import pandas as pd
import numpy as np

def detect_and_flag_outliers(df: pd.DataFrame, column: str, sigma_level: int = 3) -> pd.DataFrame:
    """
    Detecta y marca valores atípicos (outliers) en una columna usando la Regla 3-Sigma.
    (La base de la mitigación de riesgo para datos)
    """
    if df.empty or column not in df.columns:
        return df

    # Calcula la media y la desviación estándar (STD)
    mean = df[column].mean()
    std = df[column].std()
    
    # Define los límites (3-Sigma Rule)
    lower_bound = mean - (std * sigma_level)
    upper_bound = mean + (std * sigma_level)
    
    # Crea una nueva columna para marcar el outlier (el riesgo)
    is_outlier = (df[column] < lower_bound) | (df[column] > upper_bound)
    df[f'{column}_is_outlier'] = is_outlier.astype(int)
    
    return df
    
def count_outliers(df: pd.DataFrame, column: str) -> int:
    """Devuelve el número total de outliers detectados."""
    outlier_col = f'{column}_is_outlier'
    if outlier_col in df.columns:
        return df[outlier_col].sum()
    return 0
