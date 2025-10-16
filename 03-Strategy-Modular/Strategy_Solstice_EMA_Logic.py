import backtrader as bt
class SolsticeEMA_Asymmetric(bt.Strategy):
    params = (
        ('ema_short', 9), 
        ('ema_long', 21),
        ('atr_period', 14),
        ('atr_multiplier', 3.0),
        ('risk_pct', 0.025),      
        ('short_risk_factor', 0.70), 
        ('rr_ratio', 2.8),      
    
    def __init__(self):
        self.ema_fast = bt.indicators.EMA(self.data.close, period=self.p.ema_short)
       als self.ema_slow = bt.indicators.EMA(self.data.close, period=self.p.ema_long)
        self.atr_val = bt.indicators.ATR(self.data, period=self.p.atr_period)
        
    def next(self):
        if self.position: return 

        stop_loss_base_dist = self.atr_val[0] * self.p.atr_multiplier
        
        long_signal = bt.indicators.crossover(self.ema_fast, self.ema_slow)
        short_signal = bt.indicators.crossunder(self.ema_fast, self.ema_slow)
        
        if long_signal:
            final_sl_dist = stop_loss_base_dist
            final_tp_dist = final_sl_dist * self.p.rr_ratio     
        elif short_signal:
            
            final_sl_dist = stop_loss_base_dist * self.p.short_risk_factor
            final_tp_dist = final_sl_dist * self.p.rr_ratio
            
        