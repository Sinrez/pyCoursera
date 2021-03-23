import os

with open('a.txt', 'w', encoding='utf-8') as g:
    g.write('Тестовый текст')

os.rename('a.txt', 'b.txt')
