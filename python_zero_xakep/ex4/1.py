import sqlite3

# Указываем название файла базы данных
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()

try:
    # Создаем таблицу pyblog с двумя полями - title и article
    cursor.execute('''CREATE TABLE IF NOT EXISTS pyblog (title text, article text)''')
except:
    pass

def addarticle(title, text):
    # Вставляем в таблицу pyblog первую запись со значениями title и article
    mydata = (title, text)
    cursor.execute("INSERT INTO pyblog (title, article) VALUES (?, ?)", mydata)
    conn.commit()

def getallarticles():
    print('-------------')
    # Делаем выборку всех имеющихся в таблице записей и в цикле печатаем их значения
    cursor.execute('SELECT * FROM pyblog')
    row = cursor.fetchone()
    while row is not None:
       print(row[0])
       print(row[1])
       print('-------------')
       row = cursor.fetchone()

def findarticles(search):
    print('-------------')
    # Делаем выборку записей содержащих строку search и в цикле печатаем их значения
    cursor.execute("""SELECT * FROM pyblog WHERE title LIKE ('%' || ? || '%')""", (search,))
    row = cursor.fetchone()
    while row is not None:
       print(row[0])
       print(row[1])
       print('-------------')
       row = cursor.fetchone()

x = 0
while x != 4:
    x = int(input('''Введите -
    1 чтобы добавить запись
    2 чтобы посмотреть записи
    3 чтобы произвести поиск по записям
    4 чтобы выйти из программы: '''))
    if x == 1:
        title = input('Введите заголовок: ')
        text = input('Введите текст заметки: ')
        addarticle(title, text)
    elif x == 2:
        getallarticles()
    elif x == 3:
        search = input('''Введите заголовок или часть заголовка статьи которую ищем
(регистр букв имеет значение): ''')
        findarticles(search)
    elif x == 4:
        break
        

# Закрываем соединение с базой данных
cursor.close()
conn.close()
