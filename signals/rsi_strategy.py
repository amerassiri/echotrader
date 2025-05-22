import pandas as pd

def generate_rsi_signal(data, window=14):
    close_prices = data["Close"].copy()
    
    # Calculate RSI using pandas
    delta = close_prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    # Protect against short data
    if rsi.isna().sum() > len(rsi) - 2:
        return "HOLD"

    # Generate signal
    if rsi.iloc[-1] < 30:
        return "BUY"
    elif rsi.iloc[-1] > 70:
        return "SELL"
    else:
        return "HOLD"
