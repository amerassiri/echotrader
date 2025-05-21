
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from data.us_data_collector import get_latest_us_data
from data.saudi_data_gateway import get_live_saudi_price
from signals.signal_generator import generate_signal_from_data
from signals.rsi_strategy import generate_rsi_signal  # New RSI strategy

st.set_page_config(page_title="EchoTrader Signal Dashboard", layout="centered")

# Title
st.title("📡 EchoTrader Signal Dashboard Live")

# Strategy selection
strategy = st.selectbox("Select Strategy", ["MA Crossover", "RSI Strategy"])

ticker = "AAPL"
data = get_latest_us_data(ticker)

# Show preview
st.subheader("🔍 Data Preview")
st.write(data.tail())

# Generate signal based on selected strategy
if strategy == "MA Crossover":
    signal = generate_signal_from_data(data)
elif strategy == "RSI Strategy":
    signal = generate_rsi_signal(data)
else:
    signal = "HOLD"

st.subheader(f"Signal for {ticker} → :green[{signal}]")

# Chart
fig, ax = plt.subplots()
data["Close"].plot(ax=ax, label="Close Price", linewidth=2)

if strategy == "MA Crossover":
    data["MA5"] = data["Close"].rolling(window=5).mean()
    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA5"].plot(ax=ax, label="MA5", linestyle="--")
    data["MA20"].plot(ax=ax, label="MA20", linestyle=":")

elif strategy == "RSI Strategy":
    import pandas_ta as ta
    data["RSI"] = ta.rsi(data["Close"])
    st.line_chart(data[["Close", "RSI"]].dropna())

ax.set_title("AAPL Price + Signals")
ax.set_xlabel("Time")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)
