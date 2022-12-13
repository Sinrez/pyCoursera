# https://alfabank.ru/currency/

import requests as req
from bs4 import BeautifulSoup

url_in = 'https://alfabank.ru/currency/'
resp = req.get(url_in)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)