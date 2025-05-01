import requests

webhook_url = input("Please Enter The Webhook URL: ")

response = requests.delete(webhook_url)

if response.status_code == 204:
    print('Webhook deleted successfully.')
else:
    print(f'Failed to delete webhook. Status code: {response.status_code}')
    print(response.text)
