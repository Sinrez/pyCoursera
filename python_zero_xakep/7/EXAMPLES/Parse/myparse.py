from bs4 import BeautifulSoup
import requests

class parser:

    # Функция конструктор которая запускается при инициализации класса  
    def __init__(self):
        print('Модуль myparse подключен!')
        
    # Функция вернёт текст страницы без тегов
    def gettext(self, url, start = None, end = None):
        html = requests.get(url, timeout = 7).text
        html = html.replace('<br>', '\n\n')
        html = html.replace('<p>', '\n\n')
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        mas = text.split('\n')
        text = ''
        for s in mas:
            if s.strip() != '':
                text += s.strip() + '\n\n'
        if start != None and start in text:
            text = text.split(start)[1]
        if end != None and end in text:
            text = text.split(end)[0]
        return text

    # Функция возвращает словарь из заголовков и ссылок
    # В качестве аргумента принимает тег и класс контейнера в котором лежит ссылка
    def getlinks(self, url, tag, myclass, domain = ''):
        html = requests.get(url, timeout = 7).text
        soup = BeautifulSoup(html, 'html.parser')
        links = {}
        titles = soup.find_all(tag, class_=myclass)
        for x in titles:
            title = None
            link = None
            if tag != 'a':
                title = x.find('a').get_text()  
                link = x.a.get('href')  
            else:
                title = x.get_text()
                link = x.get('href')
            if title != None and link != None:
                links[title] = domain + link
        return links













    
            
