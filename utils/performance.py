import pandas as pd

def calculate_performance(log_path="logs/signal_log.csv"):
    df = pd.read_csv(log_path, parse_dates=["datetime"])
    df = df.sort_values("datetime")

    df["next_price"] = df["price"].shift(-1)
    df["pnl"] = 0.0

    for i in range(len(df) - 1):
        if df.iloc[i]["signal"] == "BUY":
            df.at[i, "pnl"] = df.iloc[i+1]["price"] - df.iloc[i]["price"]
        elif df.iloc[i]["signal"] == "SELL":
            df.at[i, "pnl"] = df.iloc[i]["price"] - df.iloc[i+1]["price"]

    df["cumulative"] = df["pnl"].cumsum()
    return df
