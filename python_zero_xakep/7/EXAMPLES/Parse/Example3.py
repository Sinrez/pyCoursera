from myparse2 import parser

myparser = parser()

articles = myparser.getalltexts('https://habr.com/ru/', 'h2', 'tm-article-snippet__title', 'https://habr.com', start = 'Профиль         Обновить', end = 'Теги:')
for text in articles:
    print('----------------------------------')
    print(text)
    print('----------------------------------')
