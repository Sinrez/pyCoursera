import requests
import bs4
import re

f = open('result/jokes.html', 'w', encoding = 'UTF-8')
# Парсим одну и ту же страницу три раза
for _ in range(3):
    s = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(s.text, "html.parser")
    # Получаем список анекдотов по CSS классу
    txt = soup.select('.anekdot_text')
    # Проходим списком по спарсенным элементам
    for x in txt:
        # Печатаем текст тегов
        print('---')
        # Оставляем в тексте только символы указанные в регулярном выражении
        reg = re.compile('[^0-9a-zA-Zа-яА-Я .:,!-—()_ ЁёьЬъЪ\n\r\t]')
        s = reg.sub('', x.text.strip())
        print(s)
        joke = '<div style="margin: 10px; padding: 10px; border-radius: 10px; background: Moccasin;">' + s + '</div>'
        f.write(joke)
f.close()


