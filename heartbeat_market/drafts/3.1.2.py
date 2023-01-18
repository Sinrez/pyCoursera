# https://mainfin.ru/currency/usd/moskva

import requests as req
from bs4 import BeautifulSoup

url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'
resp = req.get(url_in)
soup = BeautifulSoup(resp.text, 'html.parser')
items_buy = soup.find_all('span', class_='float-convert__btn', id="buy_usd")
items_sell = soup.find_all('span', class_='float-convert__btn', id="sell_usd")
# вытаскиваем из тегов покупку usd и продажу
buy_in = str(items_buy).split()[5]
sale_in = str(items_sell).split()[5]
sale_res = float(sale_in[sale_in.find('">')+2:sale_in.find('</')])
buy_res = float(buy_in[buy_in.find('">')+2:buy_in.find('</')])
print(buy_res)
print(items_sell)