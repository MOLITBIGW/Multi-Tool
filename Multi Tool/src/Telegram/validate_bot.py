import aiohttp
import asyncio

async def validate(bot_token):
    validation_url = f"https://api.telegram.org/bot{bot_token}/getMe"
    async with aiohttp.ClientSession() as session:
        async with session.get(validation_url) as resp:
            if resp.status == 200:
                result = await resp.json()
                print(f"Bot is valid! Name: {result['result']['first_name']}, Username: {result['result']['username']}")
            else:
                error_text = await resp.text()
                print(f"Invalid bot token. Error: {error_text}")

async def main():
    bot_token = input("Enter bot token to validate: ").strip()
    await validate(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
