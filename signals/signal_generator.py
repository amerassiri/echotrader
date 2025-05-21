# Placeholder for signal_generator.py 
import pandas as pd

def generate_signal_from_data(data):
    """
    Generate signal based on MA crossover.
    Fully protected against empty data, missing columns, and NaNs.
    """
    if data is None or len(data) < 21:
        return "HOLD"

    if "Close" not in data.columns:
        return "HOLD"

    close_prices = data["Close"].copy()

    if close_prices.isna().sum() > 0:
        close_prices = close_prices.fillna(method="ffill")

    try:
        short_ma = close_prices.rolling(window=5).mean()
        long_ma = close_prices.rolling(window=20).mean()
    except Exception as e:
        print("Rolling MA error:", e)
        return "HOLD"

    if (
        pd.isna(short_ma.iloc[-1]) or pd.isna(short_ma.iloc[-2])
        or pd.isna(long_ma.iloc[-1]) or pd.isna(long_ma.iloc[-2])
    ):
        return "HOLD"

    latest_short = short_ma.iloc[-1]
    prev_short = short_ma.iloc[-2]
    latest_long = long_ma.iloc[-1]
    prev_long = long_ma.iloc[-2]

    if latest_short > latest_long and prev_short <= prev_long:
        return "BUY"
    elif latest_short < latest_long and prev_short >= prev_long:
        return "SELL"

    return "HOLD"






