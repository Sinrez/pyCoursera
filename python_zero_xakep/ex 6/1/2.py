import requests
import json

# Пример работы с API
# Получаем курс BTC-ETH

s  = requests.get('http://bittrex.com/api/v1.1/public/getmarketsummary?market=BTC-ETH')
data = s.json()
print(data)

print('___________\n')

k = data["result"][0]["Last"]
print(k)
