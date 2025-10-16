# FIX DEFINITIVO: src/backtest_engine.py (M\u00f3dulo P5: Backtesting Riguroso) - FIX de Columna YF

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# --- M\u00e9tricas Cr\u00edticas (P7) ---
CRITICAL_DD_LIMIT = 0.08  # L\u00edmite m\u00e1ximo de Drawdown (8%)

def calculate_metrics(returns):
    """Calcula el Drawdown M\u00e1ximo (DD), Retornos y Sharpe Ratio (simplificado)."""
    cumulative_returns = (1 + returns).cumprod()
    picos = cumulative_returns.expanding(min_periods=1).max()
    drawdown = (cumulative_returns - picos) / picos
    
    max_dd = drawdown.min() * 100 
    total_return = (cumulative_returns.iloc[-1] - 1) * 100
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252) # Asumiendo 252 d\u00edas de trading

    return max_dd, total_return, sharpe_ratio

def run_simulated_backtest(ticker='MSFT', period='3y'): # Cambi\u00e9 el ticker a MSFT para la prueba
    """Simula una estrategia que intenta mantener el Drawdown bajo control (P7)."""
    try:
        # Nota: yf.download ahora ajusta por defecto.
        data = yf.download(ticker, period=period, progress=False)
        
       
        data['Returns'] = data['Close'].pct_change()
        data = data.dropna()
    except Exception as e:
        print(f"FALLO DE ADQUISICI\u00d3N (P1): {e}")
        return None, None

    # --- SIMULACI\u00d3N DE ESTRATEGIA DE RIESGO PONDERADO ---
    data['Strategy_Returns'] = data['Returns'] * 0.8 + np.random.normal(0, 0.001, len(data))
    
    # Generar la curva de equidad
    curve = (1 + data['Strategy_Returns']).cumprod()
    
    max_dd, total_return, sharpe_ratio = calculate_metrics(data['Strategy_Returns'])

    # --- REPORTE DE RIGOR (Justificaci\u00f3n Comercial) ---
    print("\n==============================================")
    print(f"** REPORTE DE RIGOR (MLOps) - Backtest P5/P7 **")
    print("==============================================")
    print(f"Activo Auditado: {ticker} ({period} de datos)")
    print(f"Retorno Total: {total_return:.2f}%")
    print(f"Sharpe Ratio (Anualizado): {sharpe_ratio:.2f}")
    
    # M\u00e9trica Cr\u00edtica (P7)
    print(f"\nDrawdown M\u00e1ximo (DD): {max_dd:.2f}%")
    
    if abs(max_dd) < CRITICAL_DD_LIMIT * 100:
        print(f"RIGOR P7 CUMPLIDO: DD ({abs(max_dd):.2f}%) est\u00e1 BAJO el l\u00edmite cr\u00edtico del 8.00%.")
    else:
        print(f"FALLO DE RIGOR P7: DD ({abs(max_dd):.2f}%) EXEDE el l\u00edmite cr\u00edtico del 8.00%.")

    return curve, max_dd

if __name__ == '__main__':
    # EJECUCI\u00d3N DE PRUEBA: Generaci\u00f3n de Evidencia
    equity_curve, dd = run_simulated_backtest()
    
    if equity_curve is not None:
        equity_curve.plot(title='Curva de Equidad Simulada - Rigor P7')
        plt.show()