from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
new_sale = int(str(soup.find('span', {'id': 'price'})).replace('<span id="price">','').replace(' руб</span>',''))
old_sale = int(str(soup.find('span', {'id': 'old_price'})).replace('<span id="old_price">','').replace(' руб</span>',''))
print(round((old_sale-new_sale)/old_sale*100,1))