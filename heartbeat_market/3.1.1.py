# https://mainfin.ru/currency/usd/moskva

import requests as req
from bs4 import BeautifulSoup

url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'
resp = req.get(url_in)
soup = BeautifulSoup(resp.text, 'html.parser')
items_buy = soup.find_all('span', class_='float-convert__btn', id="buy_usd")

# print(soup)
# print(items)