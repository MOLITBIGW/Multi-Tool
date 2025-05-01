import requests
import time

def send_webhook_message(webhook_url, content, tts=False):
    data = {
        "content": content,
        "tts": tts
        
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed. {response.status_code}")

def main():
    webhook_url = input("Enter your webhook URL: ")
    content = input("Enter the message you want to send: ")
    num_threads = int(input("Enter the number of threads: "))
    tts_input = input("Do you want TTS enabled (y/n)? ").lower()
    tts = True if tts_input == "y" else False


    for i in range(num_threads):  
        if i != 0:
            time.sleep(1)  

        send_webhook_message(webhook_url, content, tts)

if __name__ == "__main__":
    main()
