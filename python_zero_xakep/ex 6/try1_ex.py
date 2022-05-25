# Задание попроще:
# Создайте парсер какого-нибудь популярного новостного сайта с
# сохранением напарсенных новостей в базу данных SQLITE3.
# Сделайте в базе поиск по ключевым словам заголовков новостей.
# Например - ввели "", напечатало нам все ранее напарсенные новости о .

import requests
from bs4 import BeautifulSoup
import sqlite3

# Указываем название файла базы данных
conn = sqlite3.connect('newsdb.sqlite')
cursor = conn.cursor()

try:
        # Создаем таблицу
    cursor.execute('''CREATE TABLE IF NOT EXISTS pynews (news_name text, url_news text)''')
except sqlite3.ProgrammingError:
    print('Таблица не найдена или уже существует')
except sqlite3.Warning:
    exit('Ошибка БД')

def add_notes(news_name, url_news):
    # Вставляем в таблицу pyblog первую запись со значениями title и article
    mydata = (news_name, url_news)
    cursor.execute("INSERT INTO pynews (news_name, url_news) VALUES (?, ?)", mydata)
    conn.commit()

def return_all_notes():
    "чтение всех новостей из БД"
    try:
        print('*' * 40)
        print('Вот cписок новостей: ')
        print('*' * 40 + '\n')
        cursor.execute('SELECT * FROM pynews')
        row = cursor.fetchone()
        while row is not None:
           print(row[0])
           print(row[1])
           print('-------------')
           row = cursor.fetchone()

    except sqlite3.ProgrammingError:
           exit('Синтаксическая ошибка или нет базы')
    except sqlite3.OperationalError:
        exit('Ошибка в запросе к БД')
    except Exception:
        exit('Что-то сломалось')

def find_notes(search):
    "поиск новостей в БД"
    print('-------------')
    try:
        # Делаем выборку записей содержащих строку search и в цикле печатаем их значения
        cursor.execute("""SELECT * FROM pynews WHERE news_name LIKE ('%' || ? || '%' )""", (search,))
        row = cursor.fetchone()
        if row is None:
            print(f'По запросу "{search}" ничего не найдено')
        while row is not None:
            print(row[0])
            print(row[1])
            print('-------------')
            row = cursor.fetchone()

    except sqlite3.ProgrammingError:
           exit('Синтаксическая ошибка или нет базы')
    except sqlite3.OperationalError:
        exit('Ошибка в запросе к БД')
    except Exception:
        exit('Что-то сломалось')

def pars_yandex():
    html = requests.get(r'https://yandex.ru/news').text
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('h2', class_='mg-card__title')
    for x in news:  # Проходим по всем полученным заголовкам
        title = x.find('a').get_text()  # В заголовке находим все ссылки и получаем их текст
        link = x.a.get('href')  # получаем сами ссылки
        add_notes(title, link) # сохраняем в БД

def check_q(d):
    if d.lower() == 'q':
        exit(f'Работа завершена')
    elif not d.isdigit():
        exit(f'Нужно ввести число!')

def main():
    "основной блок программы"
    pars_yandex()
    the_tag = input('Вы работаете с топорной программой парсинга новостей из Яндекса, если решили выйти - введите Q, если нет - любую клавишу :) ').strip().lower()
    while(the_tag != 'q'):
        inp_check = (input('''Введите -
        1 Посмтреть все новости
        2 Искать новость
        q чтобы выйти из программы: ''')).strip()

        check_q(inp_check)
        inp_check = int(inp_check)

        if inp_check == 1:
            return_all_notes()
        elif inp_check == 2:
            print('*' * 20)
            search = input('''Введите слово по которому ищем новость
    (регистр букв имеет значение): ''')
            find_notes(search)
            print('*' * 20)
        elif inp_check == 'q':
            break
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
