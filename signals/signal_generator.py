# Placeholder for signal_generator.py 
import pandas as pd

def generate_signal_from_data(data):
    """
    Generate signal based on MA crossover.
    """
    close_prices = data["Close"]

    short_ma = close_prices.rolling(window=5).mean()
    long_ma = close_prices.rolling(window=20).mean()

    # Ensure enough data
    if short_ma.isna().sum() > 2 or long_ma.isna().sum() > 2:
        return "HOLD"

    # Avoid invalid comparisons with NaN
    if pd.notna(short_ma.iloc[-1]) and pd.notna(long_ma.iloc[-1]) and pd.notna(short_ma.iloc[-2]) and pd.notna(long_ma.iloc[-2]):
        if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
            return "BUY"
        elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
            return "SELL"

    return "HOLD"




