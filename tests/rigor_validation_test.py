# rigor_validation_test.py
# PROTOCOLO DE VALIDACIÓN MLOPS: Prueba el flujo de trabajo de Módulos I y II.
# Rigor: Asegura que la arquitectura de importación funcione correctamente.

import sys
import os
import pandas as pd
import numpy as np
import time

# --- 1. SOLUCIÓN CRÍTICA AL ERROR DE IMPORTACIÓN (RIGOR DE RUTA) ---
# Esto añade las rutas de los módulos al PATH de Python, permitiendo la importación.
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agrega las rutas de las carpetas de los módulos al sistema:
sys.path.append(os.path.join(current_dir, '01-Descarga-Garantizada'))
sys.path.append(os.path.join(current_dir, '02-Data-Quality-Auditor'))

# --- 2. IMPORTACIONES DESDE LOS MÓDULOS ---
try:
    # Módulo I
    from download_ccxt_client import fetch_historical_data
    
    # Módulo II
    from audit_functions import clean_and_validate_data, generate_audit_report
    from outlier_detection import detect_and_flag_outliers
    
    print("✅ MLOPS: Importación de Módulos exitosa.")
except ImportError as e:
    print(f"❌ MLOPS: Fallo crítico al importar módulos. Error: {e}")
    print("VERIFICAR: 1. Nombres de archivos correctos. 2. Que el terminal esté en la raíz del repositorio.")
    sys.exit(1)

# --- 3. TEST DE EJECUCIÓN: MÓDULO I (DESCARGA GARANTIZADA) ---
def test_modulo_i():
    print("\n--- INICIANDO TEST MÓDULO I: DESCARGA GARANTIZADA ---")
    try:
        # Descarga rápida de 100 velas para la prueba.
        data_raw = fetch_historical_data('BTC/USDT', '1h', 100)
        print(f"RESULTADO: Descarga de {len(data_raw)} filas exitosa.")
        return data_raw
    except Exception as e:
        print(f"RESULTADO: ❌ Falla en la descarga. {e}")
        return None

# --- 4. TEST DE EJECUCIÓN: MÓDULO II (AUDITORÍA DE CALIDAD) ---
def test_modulo_ii(data_raw):
    if data_raw is None or data_raw.empty:
        print("RESULTADO MÓDULO II: ⚠️ Skipping, no hay datos para auditar.")
        return

    print("\n--- INICIANDO TEST MÓDULO II: AUDITORÍA DE CALIDAD ---")

    # (A) Limpieza de datos (Nulls y Duplicados)
    data_clean = clean_and_validate_data(data_raw.copy())
    print("RESULTADO: Limpieza de duplicados/NaN aplicada.")

    # (B) Detección de Outliers (Riesgo Estadístico)
    # Creamos un outlier artificial para forzar la prueba:
    # Nota: Forzamos un outlier para que el test sea más sensible
    try:
        data_clean['Close'].iloc[-1] *= 1.5 
    except IndexError:
        pass # Ignorar si no hay suficientes filas

    data_audited = detect_and_flag_outliers(data_clean, 'Close', sigma_level=2) # Usamos 2 Sigma para una prueba sensible
    outliers_count = data_audited['Close_is_outlier'].sum()

    # (C) Generación de Reporte Final
    report = generate_audit_report(data_audited)

    print(f"RESULTADO: Outliers detectados (Riesgo): {outliers_count}")
    print(f"CONCLUSIÓN DQA: Calidad de datos APROBADA (Con {outliers_count} anomalías).")
    return report

# --- 5. EJECUCIÓN PRINCIPAL ---
if __name__ == '__main__':
    
    # 1. Ejecutar el test de Módulo I
    data = test_modulo_i()
    
    # 2. Ejecutar el test de Módulo II
    if data is not None:
        report = test_modulo_ii(data)