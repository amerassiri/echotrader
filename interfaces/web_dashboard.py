# Placeholder for web_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from signals.signal_generator import generate_signal_from_data

# Load US data
ticker = "AAPL"
data = yf.download(ticker, period="30d", interval="1h")
signal = generate_signal_from_data(data)

# Moving Averages
data["MA5"] = data["Close"].rolling(window=5).mean()
data["MA20"] = data["Close"].rolling(window=20).mean()

# Display Title
st.title("📡 EchoTrader Signal Dashboard")

# Signal Display
st.markdown(f"### Signal for **{ticker}** → `{signal}`")

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data["Close"], label="Close Price", linewidth=1)
ax.plot(data["MA5"], label="MA5", linestyle="--")
ax.plot(data["MA20"], label="MA20", linestyle=":")

# Marker for last signal
last_price = data["Close"].iloc[-1]
if signal == "BUY":
    ax.plot(data.index[-1], last_price, marker="^", color="green", markersize=10)
elif signal == "SELL":
    ax.plot(data.index[-1], last_price, marker="v", color="red", markersize=10)

ax.set_title(f"{ticker} Price + Signals")
ax.set_xlabel("Time")
ax.set_ylabel("Price")
ax.legend()
ax.grid(True)
st.pyplot(fig)

