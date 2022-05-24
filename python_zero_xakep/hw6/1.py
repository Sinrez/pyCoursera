# Задание попроще:
#
# Создайте парсер какого-нибудь популярного новостного сайта с
# сохранением напарсенных новостей в базу данных SQLITE3.
# Сделайте в базе поиск по ключевым словам заголовков новостей.
# Например - ввели "", напечатало нам все ранее напарсенные новости о .

import requests
import validators
from bs4 import BeautifulSoup


def check_url(url_ping):
    if 'http' not in url_ping[:5]:
        url_ping = 'http://'+ url_ping
    elif 'https' not in url_ping[:5]:
        url_ping = 'https://' + url_ping
    if not validators.url(url_ping):
        exit('Введен некорректный адрес web-ресурса, повторите попытку!')

# https://yandex.ru/news



if __name__ == '__main__':
    pass