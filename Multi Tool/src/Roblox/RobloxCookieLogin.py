from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

BEFORE = "["
AFTER = "]"
INPUT = "[INPUT]"
WAIT = "[WAIT]"
INFO = "[INFO]"
ERROR = "[ERROR]"
white = ""
blue = ""
reset = ""


def ErrorChoice():
    print(f"Invalid choice.")
    exit()

def ErrorModule(e):
    print(f"Module Import Error: {e}")
    exit()

def Error(e):
    print(f"{e}")
    exit()

def Continue():
    input(f"Press Enter to exit...")

try:
    cookie = input(f"Cookies: {white}")

    navigator = "Chrome"
        
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        Error(f"{navigator} not installed or chromedriver not up to date. Details: {e}")

    try:
        driver.get("https://www.roblox.com/Login")
        time.sleep(2) 
        driver.add_cookie({"name": ".ROBLOSECURITY", "value": cookie, "domain": ".roblox.com"})
        print(f"Connected Cookie!")
        
        driver.refresh()
        time.sleep(2)
        
        print(f"Connected!")
        driver.get("https://www.roblox.com/users/profile")
        print(f"If you leave the tool, Chrome will close!")
        Continue()

    except Exception as e:
        Error(f"Failed during Roblox automation. Details: {e}")

except Exception as e:
    Error(e)