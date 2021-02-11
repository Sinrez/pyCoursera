import requests

result = requests.get('https://www.nbrb.by/api/exrates/rates/usd?parammode=2')
data = result.json()
# print(data["Cur_OfficialRate"])
print(data)