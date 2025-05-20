# Placeholder for logger.py
import csv
from datetime import datetime

def log_signal(ticker, market, signal, price):
    log_entry = {
        "datetime": datetime.now().isoformat(),
        "ticker": ticker,
        "market": market,
        "signal": signal,
        "price": price
    }

    with open("logs/signal_log.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=log_entry.keys())
        writer.writerow(log_entry)
