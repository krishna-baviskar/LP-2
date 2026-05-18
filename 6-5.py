class StockTradingExpertSystem:
    def __init__(self):
        print("--- Quantitative Stock Market Expert Trading System Initialized ---")

    def generate_trade_signal(self, rsi, price_above_200sma, macd_crossover):
        # Rule Base Rules Architecture
        if rsi < 30 and price_above_200sma == 'yes' and macd_crossover == 'bullish':
            return "Action: STRONG BUY. Rationale: Asset structurally uptrending, deeply oversold with momentum convergence."
        elif rsi > 70 and price_above_200sma == 'no' and macd_crossover == 'bearish':
            return "Action: STRONG SELL / SHORT. Rationale: Asset structurally downtrending, severely overbought, momentum divergence."
        elif rsi < 30 and price_above_200sma == 'no':
            return "Action: HOLD / ACCUMULATE MINIMAL. Rationale: Asset oversold but trapped under dominant long-term macro resistance."
        elif rsi > 70 and price_above_200sma == 'yes':
            return "Action: HOLD / PARTIAL PROFIT TAKING. Rationale: Bullish trend intact but near-term momentum exhausted."
        else:
            return "Action: NO SIGNAL / WAIT. Rationale: Metrics consolidating within standard mean-reversion brackets."

# Interactive Interface
try:
    current_rsi = float(input("Enter 14-period Relative Strength Index (RSI) value (0-100): "))
    sma = input("Is the asset spot price trading above its historical 200-day SMA? (yes/no): ").strip().lower()
    macd = input("Enter standard MACD Line indicator condition (bullish / bearish / neutral): ").strip().lower()

    signal = StockTradingExpertSystem().generate_trade_signal(current_rsi, sma, macd)
    print(f"\n[Market Execution Strategy]\n{signal}")
except ValueError:
    print("Invalid indicator threshold entered.")
