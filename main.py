import os
import requests
import time
from dotenv import load_dotenv

# Ładowanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Pobieranie danych z .env
ISOD_API_KEY = os.getenv("ISOD_API_KEY")
ISOD_USERNAME = os.getenv("ISOD_USERNAME")
PUSHCUT_API_KEY = os.getenv("PUSHCUT_API_KEY")
PUSHCUT_NOTIFICATION_NAME = os.getenv("PUSHCUT_NOTIFICATION_NAME")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
NOTIFICATION_CONTENT = os.getenv("NOTIFICATION_CONTENT") == "1"
# Budowanie URL-i
ISOD_URL = f"http://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsfull&username={ISOD_USERNAME}&apikey={ISOD_API_KEY}"
PUSHCUT_URL = f"https://api.pushcut.io/v1/notifications/{PUSHCUT_NOTIFICATION_NAME}"


# Zmienna do przechowywania ostatniego hasha
last_saved_hash = None


def check_isod_feed():
    global last_saved_hash
    try:
        response = requests.get(ISOD_URL)
        response.raise_for_status()
        feed_data = response.json()

        latest_item = feed_data["items"][0]
        latest_hash = latest_item["hash"]

        if latest_hash != last_saved_hash:
            subject = latest_item["subject"]
            send_pushcut_notification(subject)
            last_saved_hash = latest_hash
            print(f"[.] New notification sent: {subject}")
        else:
            print("[.] No new announcements.")

    except Exception as e:
        print(f"[!] Error fetching ISOD feed: {e}")


def send_pushcut_notification(message):
    headers = {"Content-Type": "application/json", "API-Key": PUSHCUT_API_KEY}
    data = {}
    if NOTIFICATION_CONTENT:
        data = {"text": message}

    try:
        response = requests.post(PUSHCUT_URL, headers=headers, json=data)
        response.raise_for_status()
        print("[.] Notification sent successfully!")
    except Exception as e:
        print(f"[!] Failed to send notification: {e}")


if __name__ == "__main__":
    print("App started, checking for new notifications...")
    while True:
        check_isod_feed()
        time.sleep(CHECK_INTERVAL)
