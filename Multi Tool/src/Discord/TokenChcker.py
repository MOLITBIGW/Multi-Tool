import requests

def check_token(token):
    headers = {
        'Authorization': token
    }
    
    url = "https://discord.com/api/v10/users/@me"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Token is valid!")
    elif response.status_code == 401:
        print("Invalid token.")
    else:
        print(f"Failed to check token. Status code: {response.status_code}")
        print("Error message:", response.text)

def main():    
    token = input("Enter the Discord token: ")
    
    check_token(token)

if __name__ == "__main__":
    main()
