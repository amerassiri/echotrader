import requests

TELEGRAM_TOKEN = "PASTE_YOUR_TOKEN"
CHAT_ID = 146993200

message = "🚀 Test message from EchoTrader"

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": message}

response = requests.post(url, data=payload)
print(response.text)
