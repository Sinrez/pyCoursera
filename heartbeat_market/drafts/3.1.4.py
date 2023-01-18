import requests as req

url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'

r = req.head(url_in)
print(r.status_code)
print(r)