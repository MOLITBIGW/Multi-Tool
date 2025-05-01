import aiohttp
import asyncio

class SpamBot:
    def __init__(self):
        self.bot_token = None
        self.chat_id = None
        self.api_url = None
        self.is_nuking = False
        self.nuke_count = 0

    async def spam_message(self, message, delay=0.1):
        self.is_nuking = True
        async with aiohttp.ClientSession() as session:
            while self.is_nuking:
                try:
                    async with session.post(self.api_url, data={
                        'chat_id': self.chat_id,
                        'text': message
                    }) as resp:
                        if resp.status == 200:
                            self.nuke_count += 1
                            print(f"Message sent ({self.nuke_count})")
                        else:
                            error_text = await resp.text()
                            print(f"Telegram API Error: {resp.status} - {error_text}")
                    await asyncio.sleep(delay)
                except Exception as e:
                    print(f"Request failed: {e}")
                    await asyncio.sleep(1)

    def stop(self):
        self.is_nuking = False

async def main():
    bot_token = input("Enter your bot token: ").strip()
    chat_id = input("Enter target chat ID: ").strip()
    message = input("Enter spam message: ").strip()
    delay = float(input("Enter delay between messages (seconds): ").strip())

    spammer = SpamBot()
    spammer.bot_token = bot_token
    spammer.chat_id = chat_id
    spammer.api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        print("\nPress Ctrl+C to stop.")
        await spammer.spam_message(message, delay)
    except KeyboardInterrupt:
        spammer.stop()
        print(f"\nSpam session ended. Total messages sent: {spammer.nuke_count}")

if __name__ == "__main__":
    asyncio.run(main())
