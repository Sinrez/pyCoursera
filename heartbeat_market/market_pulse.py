from bs4 import BeautifulSoup
import requests as req
import sqlite3
import datetime as dt
from matplotlib import pyplot as plt, MatplotlibDeprecationWarning
import warnings
import os
from matplotlib.pyplot import MultipleLocator
from user_agent import make_usr_agent


def check_url(in_url) -> None:
    """
    Функция отправляет запрос HEAD, чтобы определить, существует ли ресурс, не загружая его содержимое
    """
    try:
        r = req.head(in_url, allow_redirects=True, headers=make_usr_agent())
        #405 код учтен как позитивный конкретно для данного ресурса-источника курса
        if r.status_code not in (200,405):
            print(f'Запрошенный ресурс недоступен, код: {r.status_code}')
    except req.exceptions.MissingSchema:
        print('Invalid URL')
    except Exception:
        print('Ошибка формата запрашиваемого ресурса')

def get_usd_course() -> tuple:
    """Функция выполняет загрузку курса USD и расчет спреда"""
    now = dt.date.today()
    url_in = 'https://mainfin.ru/bank/alfabank/currency/usd/moskva'
    check_url(url_in)
    resp = req.get(url_in, headers=make_usr_agent())
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
    "Функция выполняет создание БД для хранения истории курсов и спреда"
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
    """Функция выполняет запись курса и спреда в БД"""
    mydata = get_usd_course()
    try:
        conn = sqlite3.connect('usd_spread.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO spread (buy_val, sale_val, spread, cur_date) VALUES (?, ?, ?, ?)", mydata)
        conn.commit()
        cursor.close()
        conn.close()
        # buy_res, sale_res, spread, now
        print(f'Курс за {mydata[3]} добавлен')
        print(f'Покупка: {mydata[0]} Продажа: {mydata[1]}')
        print(f'Спред: {mydata[1] - mydata[0]}')
    except sqlite3.IntegrityError as er3:
        print(f'За сегодняшнюю дату {dt.date.today()} уже есть запись в базе! {er3} ')
    except TypeError as te:
        if not os.path.exists('usd_spread.sqlite'):
            pass
        else:
            print(f'Произошла ошибка записи в БД {te}')
            # заглушка предупреждения об отсутствии БД после первого создания базы, хотя она уже создана - тупит поток или pyCharm
    except Exception as er4:
        print(f'Произошла ошибка записи в БД {er4}')


def del_data(del_data) -> None:
    """Функция выполняет удаление записи из БД"""
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    sql_del_query = """DELETE FROM spread where cur_date = ? """
    cursor.execute(sql_del_query, (del_data,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Запись успешно удалена")


def print_all_entries() -> None:
    """Функция выводит все записи из БД"""
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

def return_last_entries() -> list:
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    sql_query = """SELECT  * FROM spread where cur_date = ?"""
    cursor.execute(sql_query, (dt.date.today(),))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return f'На {res[0][3]} курс покупки: {res[0][0]} руб за $, курс продажи: {res[0][1]}, спред: {res[0][2]}'


def make_graph(lst) -> None:
    try:
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        fig, ax = plt.subplots(figsize=(8, 8))
        x_val = [l[3] for l in lst]
        y_val = [l[2] for l in lst]
        plt.xlabel('Дата')
        plt.ylabel('Спред')
        x_major_locator = MultipleLocator(2)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.xticks(rotation=30)
        plt.ylim(2,20)
        plt.title('Динамика спреда покупка-продажа USD $')
        plt.plot(x_val, y_val, color='red')
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        plt.show()
    except Exception as ex0:
        print(f'Ошибка при построении графика {ex0}')

def return_graph():
    lst = return_all_entries()
    try:
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        fig, ax = plt.subplots(figsize=(8, 8))
        x_val = [l[3] for l in lst]
        y_val = [l[2] for l in lst]
        plt.xlabel('Дата')
        plt.ylabel('Спред')
        x_major_locator = MultipleLocator(2)
        ax.xaxis.set_major_locator(x_major_locator)
        plt.xticks(rotation=30)
        plt.ylim(2, 20)
        plt.title('Динамика спреда покупка-продажа USD $')
        plt.plot(x_val, y_val, color='red')
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        plt.savefig('sprd.png')
    except Exception as ex0:
        print(f'Ошибка при построении графика {ex0}')


def check_q(d) -> None:
    if d.lower() in ('q','й'):
        exit(f'Работа завершена')


def router() -> None:
    if not os.path.exists('usd_spread.sqlite'):
        print('Подождите, создаю БД!')
        db_create()
        print('БД создана')

    the_tag = input(
        'Вы работаете с программой просмотра спреда курса USD, если решили выйти - введите q, если нет - любую клавишу :) ').strip().lower()
    while (the_tag not in ('q', 'й')):
        inp_check = (input('''Введите -
        1 чтобы добавить курс в БД
        2 чтобы построить график динамики спреда
        3 чтобы вывести все записи курсов из БД
        4 чтобы удалить запись из БД по дате
        5 чтобы создать базу данных для хранения курса и спреда
        q чтобы выйти из программы: ''')).strip()

        check_q(inp_check)
        try:
            inp_check = int(inp_check)
        except ValueError:
            print('Нужно ввести число или q для выхода!')

        if inp_check == 1:
            print(20 * '-')
            add_data()
            print(20 * '-')
        elif inp_check == 2:
            make_graph((return_all_entries()))
        elif inp_check == 3:
            print(20 * '-')
            print_all_entries()
            # print(return_all_entries())
            print(20 * '-')
        elif inp_check == 4:
            print(20 * '-')
            date_del = input('Введите дату в формате YYYY-MM-DD: ')
            del_data(date_del)
        elif inp_check == 5:
            print('Подождите, создаю БД!')
            db_create()
            print('БД создана')
        elif inp_check in ('q', 'й'):
            break

if __name__ == '__main__':
    router()
