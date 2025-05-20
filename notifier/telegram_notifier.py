# Placeholder for telegram_notifier.py
import requests

TELEGRAM_TOKEN = "7822038443:AAHed9vajgqt1Z8OldBqEUgL9XtoMkXoJMo"
CHAT_ID = 146993200  # Your confirmed Chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        print(f"[Telegram] Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"[Telegram] Failed to send: {e}")
