from bs4 import BeautifulSoup
import requests 

# Даем get запрос и получаем в переменную html код веб страницы
html = requests.get(r'https://habr.com/ru/').text
# Создаём объект bs4
soup = BeautifulSoup(html, 'html.parser') 
# Ищем все теги определенного типа и класса
# .find_all находит все элементы по их идентификатору
# в данном случае все теги h2 с классом 'tm-article-snippet__title'
news = soup.find_all('h2', class_='tm-article-snippet__title') 
for x in news:  # Проходим по всем полученным заголовкам
    # .find найдет первый встречающийся элемент
    # в данном случае это тег ссылки 'a'
    # .get_text() выдаст нам текст элемента
    title = x.find('a').get_text()  # В заголовке находим все ссылки и получаем их текст
    link = x.a.get('href')  # А теперь получаем сами ссылки
    print(title)
    print('https://habr.com'+link)
    print('__________')
