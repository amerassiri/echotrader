# Placeholder for web_dashboard.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
from data.us_data_collector import get_latest_us_data
from data.saudi_data_gateway import get_live_saudi_price
from signals.signal_generator import generate_signal_from_data

from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="EchoTrader Dashboard", layout="wide")

# Refresh the dashboard every 60 seconds
st_autorefresh(interval=60000, key="datarefresh")


st.title("📊 EchoTrader Real-Time Dashboard")

# US Market
st.subheader("🇺🇸 US Market (AAPL)")
us_data = get_latest_us_data("AAPL")
st.line_chart(us_data["Close"])
us_signal = generate_signal_from_data(us_data)
st.success(f"US Market Signal for AAPL: {us_signal}")

# Saudi Market
st.subheader("🇸🇦 Saudi Market (SABIC)")
saudi_data = get_live_saudi_price("SABIC")
st.line_chart(saudi_data["Close"])
saudi_signal = generate_signal_from_data(saudi_data)
st.success(f"Saudi Market Signal for SABIC: {saudi_signal}")

st.markdown("---")
st.header("📘 Signal History")

# Load logged signals
log_df = pd.read_csv("logs/signal_log.csv", parse_dates=["datetime"])

# Show full table
st.subheader("📋 Full Signal Log")
st.dataframe(log_df.sort_values("datetime", ascending=False), use_container_width=True)

# BUY vs SELL count
st.subheader("📊 Signal Counts")
signal_counts = log_df["signal"].value_counts()
st.bar_chart(signal_counts)

# Price vs Signal Timeline (optional)
st.subheader("📈 Price vs Signal (Latest Ticker Only)")
latest_ticker = log_df["ticker"].iloc[-1]
ticker_df = log_df[log_df["ticker"] == latest_ticker]

st.line_chart(ticker_df.set_index("datetime")["price"])

from utils.performance import calculate_performance

st.markdown("---")
st.header("💸 EchoTrader Performance Summary")

perf_df = calculate_performance()

# Show running total profit/loss
st.subheader("Cumulative PnL (simulated)")
st.line_chart(perf_df.set_index("datetime")["cumulative"])

# Win/Loss summary
st.subheader("📊 Win/Loss Overview")
wins = (perf_df["pnl"] > 0).sum()
losses = (perf_df["pnl"] < 0).sum()
neutral = (perf_df["pnl"] == 0).sum()
st.write(f"🏆 Wins: {wins} | ❌ Losses: {losses} | ➖ Neutral: {neutral}")
