from bs4 import BeautifulSoup
import requests as req
import sqlite3
import datetime as dt
from matplotlib import pyplot as plt, MatplotlibDeprecationWarning
import warnings


# начальный вариант соединения с БД. Внесен в каждую функцию, чтобы не держать соединение
# conn = sqlite3.connect('usd_spread.sqlite')
# cursor = conn.cursor()

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
        conn = sqlite3.connect('usd_spread.sqlite')
        cursor = conn.cursor()
        # Создаем таблицу
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS spread (buy_val float , sale_val float, spread float, cur_date date primary key,unique(cur_date))''')
        cursor.close()
        conn.close()
    except sqlite3.ProgrammingError as er0:
        print(f'Таблица не найдена или уже существует: {er0}')
    except sqlite3.Warning as er1:
        exit(f'Ошибка БД {er1}')


def add_data() -> None:
    mydata = get_usd_course()
    try:
        conn = sqlite3.connect('usd_spread.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO spread (buy_val, sale_val, spread, cur_date) VALUES (?, ?, ?, ?)", mydata)
        conn.commit()
        cursor.close()
        conn.close()
    except sqlite3.IntegrityError as er3:
        print(f'За сегодняшнюю дату {dt.date.today()} уже есть запись в базе! {er3} ')


def del_data(del_data) -> None:
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    sql_del_query = """DELETE FROM spread where cur_date = ? """
    cursor.execute(sql_del_query, (del_data,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Запись успешно удалена")


def print_all_entries() -> None:
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT  * FROM spread')
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
    cursor.close()
    conn.close()


def return_all_entries() -> list:
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT  * FROM spread')
    row = cursor.fetchone()
    res = []
    while row is not None:
        res.append(row)
        row = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def make_graph(lst) -> None:
    try:
        x_val = [l[3] for l in lst]
        y_val = [l[2] for l in lst]
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        plt.xlabel('Дата')
        plt.ylabel('Спред')
        plt.title('Динамика спреда покупка-продажа USD $')
        plt.plot(x_val, y_val, color='red')
        plt.show()
    except Exception as ex0:
        print(f'Ошибка при построении графика {ex0}')


if __name__ == '__main__':
    db_create()
    make_graph((return_all_entries()))
    # add_data()
    # print_all_entries()
    # del_data('2022-12-13')
    # return_all_entries()
    # cursor.close()
    # conn.close()
