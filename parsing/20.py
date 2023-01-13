from collections import defaultdict
import requests

responses = requests.get('https://parsinger.ru/downloads/get_json/res.json').json()

categories = defaultdict(int)
for response in responses:
    categories[response['categories']] += int(response['count'])

print(dict(categories))