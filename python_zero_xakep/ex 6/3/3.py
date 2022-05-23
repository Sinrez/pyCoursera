from bs4 import BeautifulSoup
import requests 

url = 'https://habr.com/ru/'
baseurl = 'https://habr.com'
f = open('habrlog.txt', 'w', encoding='UTF-8')

# Функция которая получает URL адрес
# А возвращает набор ссылок с него
def getlinks(url):
    links = []
    href = requests.get(url).text 
    soup = BeautifulSoup(href, 'html.parser') 
    for link in soup.find_all('a'):
        l = link.get('href')
        if l != None:
            if not 'http' in l:
                links.append(baseurl + l)
    return links

# Список ссылок, пока содержит стартовый url
alllinks=[url]
z=0
# Мы будем бродить по сайту пока не спарсим 1000 или более ссылок
while len(alllinks) < 1000 and z < len(alllinks):
    links=getlinks(url)
    # Получаем ссылки с очередного url
    for x in links:
        # Если этой ссылки нет в нашем списке
        if not x in alllinks:
            # добавляем ссылку в список
            alllinks.append(x)
            print('Найдено: '+x)
            # Пишем в файл
            f.write(x+'\n')
    # Индекс следующего элемента списка
    z=z+1
    try:
        # Следующий url для парсинга
        url=alllinks[z]
        print('Проверяю: '+url)
    except:
        pass

print('--------------')
print('Сохранено: ', len(alllinks), ' ссылки')

f.close()
        
