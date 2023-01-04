import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    try:
        with open('sqlitescript.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()
    except FileNotFoundError as fer:
        print(f'Ошибка открытия файла {fer}')
    except Exception as ex0:
        print(f'Еще какая-то ошибка с файлом {ex0}')

    cursor.executescript(sql_script)
    print("Скрипт SQLite успешно выполнен")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")