# Placeholder for main.py
from utils.logger import log_signal
import yaml
from data.us_data_collector import get_latest_us_data
from signals.signal_generator import generate_signal_from_data

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("=== EchoTrader Real-Time Mode ===")
print(f"Markets: {config['markets']}")

# US Data & Signal Generation
if config['markets']['us']:
    print("\n[US Market]")
    us_data = get_latest_us_data("AAPL")  # ✅ This defines us_data
    print("Latest Prices:\n", us_data.tail())
    signal = generate_signal_from_data(us_data)
    print(f"Generated Signal: {signal}")

    # ✅ Logging AFTER us_data and signal are both defined
    log_signal("AAPL", "US", signal, us_data["Close"].iloc[-1])
    from notifier.telegram_notifier import send_telegram_message

...

send_desktop_alert("EchoTrader", f"{ticker} → {signal}")
send_telegram_message(f"📡 EchoTrader\n{ticker} → {signal}")


from data.saudi_data_gateway import get_live_saudi_price

# SAUDI Data & Signal
from data.saudi_data_gateway import get_live_saudi_price
from utils.logger import log_signal
from notifier.desktop_notifier import send_desktop_alert
from notifier.telegram_notifier import send_telegram_message


SAUDI_TICKERS = ["SABIC", "STC", "ALRAJHI", "ARAMCO"]

if config["markets"]["saudi"]:
    print("\n[Saudi Market]")

    for ticker in SAUDI_TICKERS:
        try:
            saudi_data = get_live_saudi_price(ticker)
            print(f"\n{ticker} Prices:\n", saudi_data.tail())

            saudi_signal = generate_signal_from_data(saudi_data)
            print(f"Generated Signal for {ticker}: {saudi_signal}")

            log_signal(ticker, "Saudi", saudi_signal, saudi_data["Close"].iloc[-1])
            send_desktop_alert("EchoTrader Saudi Signal", f"{ticker} → {saudi_signal}")
        except Exception as e:
            print(f"[ERROR] {ticker} failed: {e}")
        from notifier.telegram_notifier import send_telegram_message

...

send_desktop_alert("EchoTrader", f"{ticker} → {signal}")
send_telegram_message(f"📡 EchoTrader\n{ticker} → {signal}")





