# test_module_04_behavioral.py
# PROTOCOLO DE RIGOR: PRUEBA UNITARIA PARA EL MÓDULO DE ANÁLISIS CONDUCTUAL (P4)

import unittest
import sys
import os
from datetime import datetime

# --- 1. SOLUCIÓN CRÍTICA DE RUTA PARA IMPORTAR MÓDULOS (FIX DE RAÍZ FORZADA) ---
# Hemos movido los archivos a la raíz para eliminar el conflicto de rutas.
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir) 

try:
    # Importamos las funciones que vamos a probar
    from Behavioral_Bias_Detector import analyze_high_impact_news, generate_risk_report
    print("✅ TESTEO MÓDULO 04: Funciones de análisis conductual importadas.")
except ImportError as e:
    print(f"❌ TESTEO MÓDULO 04: Fallo al importar la lógica de análisis. Error: {e}")
    sys.exit(1)


class TestBehavioralRigor(unittest.TestCase):
    """
    Clase que define las pruebas unitarias para el filtro de riesgo conductual.
    El objetivo es garantizar que solo los eventos críticos de riesgo (macro) activen la alerta.
    """
    
    def setUp(self):
        """Prepara los datos de prueba."""
        self.critical_keywords = ['FED RATE HIKE', 'INFLATION CPI', 'NFP']
        
        self.test_data = [
            {'time': '2025-10-15', 'headline': 'Global CPI data beats estimates; fears of FED Rate Hike rise.', 'source': 'Bloomberg'}, # 1. CRÍTICA
            {'time': '2025-10-15', 'headline': 'Local restaurant chain expands.', 'source': 'Local News'},                         # 2. RUIDO
            {'time': '2025-10-15', 'headline': 'Strong quarterly Earnings Beat in the tech sector.', 'source': 'CNBC'}              # 3. RUIDO
        ]

    def test_A_detects_critical_macro_risk(self):
        """Prueba que solo los titulares con keywords de riesgo activen la alerta (Precisión)."""
        
        # Ejecutamos el análisis en los datos de prueba
        critical_events = analyze_high_impact_news(self.test_data, self.critical_keywords)
        
        # Debe detectar solo 1 evento crítico (la noticia del FED/CPI)
        self.assertEqual(len(critical_events), 1, "Debe detectar exactamente 1 evento de riesgo crítico.")
        self.assertIn("FED RATE HIKE", critical_events[0]['headline'].upper(), "El evento detectado no es el correcto.")

    def test_B_filters_out_market_noise(self):
        """Prueba que los eventos de bajo riesgo sean ignorados (Filtro)."""
        
        # Creamos una lista solo de ruido. No debe arrojar resultados.
        noise_data = [self.test_data[1], self.test_data[2]]
        noise_events = analyze_high_impact_news(noise_data, self.critical_keywords)

        # La lista de eventos críticos debe estar vacía.
        self.assertEqual(len(noise_events), 0, "No debe detectar alertas críticas en el ruido del mercado.")


# --- EJECUCIÓN DE PRUEBAS ---
if __name__ == '__main__':
    print("\n--- CONSTRUYENDO EL GUARDIÁN 24/7: TESTING MÓDULO IV ---")
    # Nota: El argumento argv es necesario para que unittest.main() funcione en VS Code/PowerShell sin errores
    unittest.main(argv=['first-arg-is-ignored'], exit=False)