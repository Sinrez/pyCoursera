from bs4 import BeautifulSoup
import requests as req

def get_usd_course():

    url_in = 'https://www.banki.ru/products/currency/bank/sberbank/usd/moskva/#bank-rates'
    resp = req.get(url_in)
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.find_all("td", class_='font-size-large')
    buy_in = str(list(items)[0])
    #вытаскиваем из тегов покупку usd и продажу
    sale_in  = str(list(items)[1])

    buy_val = float(buy_in[buy_in.find('">')+2:buy_in.find('</')].strip().replace(',','.'))
    # вырезаем из тега число - сумму покупки/продажи
    sale_val = float(sale_in[sale_in.find('">')+2:sale_in.find('</')].strip().replace(',','.'))

    return f'USD Покупка: {buy_val} Продажа {sale_val} Спред: {sale_val-buy_val}'



if __name__ == '__main__':
    print(get_usd_course())