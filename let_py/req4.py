import requests
import json

result = requests.get('https://www.nbrb.by/api/exrates/rates/usd?parammode=2')
data = json.loads(result.text)
print(data["Cur_OfficialRate"])
# print(data)