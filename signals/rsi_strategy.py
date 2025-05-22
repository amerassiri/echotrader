import pandas as pd

def generate_rsi_signal(data, window=14):
    close_prices = data["Close"].copy()

    if len(close_prices) < window + 1:
        return "HOLD"  # Not enough data for RSI calculation

    # Calculate RSI
    delta = close_prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    # Ensure last RSI value exists
    if pd.isna(rsi.iloc[-1]).item():
        return "HOLD"

    # Signal logic
    if rsi.iloc[-1] < 30:
        return "BUY"
    elif rsi.iloc[-1] > 70:
        return "SELL"
    else:
        return "HOLD"
