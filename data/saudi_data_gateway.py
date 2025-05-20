# Placeholder for saudi_data_gateway.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_live_saudi_price(ticker_name="SABIC"):
    # You can later replace this with Argaam/Tadawul APIs or scraper
    simulated_data = {
        "SABIC": [111.2, 112.0, 112.3, 112.4, 112.1],
        "STC":   [39.2, 39.5, 39.6, 39.9, 39.7],
        "ALRAJHI": [84.0, 84.2, 84.4, 84.3, 84.1],
        "ARAMCO": [32.1, 32.2, 32.4, 32.3, 32.2],
    }

    prices = simulated_data.get(ticker_name.upper())
    if not prices:
        raise Exception(f"{ticker_name} not found in simulated feed.")

    df = pd.DataFrame({
        "Date": pd.date_range(end=pd.Timestamp.today(), periods=5, freq="D"),
        "Close": prices
    }).set_index("Date")

    return df



