from bs4 import BeautifulSoup as soup
import requests

# Попробуем спарсить RSS ленту новостей
# В формате xml
z='https://news.mail.ru/rss/sport/'
s=requests.get(z).text
soup_page=soup(s,"xml")
news_list=soup_page.findAll("item")[:15]
for news in news_list:
    title = news.title.text
    description = news.description.text
    link = news.link.text
    print(title)
    print('---')
    print(description)
    print('---')
    print(link)
    print('_____________')
