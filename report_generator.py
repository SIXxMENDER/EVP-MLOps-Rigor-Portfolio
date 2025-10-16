import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

def generate_equity_curve(initial_capital=1000, days=100):
    """
    Simula 100 días de retornos aleatorios y genera una curva de capital.
    (El PoW para la habilidad Data Visualization)
    """
    print(f"[{datetime.now()}] Iniciando simulación de Curva de Capital...")
    
    np.random.seed(42) 
    daily_returns = np.random.normal(loc=0.001, scale=0.01, size=days) 
    capital_curve = initial_capital * (1 + daily_returns).cumprod()
    dates = pd.date_range(start='2025-01-01', periods=days, freq='D')
    df = pd.DataFrame({'Capital': capital_curve}, index=dates)
    
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Capital'], color='#0077CC', linewidth=2, label='Equity Curve')
    
    plt.title('Automated Capital Curve Report (100 Days)', fontsize=14, color='white')
    plt.xlabel('Time', color='white')
    plt.ylabel('Capital (USD)', color='white')
    plt.grid(True, linestyle='--', alpha=0.6, color='gray')
    
    plt.gca().set_facecolor('#1e1e1e')
    plt.gcf().set_facecolor('#1e1e1e')
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')
    plt.legend(facecolor='#1e1e1e', edgecolor='white', labelcolor='white')
    
    output_path = 'equity_curve_demo.png'
    plt.savefig(output_path)
    
    print(f"[{datetime.now()}] ✅ Reporte Generado y guardado como '{output_path}'.")
    print(f"Resultado: Capital Final: ${capital_curve[-1]:.2f} USD")
    return output_path

if __name__ == '__main__':
    generate_equity_curve()