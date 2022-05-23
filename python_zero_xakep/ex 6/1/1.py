import requests
import shutil
import os
import html2text
# https://pypi.org/project/html2text/

# Отправка запроса с Cookies
url = 'https://httpbin.org/cookies'
cookies = dict(mycookies='working')
r = requests.get(url, cookies=cookies)
print(r.text)
print('\n--------------------\n')

# Иногда в GET-запросе нужно передать какие-то параметры
# Создадим словарь с параметрами
dict1 = {'key1': 'value1', 'key2': 'value2'}
# Дадим GET запрос
s = requests.get('https://httpbin.org/get', params = dict1)
# Для наглядности распечатаем получившийся url
print(s.url)
print(s.text)
print('\n--------------------\n')

# POST запрос  с параметрами
dict1 = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data = dict1)
print(r.text)
print('\n--------------------\n')

# Отправка файла на сайт POST запросом
url = 'https://httpbin.org/post'
dict1 = {'key1': 'value1', 'key2': 'value2'}
files = {'file': open('data/test.txt', 'rb')}
r = requests.post(url, files=files, data=dict1)
print(r.text)
print('\n--------------------\n')

# Как скачать файл с сайта
s = 'https://xakep.ru/robots.txt'
# С помощью функции os.path.split(s) вытаскиваем из строки путь к файлу и его имя
dirname, filename = os.path.split(s)
# GET-запрос в режиме stream=True для скачивания файла
r = requests.get(s, stream=True)
# Если ответ сервера удачен (200)
if r.status_code == 200:
    # Создаем файл и открываем его в бинарном режиме для записи
    with open(filename, 'wb') as f:
    # Декодируем поток данных на основе заголовка content-encoding
        r.raw.decode_content = True
        # Копируем поток данных из интернета в файл с помощью модуля shutil
        shutil.copyfileobj(r.raw, f)
print('Скачали файл robots.txt')
print('\n--------------------\n')

# Получить текст страницы без тегов
html = requests.get('https://xakep.ru').text
d = html2text.HTML2Text()
d.ignore_links = True
txt = d.handle(html)
print(txt)
print('\n--------------------\n')

