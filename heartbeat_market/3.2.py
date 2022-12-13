from bs4 import BeautifulSoup
import requests as req
import sqlite3
import datetime as dt
from matplotlib import pyplot as plt


conn = sqlite3.connect('usd_spread.sqlite')
cursor = conn.cursor()

def get_usd_course() -> tuple:
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


def db_create() -> None:
    try:
        # Создаем таблицу
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS spread (buy_val float , sale_val float, spread float, cur_date date primary key,unique(cur_date))''')
    except sqlite3.ProgrammingError as er0:
        print(f'Таблица не найдена или уже существует: {er0}')
    except sqlite3.Warning as er1:
        exit(f'Ошибка БД {er1}')


def add_data() ->None:
    mydata = get_usd_course()
    try:
        cursor.execute("INSERT INTO spread (buy_val, sale_val, spread, cur_date) VALUES (?, ?, ?, ?)", mydata)
        conn.commit()
    except sqlite3.IntegrityError as er3:
        print(f'За сегодняшнюю дату {dt.date.today()} уже есть запись в базе! {er3} ')

def del_data(del_data) -> None:
    sql_del_query = """DELETE FROM spread where cur_date = ? """
    cursor.execute(sql_del_query, (del_data, ))
    conn.commit()
    print("Запись успешно удалена")

def print_all_entries() -> None:
    cursor.execute('SELECT  * FROM spread')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def return_all_entries() -> list:
    cursor.execute('SELECT  * FROM spread')
    row = cursor.fetchone()
    res = []
    while row is not None:
        res.append(row)
        row = cursor.fetchone()
    return res

def make_graph(lst) -> None:
    x_val = [l[3] for l in lst]
    y_val = [l[2] for l in lst]
    plt.title('Динамика спреда покупка-продажа USD $')
    plt.plot(x_val, y_val)
    plt.show()


if __name__ == '__main__':
    db_create()
    make_graph((return_all_entries()))
    # add_data()
    # print_all_entries()
    # del_data('2022-12-13')
    #return_all_entries()
    cursor.close()
    conn.close()
