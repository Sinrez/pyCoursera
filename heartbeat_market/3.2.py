from bs4 import BeautifulSoup
import requests as req
import sqlite3
import datetime as dt

conn = sqlite3.connect('usd_spread.sqlite')
cursor = conn.cursor()

def get_usd_course():

    now = dt.date.today()
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
    spread = sale_val - buy_val

    return buy_val, sale_val, spread, now

def db_create():
    try:
        # Создаем таблицу
        cursor.execute('''CREATE TABLE IF NOT EXISTS spread (buy_val float , sale_val float, spread float, cur_date text)''')
    except sqlite3.ProgrammingError as er0:
        print(f'Таблица не найдена или уже существует: {er0}')
    except sqlite3.Warning as er1:
        exit(f'Ошибка БД {er1}')

def add_data():
    mydata = get_usd_course()
    cursor.execute("INSERT INTO spread (buy_val, sale_val, spread, cur_date) VALUES (?, ?, ?, ?)", mydata)
    conn.commit()

def return_all_entries():
    cursor.execute('SELECT * FROM spread')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

if __name__ == '__main__':
    db_create()
    add_data()
    return_all_entries()
    cursor.close()
    conn.close()

