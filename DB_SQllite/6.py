
import sqlite3

def progress(status, remaining, total):
    print(f'Скопировано {total-remaining} из {total}...')

try:
    sqlite_con = sqlite3.connect('sqlite_python.db')
    backup_con = sqlite3.connect('sqlite_backup.db')
    with backup_con:
        sqlite_con.backup(backup_con, pages=3, progress=progress)
    print("Резервное копирование выполнено успешно")
except sqlite3.Error as error:
    print("Ошибка при резервном копировании: ", error)
finally:
    if(backup_con):
        backup_con.close()
        sqlite_con.close()