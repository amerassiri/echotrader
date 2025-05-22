# Placeholder for signal_generator.py 
import pandas as pd
import streamlit as st

def generate_signal_from_data(data):
    st.subheader("🔍 Data Preview")
    st.write(data)

    if data is None or data.empty:
        return "HOLD"

    if "Close" not in data.columns:
        st.warning("⚠️ 'Close' column is missing from data.")
        return "HOLD"

    close_prices = data["Close"].copy()

    if len(close_prices) < 20:
        st.info("Not enough data to compute moving averages.")
        return "HOLD"

    short_ma = close_prices.rolling(window=5).mean()
    long_ma = close_prices.rolling(window=20).mean()

    # Defensive check to avoid ambiguity
    if pd.isna(short_ma.iloc[-1]) or pd.isna(long_ma.iloc[-1]) or pd.isna(short_ma.iloc[-2]) or pd.isna(long_ma.iloc[-2]):
        return "HOLD"

    if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
        return "BUY"
    elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
        return "SELL"
    else:
        return "HOLD"




