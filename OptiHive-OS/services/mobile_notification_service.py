import requests
import os

FIREBASE_SERVER_KEY = os.getenv("FIREBASE_SERVER_KEY") 
FIREBASE_API_URL = "https://fcm.googleapis.com/fcm/send"

def send_notification(token, title, message):
    headers = {
        "Authorization": f"key={FIREBASE_SERVER_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": token,
        "notification": {
            "title": title,
            "body": message
        }
    }
    response = requests.post(FIREBASE_API_URL, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    test_token = "DEVICE_FCM_TOKEN_HERE"
    result = send_notification(test_token, "Battery Alert", "Your battery is below 20%!")
    print("Notification Result:", result)
