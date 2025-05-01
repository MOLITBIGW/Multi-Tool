import aiohttp
import asyncio

async def delete(bot_token):
    async with aiohttp.ClientSession() as session:
        log_out_url = f"https://api.telegram.org/bot{bot_token}/logOut"
        close_url = f"https://api.telegram.org/bot{bot_token}/close"

        print("\nLogging out bot session...")
        async with session.get(log_out_url) as logout_resp:
            logout_result = await logout_resp.text()
            print(f"Logout response: {logout_result}")

        print("Closing bot connection...")
        async with session.get(close_url) as close_resp:
            close_result = await close_resp.text()
            print(f"Close response: {close_result}")

        print("\nBot session closed.")
        print("To fully delete the bot, go to https://t.me/BotFather → /mybots → select bot → Delete Bot.")

async def main():
    bot_token = input("Enter bot token to delete: ").strip()
    await delete(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
