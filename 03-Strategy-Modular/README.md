# 03 | STRATEGY ARCHITECTURE - Asymmetric Risk Design

## FUNCTIONAL SPECIFICATION: MODULAR RISK LOGIC

This module serves as the core intellectual property, showcasing our mastery in designing strategies with a defined, **asymmetric risk profile**. We build systems that are not reliant on a single market condition, but are dynamically adaptive to both high volatility (Attack) and low volatility (Defense) environments.

The modular structure of this code base allows for rapid iteration and performance scaling, while maintaining granular control over the *Position Sizing* and *Stop Loss* logic—the true drivers of long-term profitability. This modularity is a direct application of the **Separation of Concerns (MLOps)** principle in quantitative finance.

### RIGOR AND QUANTITATIVE DOMAIN:

* **Risk Disaggregation:** Code separation between **Aggressive Logics (Solstice/EMA)** for high-ROI capture and **Defensive Logics (Equinox/ADX)** for capital preservation (P3/P7).
* **Friction Elimination:** Implementation of **Trailing Stop Logic (TSL)** and **Break-Even Protocols** to eliminate frictional losses observed in conventional systems, optimizing the average winning trade size.
* **Indicator Mastery:** Specialized integration of key momentum and volatility indicators (ADX, ATR, RSI, EMA) that demonstrate an understanding of *when not to trade*—a fundamental risk-mitigation tool.
* **Ponderation Logic:** Inclusion of a model that dynamically allocates capital weight to the best-performing strategy at any given moment, mitigating overall portfolio risk drift.

---
