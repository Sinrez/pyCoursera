import requests
import json

result = requests.get('https://api.telegram.org/bot/getUpdates')

data = result.json()
for update in data['result']:
    print(update['message']['text'])