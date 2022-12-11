from bs4 import BeautifulSoup
import requests as req

resp = req.get('https://www.banki.ru/products/currency/bank/sberbank/usd/moskva/#bank-rates')
soup = BeautifulSoup(resp.text, 'html.parser')
items = soup.find_all("td", class_='font-size-large')
buy_in = str(list(items)[0])
#вытаскиваем из тегов покупку usd и продажу
sale_in  = str(list(items)[1])

buy_val = float(buy_in[buy_in.find('">')+2:buy_in.find('</')].strip().replace(',','.'))
# вырезаем из тега число - сумму покупки/продажи
sale_val = float(sale_in[sale_in.find('">')+2:sale_in.find('</')].strip().replace(',','.'))

print(f'USD Покупка: {buy_val} Продажа {sale_val}')
