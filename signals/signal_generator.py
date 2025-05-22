# Placeholder for signal_generator.py 

st.subheader("🔍 Data Preview")
st.write(data)
st.write("Data type:", type(data))

def generate_signal_from_data(data):
    """
    Safe MA crossover with deep data checks.
    """
    try:
        if data is None:
            return "HOLD"

        if not isinstance(data, pd.DataFrame):
            return "HOLD"

        if "Close" not in data.columns:
            return "HOLD"

        close_prices = data["Close"]
        if isinstance(close_prices, pd.DataFrame):  # Defensive: some yfinance bugs cause this
            close_prices = close_prices.iloc[:, 0]

        # Fill any NaNs
        close_prices = close_prices.fillna(method="ffill")

        # Sanity check
        if len(close_prices) < 21:
            return "HOLD"

        # MAs
        short_ma = close_prices.rolling(window=5).mean()
        long_ma = close_prices.rolling(window=20).mean()

        if any(pd.isna([short_ma.iloc[-1], short_ma.iloc[-2], long_ma.iloc[-1], long_ma.iloc[-2]])):
            return "HOLD"

        latest_short = short_ma.iloc[-1]
        prev_short = short_ma.iloc[-2]
        latest_long = long_ma.iloc[-1]
        prev_long = long_ma.iloc[-2]

        if latest_short > latest_long and prev_short <= prev_long:
            return "BUY"
        elif latest_short < latest_long and prev_short >= prev_long:
            return "SELL"
        return "HOLD"

    except Exception as e:
        print("Signal generation error:", str(e))
        return "HOLD"





