from bs4 import BeautifulSoup
import requests as req
import sqlite3
import datetime as dt

conn = sqlite3.connect('usd_spread.sqlite')
cursor = conn.cursor()

def get_usd_course():

    now = dt.date.today()
    url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'
    resp = req.get(url_in)
    soup = BeautifulSoup(resp.text, 'html.parser')
    items_buy = soup.find_all('span', class_='float-convert__btn', id="buy_usd")
    items_sell = soup.find_all('span', class_='float-convert__btn', id="sell_usd")
    # вытаскиваем из тегов покупку usd и продажу
    buy_in = str(items_buy).split()[5]
    sale_in = str(items_sell).split()[5]
    sale_res = float(sale_in[sale_in.find('">') + 2:sale_in.find('</')])
    buy_res = float(buy_in[buy_in.find('">') + 2:buy_in.find('</')])
    spread = sale_res - buy_res

    return buy_res, sale_res, spread, now

def db_create():
    try:
        # Создаем таблицу
        cursor.execute('''CREATE TABLE IF NOT EXISTS spread (buy_val float , sale_val float, spread float, cur_date date )''')
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

