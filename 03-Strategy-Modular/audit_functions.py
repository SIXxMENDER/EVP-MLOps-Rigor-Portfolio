import pandas as pd
from datetime import datetime

def clean_and_validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función principal de MLOps para la limpieza de datos financieros.
    1. Elimina duplicados de índice (errores de broker).
    2. Maneja valores nulos usando Forward-Fill (ffill).
    """
    initial_rows = len(df)
    
    
    df = df[~df.index.duplicated(keep='first')]
    

    df.ffill(inplace=True) 
    
    final_rows = len(df)
    print(f"Rigor DQA: Filas ajustadas por duplicidad o NaN: {initial_rows - final_rows}")
    
    return df

def generate_audit_report(df: pd.DataFrame) -> dict:
    """Calcula y reporta las métricas de calidad de datos antes de la ejecución."""
    
    total_rows = len(df)
    missing_values = df.isnull().sum().sum()
    
    report = {
        'total_registros': total_rows,
        'missing_values': missing_values,
        'is_clean': bool(missing_values == 0),
        'check_date': datetime.now().isoformat()
    }
    
    return report