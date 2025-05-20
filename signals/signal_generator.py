# Placeholder for signal_generator.py 
import pandas as pd
import pandas_ta as ta

def generate_signal_from_data(data, short_ma=5, long_ma=20, rsi_period=14):
    """
    Hybrid logic: MA crossover + RSI confirmation
    """
    df = data.copy()

    # Calculate indicators
    df["ma_short"] = df["Close"].rolling(window=short_ma).mean()
    df["ma_long"] = df["Close"].rolling(window=long_ma).mean()
    df["rsi"] = ta.rsi(df["Close"], length=rsi_period)

    # Get latest values
    latest = df.iloc[-1]
    prev = df.iloc[-2]

    # Conditions
    crossover_up = prev["ma_short"] < prev["ma_long"] and latest["ma_short"] > latest["ma_long"]
    crossover_down = prev["ma_short"] > prev["ma_long"] and latest["ma_short"] < latest["ma_long"]

    # Apply hybrid logic
    if crossover_up and latest["rsi"] < 70:
        return "BUY"
    elif crossover_down and latest["rsi"] > 30:
        return "SELL"
    else:
        return "HOLD"


