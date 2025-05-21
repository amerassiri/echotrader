import yfinance as yf
import pandas as pd

def get_latest_us_data(ticker="AAPL", period="7d", interval="1h"):
    df = yf.download(ticker, period=period, interval=interval)
    df = df.reset_index().set_index("Datetime")
    return df[["Open", "High", "Low", "Close", "Volume"]]
