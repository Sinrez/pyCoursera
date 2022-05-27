from myparse import parser

myparser = parser()

print(myparser.getlinks('https://habr.com/ru/', 'h2', 'tm-article-snippet__title', 'https://habr.com'))
