# Создайте программу которая позволяет вести дневник,
# открывая файл в режиме дозаписи строк в конец файла ('a')
# и записывает полученную от юзера информацию.

#решение через БД

import time
import sqlite3

# Указываем название файла базы данных
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

try:
    # Создаем таблицу
    cursor.execute('''CREATE TABLE IF NOT EXISTS pynotes (dt text, note_name text, note_text text)''')
except sqlite3.ProgrammingError:
    print('Таблица не найдена или уже существует')
except sqlite3.Warning:
    exit('Ошибка БД')

def add_notes(dt, note_name, note_text):
    # Вставляем в таблицу pyblog первую запись со значениями title и article
    mydata = (dt, note_name, note_text)
    cursor.execute("INSERT INTO pynotes (dt, note_name, note_text) VALUES (?, ?, ?)", mydata)
    conn.commit()

def input_notes():
  "ввод заметок, версия с сохранение в БД sqlite"
  go_input = 'Y'
  while go_input != 'N':
    note_name = input('Введите название заметки дневника: ')
    note_text = input('Введите текст заметки: ')
    go_input = input('Ввести еще одну заметку? Y/N: ').upper()
    dt = time.strftime("%d.%m.%Y г. %H:%M", time.localtime())
    try:
        add_notes(dt, note_name, note_text)
    except sqlite3.ProgrammingError:
        exit('Синтаксическая ошибка или нет базы')
    except sqlite3.OperationalError:
        exit('Системная ошибка, транзакция не может быть обработана')
    except Exception:
        exit('Что-то сломалось')

def return_all_notes():
    "чтение заметок из БД"
    try:
        print('*' * 40)
        print('Вот ваш дневник: ')
        print('*' * 40 + '\n')
        cursor.execute('SELECT * FROM pynotes')
        row = cursor.fetchone()
        while row is not None:
           print(row[0])
           print(row[1])
           print(row[2])
           print('-------------')
           row = cursor.fetchone()

    except sqlite3.ProgrammingError:
           exit('Синтаксическая ошибка или нет базы')
    except sqlite3.OperationalError:
        exit('Системная ошибка, транзакция не может быть обработана')
    except Exception:
        exit('Что-то сломалось')

def find_notes(search):
    "поиск заметок в БД"
    print('-------------')
    try:
        # Делаем выборку записей содержащих строку search и в цикле печатаем их значения
        cursor.execute("""SELECT * FROM pynotes WHERE note_name LIKE ('%' || ? || '%' )""", (search,))
        row = cursor.fetchone()
        while row is not None:
           print(row[0])
           print(row[1])
           print(row[2])
           print('-------------')
           row = cursor.fetchone()

    except sqlite3.ProgrammingError:
           exit('Синтаксическая ошибка или нет базы')
    except sqlite3.OperationalError:
        exit('Системная ошибка, транзакция не может быть обработана')
    except Exception:
        exit('Что-то сломалось')

def check_q(d):
    if d.lower() == 'q':
        exit(f'Работа завершена')
    elif not d.isdigit():
        exit(f'Нужно ввести число!')

def main():
    "основной блок программы"
    the_tag = input('Вы работаете с топорной программой ввода заметок, если решили выйти - введите Q, если нет - любую клавишу :) ').strip().lower()
    while(the_tag != 'q'):
        inp_check = (input('''Введите -
        1 чтобы добавить запись
        2 чтобы посмотреть записи
        3 чтобы произвести поиск по записям
        q чтобы выйти из программы: ''')).strip()

        check_q(inp_check)
        inp_check = int(inp_check)

        if inp_check == 1:
            input_notes()
        elif inp_check == 2:
            return_all_notes()
        elif inp_check == 3:
            print('*' * 20)
            search = input('''Введите заголовок или часть заголовка статьи которую ищем
    (регистр букв имеет значение): ''')
            find_notes(search)
            print('*' * 20)
        elif  inp_check == 'q':
            break
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

if __name__ == '__main__':
  main()