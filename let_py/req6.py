import requests

last_update_id = 0

while True:
    result = requests.get(
        'https://api.telegram.org/bot/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']

        send_result = requests.get(
            'https://api.telegram.org/bot1693789635:AAH70u4-ZvtNjXNwRO_y4C7szVu4CfDp4aA/sendMessage',
            params={'chat_id': chat_id, 'text': 'Привет от LETPY'}
            )