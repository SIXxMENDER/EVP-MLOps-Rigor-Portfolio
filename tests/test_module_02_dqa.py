# test_module_02_dqa.py
# PROTOCOLO DE RIGOR: PRUEBA UNITARIA PARA EL MÓDULO DE LIMPIEZA DE DATOS (DQA)

import pandas as pd
import numpy as np
import unittest
import sys
import os

# --- 1. SOLUCIÓN CRÍTICA DE RUTA PARA IMPORTAR MÓDULOS (FIX DEFINITIVO) ---
# Subimos un nivel en el directorio para encontrar los archivos de lógica que están en la raíz.
current_dir = os.path.dirname(os.path.abspath(__file__))

# El '..' sube un directorio. Esto le dice a Python: "Busca en la carpeta padre"
sys.path.append(os.path.join(current_dir, '..')) 

try:
    # Importamos la función de la lógica que debería estar en el directorio padre
    from audit_functions import clean_and_validate_data 
    print("✅ TESTEO MÓDULO 02: Funciones de limpieza importadas.")
except ImportError as e:
    print(f"❌ TESTEO MÓDULO 02: Fallo al importar la lógica de limpieza. Error: {e}")
    print("VERIFICAR: Asegúrate de que 'audit_functions.py' esté en la carpeta raíz (un nivel arriba).")
    sys.exit(1)


class TestDataRigor(unittest.TestCase):
    """
    Clase que define las pruebas unitarias para la función clean_and_validate_data.
    """
    
    def setUp(self):
        """Prepara el DataFrame de prueba con datos 'sucios'."""
        self.raw_data = pd.DataFrame({
            'Open': [10.0, 10.1, np.nan, 10.3, 10.3],
            'Close': [9.9, np.nan, 10.2, 10.4, 10.4],
            'Volume': [100, 100, 105, 110, 110]
        }, index=[
            pd.to_datetime('2025-10-01 09:00:00'),
            pd.to_datetime('2025-10-01 09:05:00'),
            pd.to_datetime('2025-10-01 09:05:00'), # Duplicado intencional
            pd.to_datetime('2025-10-01 09:10:00'),
            pd.to_datetime('2025-10-01 09:15:00')
        ])

    def test_A_removes_duplicates_and_nans(self):
        """Prueba que el sistema elimine duplicados y maneje NaNs (Punto Crítico)."""
        
        cleaned_df = clean_and_validate_data(self.raw_data.copy())
        
        # 1. Prueba de Duplicados: El índice duplicado debe eliminarse
        self.assertEqual(len(cleaned_df), 4, "Debe haber 4 filas después de eliminar el duplicado.")
        
        # 2. Prueba de NaN: Los NaNs deben haber sido rellenados (ffill)
        self.assertFalse(cleaned_df.isnull().values.any(), "No debe haber ningún valor nulo restante.")

    def test_B_maintains_data_structure(self):
        """Prueba que la estructura del DataFrame no se rompa."""
        cleaned_df = clean_and_validate_data(self.raw_data.copy())
        
        # La prueba más importante: El número de columnas debe ser el mismo
        self.assertEqual(cleaned_df.shape[1], 3, "El número de columnas (Open, Close, Volume) debe mantenerse.")


# --- EJECUCIÓN DE PRUEBAS ---
if __name__ == '__main__':
    print("\n--- CONSTRUYENDO EL GUARDIÁN 24/7: TESTING MÓDULO II ---")
    # Nota: El argumento argv es necesario para que unittest.main() funcione en VS Code/PowerShell sin errores
    unittest.main(argv=['first-arg-is-ignored'], exit=False)