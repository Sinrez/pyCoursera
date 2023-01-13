import requests
from collections import defaultdict

responses = requests.get('http://parsinger.ru/downloads/get_json/res.json').json()
categories = defaultdict(int)
for response in responses:
    categories[response['categories']] += int(response['price'].split()[0]) * int(response['count'])

print(dict(categories))