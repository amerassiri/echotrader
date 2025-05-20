# Placeholder for us_data_collector.py
import yfinance as yf
import pandas as pd

def get_latest_us_data(ticker="AAPL", period="7d", interval="1h"):
    """
    Fetches historical OHLC data for a given US stock ticker.
    Ensures a clean DataFrame format even if yfinance returns a multi-index.
    """
    data = yf.download(ticker, period=period, interval=interval, group_by="ticker")

    # Handle MultiIndex: if it looks like data['AAPL']['Close'], flatten it
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(1)

    return data

