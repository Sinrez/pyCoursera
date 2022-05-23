import sys
sys.path.append('modules/')
import requests, os, time
from checksql import checksql
import webbrowser

# Открываем файл, откуда будем брать URL, которые нужно проверить
f = open('data/urls.txt', 'r', encoding='UTF-8')
# Открываем файл, куда будем записывать найденные уязвимые URL
f2 = open('result/good.html', 'w', encoding='UTF-8')
code = '<h3>Уязвимые для SQL-иньекций URL адреса: </h3>'
f2.write(code)

# Функция для тестирования URL на уязвимость: подставляем одинарную кавычку в GET-параметры
def checkcheck(url):
    # Заменяем в URL значок & между параметрами, добавляя перед ним одинарную кавычку
    x = url.replace("&", "'&")
    # Очищаем URL от пробелов по обеим сторонам
    ur = x.strip()
    # Если вначале нет http, то добавляем его
    if not(ur[0:4] == 'http'):
        ur = 'http://' + ur
    print('Проверяю: ' + ur)
    try:
        # Получаем HTML-код по URL c подставленными кавычками
        s = requests.get(ur + "'")
        h = s.text
        # Проверяем на уязвимости
        a, b = checksql(h)
        if(a):
            print('Уязвим для SQL-инъекции: ' + ur)
            css = 'display: block; color: black; font-weight: bold; padding: 10px; margin: 10px; border-radius: 10px; background: YellowGreen;'
            code = '<a style="' + css + '" href="' + x + '" target="_blank">' + ur + '</a>'
            f2.write(code)
        else:
            print('Уязвимость не найдена: ' + ur)
    except:
        print('Ошибка при проверке: ' + ur)
        pass

    
# Последовательно пробуем URL из файла urls.txt
for site in f:
    checkcheck(site)
f.close()
f2.close()

webbrowser.open('file://' + os.path.realpath('result/good.html'))

