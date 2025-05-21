# Placeholder for signal_generator.py 
import pandas as pd

def generate_signal_from_data(data):
    """
    Generate signal based on MA crossover (bulletproof version).
    """
    if "Close" not in data.columns or len(data) < 21:
        return "HOLD"

    close_prices = data["Close"].copy()

    # Calculate moving averages
    short_ma = close_prices.rolling(window=5).mean()
    long_ma = close_prices.rolling(window=20).mean()

    # Make sure the last 2 values are valid
    if (
        pd.isna(short_ma.iloc[-1]) or pd.isna(short_ma.iloc[-2])
        or pd.isna(long_ma.iloc[-1]) or pd.isna(long_ma.iloc[-2])
    ):
        return "HOLD"

    # Extract last two values
    latest_short = short_ma.iloc[-1]
    prev_short = short_ma.iloc[-2]
    latest_long = long_ma.iloc[-1]
    prev_long = long_ma.iloc[-2]

    # Compare the MAs for signal
    if latest_short > latest_long and prev_short <= prev_long:
        return "BUY"
    elif latest_short < latest_long and prev_short >= prev_long:
        return "SELL"

    return "HOLD"






