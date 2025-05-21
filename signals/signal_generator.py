# Placeholder for signal_generator.py 
import pandas as pd

def generate_signal_from_data(data):
    """
    Generate signal based on Moving Average crossover.
    """
    if "Close" not in data.columns or len(data) < 21:
        return "HOLD"

    close_prices = data["Close"]

    short_ma = close_prices.rolling(window=5).mean()
    long_ma = close_prices.rolling(window=20).mean()

    # Check if the last two values exist and are valid
    try:
        latest_short = short_ma.iloc[-1]
        prev_short = short_ma.iloc[-2]
        latest_long = long_ma.iloc[-1]
        prev_long = long_ma.iloc[-2]
    except IndexError:
        return "HOLD"

    if pd.notna(latest_short) and pd.notna(prev_short) and pd.notna(latest_long) and pd.notna(prev_long):
        if latest_short > latest_long and prev_short <= prev_long:
            return "BUY"
        elif latest_short < latest_long and prev_short >= prev_long:
            return "SELL"

    return "HOLD"





