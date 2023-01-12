from urllib.request import urlopen
from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
html = urlopen('https://parsinger.ru/html/index1_page_1.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',{'src':'https://parsinger.ru/img/1/1.jpg'}))
# for b in bs.find(src = 'https://parsinger.ru/img/1/1.jpg').parent.children:
#     print(b)

# https://parsinger.ru/img/1/1.jpg
# print(bs)