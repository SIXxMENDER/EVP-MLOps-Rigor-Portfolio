# 04-Behavioral-Analysis/Behavioral_Bias_Detector.py
# MÓDULO IV: DETECTOR DE SESGO Y NOTICIAS DE ALTO IMPACTO
# Rigor: Demuestra la capacidad de filtrar el ruido informativo (Noticias de Alto Riesgo).

import pandas as pd
from datetime import datetime

def analyze_high_impact_news(api_data: list, keywords: list) -> list:
    """
    Simula la búsqueda de noticias que contienen keywords de alto riesgo macro.
    """
    
    high_impact_events = []
    
    # 1. Palabras clave de Riesgo (Ej. que activan el filtro FINA)
    risk_keywords = ["FED Rate Hike", "Inflation CPI", "NFP", "Tariff War", "Geopolitical Tension"]
    
    # Simulación de análisis de titular
    for item in api_data:
        headline = item.get('headline', '').upper()
        
        # El filtro busca si alguna palabra clave de riesgo está en el titular
        if any(kw.upper() in headline for kw in risk_keywords):
            high_impact_events.append({
                'timestamp': item.get('time', datetime.now().isoformat()),
                'headline': item['headline'],
                'risk_score': 0.95 # Asignamos un score de riesgo alto
            })
            
    return high_impact_events

def generate_risk_report(events: list) -> str:
    """Genera un reporte conciso sobre los eventos de alto riesgo detectados."""
    if not events:
        return "Noticias de Alto Impacto: Cero Eventos Críticos Detectados. Operación Segura."
    
    return f"ALERTA ROJA: {len(events)} eventos de alto impacto detectados. Protocolo FINA activado."

# NOTA: En un sistema real, api_data vendría de una API de noticias financieras.
