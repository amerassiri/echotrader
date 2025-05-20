# Placeholder for signal_generator.py 
import pandas as pd

def generate_signal_from_data(data):
    """
    Generate signal based on a basic Moving Average Crossover strategy.
    """
    close_prices = data['Close']

    # Calculate short-term and long-term moving averages
    short_ma = close_prices.rolling(window=5).mean()
    long_ma = close_prices.rolling(window=20).mean()

    # Get the latest crossover
    if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
        return "BUY"
    elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
        return "SELL"
    else:
        return "HOLD"



