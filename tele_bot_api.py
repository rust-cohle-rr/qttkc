import requests

# Telegram Bot API endpoint
BOT_TOKEN = "8606309195:AAGILMXaRUX88o-G8hbiX5-wJSzxUqBt2RM"
CHAT_ID = "123456789"  # Replace with your chat ID

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

# /* Get updates to find the chat ID */
# getMe_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"


response = requests.get(url)
updates = response.json()
if updates.get("result"):
    CHAT_ID = updates["result"][-1]["message"]["chat"]["id"]
else:
    print("No updates found")
    exit()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"cl

data = {
    "chat_id": CHAT_ID,
    "text": "Hello from your bot!"
}

response = requests.post(url, json=data)
print(response.json())