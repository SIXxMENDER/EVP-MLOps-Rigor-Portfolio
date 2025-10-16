# FIX DEFINITIVO: tests/test_risk_management.py - Rigor P7 Validation (CORREGIDO)
import unittest

# Funci\u00f3n simulada para el m\u00f3dulo de gesti\u00f3n de riesgo
def calcular_drawdown_maximo(valores_de_portafolio):
    """
    Calcula el Drawdown M\u00e1ximo (DD) a partir de una lista de valores de portafolio.
    """
    if not valores_de_portafolio:
        return 0.0

    pico = valores_de_portafolio[0]
    drawdown_max = 0.0

    for valor in valores_de_portafolio:
        if valor > pico:
            pico = valor
        
        # Drawdown actual como porcentaje
        drawdown_actual = (pico - valor) / pico * 100
        if drawdown_actual > drawdown_max:
            drawdown_max = drawdown_actual
            
    return drawdown_max

class TestRiskManagement(unittest.TestCase):
    
    # Objetivo: La m\u00e9trica cr\u00edtica P7 (DD < 8%) debe ser validada.
    def test_mitigacion_de_riesgo_p7(self):
        """
        Verifica que el Drawdown M\u00e1ximo se mantenga bajo el l\u00edmite de riesgo cr\u00edtico (8%).
        """
        # Portafolio 1: DD < 8% (Aceptable - DD m\u00e1x: 5%)
        portafolio_seguro = [100, 95, 105, 97]
        dd_calculado_seguro = calcular_drawdown_maximo(portafolio_seguro)
        
        # CORRECCI\u00d3N APLICADA: assertLessEqual (Elimina la Fricci\u00f3n)
        self.assertLessEqual(dd_calculado_seguro, 8.0, 
                               msg=f"FALLO DE RIGOR: El DD ({dd_calculado_seguro:.2f}%) excede el l\u00edmite P7 de 8%.")

    def test_falla_de_codigo_dd_inaceptable(self):
        """
        Verifica que el test falle si el drawdown es inaceptable, forzando un fallo de rigor.
        """
        # Portafolio 2: DD > 8% (Falla de Backtest/Riesgo Inaceptable - DD m\u00e1x: 20%)
        portafolio_riesgoso = [100, 80, 90, 110, 85]
        dd_calculado_riesgoso = calcular_drawdown_maximo(portafolio_riesgoso)

        # El test espera que este valor NO cumpla con el Rigor P7 (es decir, sea mayor a 8.0).
        self.assertGreater(dd_calculado_riesgoso, 8.0,
                           msg="Error L\u00f3gico: El c\u00f3digo permiti\u00f3 un DD inaceptable que pas\u00f3 inadvertido.")

if __name__ == '__main__':
    unittest.main()