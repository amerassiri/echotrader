import pandas as pd

def generate_rsi_signal(data, period=14):
    close = data["Close"]
    delta = close.diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    if rsi.iloc[-1] < 30:
        return "BUY"
    elif rsi.iloc[-1] > 70:
        return "SELL"
    else:
        return "HOLD"
