# test_high_value.py
# PROTOCOLO DE VALIDACIÓN MÓDULOS IV Y V (NEUROCIENCIA & REPORTING MLOPS)

import sys
import os
import pandas as pd
import json
from datetime import datetime 

# --- 1. SOLUCIÓN CRÍTICA AL ERROR DE IMPORTACIÓN (LIMPIEZA Y UNIFICACIÓN DE ALCANCE) ---
# Al mover los archivos a la raíz, usamos la importación directa y la solución de prefijo.
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agrega las rutas de las carpetas para que Python encuentre los archivos de lógica
# que no movimos (como los de Módulo I y II)
sys.path.append(os.path.join(current_dir, '01-Descarga-Garantizada'))
sys.path.append(os.path.join(current_dir, '02-Data-Quality-Auditor'))


# --- 2. IMPORTACIONES DESDE LOS ARCHIVOS EN LA RAÍZ ---
try:
    # Módulo IV (Behavioral) 
    from Behavioral_Bias_Detector import analyze_high_impact_news, generate_risk_report
    
    # Módulo V (MLOps Webhook) - Importamos el módulo completo para usar prefijo y evitar el error de alcance
    import WebHook_Alert_Handler as WH
    
    print("✅ MLOPS: Importación de Módulos IV y V exitosa.")
except ImportError as e:
    print(f"❌ MLOPS: Fallo crítico al importar módulos. Error: {e}")
    sys.exit(1)

# --- 3. TEST DE EJECUCIÓN: MÓDULO IV (FILTRO DE NOTICIAS Y RIESGO) ---
def test_modulo_iv():
    print("\n--- INICIANDO TEST MÓDULO IV: ANÁLISIS CONDUCTUAL ---")
    
    mock_news_data = [
        {'time': datetime.now().isoformat(), 'headline': 'FED Raises Rate to 5.5% - Inflation Fear Rises', 'source': 'Reuters'},
        {'time': datetime.now().isoformat(), 'headline': 'Tech Stock Rallies After Earnings', 'source': 'CNBC'}
    ]
    
    # 1. Ejecutar el filtro de riesgo 
    high_impact_events = analyze_high_impact_news(mock_news_data, keywords=['FED Rate Hike', 'Inflation'])
    
    # 2. Generar el informe de riesgo (el EVP)
    risk_report = generate_risk_report(high_impact_events)
    
    # Verificamos si la lógica de alto impacto funciona
    if "ALERTA ROJA" in risk_report:
        print(f"RESULTADO: ✅ Filtro de Riesgo (Behavioral) APROBADO.")
        print(risk_report)
    else:
        print("RESULTADO: ❌ Fallo. No se detectaron noticias de riesgo crítico.")

# --- 4. TEST DE EJECUCIÓN: MÓDULO V (WEBHOOKS Y REPORTING) ---
def test_modulo_v():
    print("\n--- INICIANDO TEST MÓDULO V: MLOPS & WEBHOOKS ---")
    
    # 1. Simulación de una alerta de trading entrante (Webhook)
    mock_trade_alert = {
        'strategy': 'SOLSTICE_EMA_LONG',
        'action': 'BUY',
        'time': '2025-10-14T20:35:00Z',
        'symbol': 'BTC/USD',
        'price': 62500.50,
        'volume': 0.05
    }
    
    # 2. Procesar la alerta con el manejador de webhook (USANDO EL PREFIJO CORREGIDO)
    webhook_response = WH.process_webhook_alert(mock_trade_alert)
    
    # 3. Validar el output
    if webhook_response.get('status') == 'SUCCESS':
        print(f"RESULTADO: ✅ Webhook Handler APROBADO. Respuesta de MLOps: {webhook_response.get('next_step')}")
    else:
        print(f"RESULTADO: ❌ Fallo del Webhook. Respuesta: {webhook_response.get('message')}")

# --- 5. EJECUCIÓN PRINCIPAL ---
if __name__ == '__main__':
    test_modulo_iv()
    test_modulo_v()