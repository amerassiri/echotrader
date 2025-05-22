
def generate_rsi_signal(data, window=14):
    close_prices = data["Close"]

    # Handle case if Close is a DataFrame (e.g., from yfinance with multi-column)
    if isinstance(close_prices, pd.DataFrame):
        close_prices = close_prices.iloc[:, 0]  # take first column

    # Not enough data
    if len(close_prices) < window + 1:
        return "HOLD"

    # Calculate RSI
    delta = close_prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=window).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    # Drop any NaNs
    rsi = rsi.dropna()

    # Final check
    if rsi.empty:
        return "HOLD"

    last_rsi = rsi.iloc[-1]

    if last_rsi < 30:
        return "BUY"
    elif last_rsi > 70:
        return "SELL"
    else:
        return "HOLD"

