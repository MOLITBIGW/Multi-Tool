from selenium import webdriver
import time


def Exit():
    input(f"Press Enter to exit...")



def main():
    token = input(f"Enter Discord token: ")

    try:
        navigator = "Chrome"
        print(f"{navigator} Starting...")
        driver = webdriver.Chrome()  
        print(f"{navigator} Ready!")

        script = """
            function login(token) {
                setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                    location.reload();
                }, 2500);
            }
        """

        driver.get("https://discord.com/login")
        driver.execute_script(script + f'\nlogin("{token}")')
        time.sleep(4)
        print(f"Token Connected!")

        Exit()

    except Exception as e:
        Exit()

if __name__ == "__main__":
    main()
