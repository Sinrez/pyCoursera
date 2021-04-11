import html

import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl
import time as t

# url = 'https://banki.ru/insurance/responses/company/sberbankstrahovaniezhizni'
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text)
# article = soup.find('article')
#
#
# header = article.find('a', {'data-test': 'responses-header'}).text

ssl._create_default_https_context = ssl._create_unverified_context  # чтобы

base_url = 'https://banki.ru/'

companies = {
    'СБСЖ': {
        'pages': 50,
        'url': 'insurance/responses/company/sberbankstrahovaniezhizni/',
    },  # СБСЖ
    'СБС': {
        'pages': 16,
        'url': 'insurance/responses/company/sberbankstrahovanie/',
    },  # СБС
}

page_url = '?page='

df = pd.DataFrame(columns=[
    'Компания', 'url жалобы', 'Заголовок', 'Статус', 'Текст', 'Время', 'Оценка', 'Оценка выплат',
])

for company in companies.keys():
    print(company)

    company_url = companies[company]['url']
    r = requests.get(base_url + company_url)

    soup = BeautifulSoup(r, "html.parser")
    pages = companies[company]['pages']

    for page in range(2, pages + 2):
        t.sleep(2)

        for article in soup.findAll('article'):
            try:
                href = article.find('a', {'data-test': 'responses-header'}).get('href')
                header = article.find('a', {'data-test': 'responses-header'}).text
                text = article.find('div', {'itemprop': 'description'}).text.strip()
                time = article.find('time', {'data-test': 'responses-datetime', 'itemprop': 'dtreviewed'}).get(
                    'datetime')

                # optional
                try:
                    rating = article.find('span', {'data-test': 'responses-rating-grade'}).text.strip()
                except:
                    rating = None
                try:
                    rating_payouts = article.find('strong', {'class': 'font-size-medium'}).text.strip()
                except:
                    rating_payouts = None
                try:
                    rating_status = article.find('span', {'data-test': 'responses-status'}).text.strip()
                except:
                    rating_status = None

                row = [company, base_url + href[1:], header, rating_status, text, time, rating, rating_payouts]

                df.loc[len(df)] = row
            except:
                pass

        # Взятие следующей страницы
        try:
            if page <= pages:
                r = requests.get(base_url + company_url + page_url + str(page))
                soup = BeautifulSoup(r.text, features='lxml')
        except:
            pass

print(len(df))
df.to_excel('Отзывы_страхование.xlsx')