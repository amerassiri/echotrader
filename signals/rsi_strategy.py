import pandas as pd
import pandas_ta as ta

def generate_rsi_signal(data, lower=30, upper=70):
    if data is None or "Close" not in data.columns or data.empty:
        return "HOLD"

    rsi = ta.rsi(data["Close"])
    if rsi.isna().sum() > 0:
        return "HOLD"

    if rsi.iloc[-1] < lower:
        return "BUY"
    elif rsi.iloc[-1] > upper:
        return "SELL"
    return "HOLD"
