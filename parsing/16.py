import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
lnk = 'https://parsinger.ru/html/'
pagen = [f"{lnk}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
link_in = []
for p in pagen:
    response = requests.get(url=p)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', class_='name_item'):
        link_in.append(f"{lnk}{link['href']}")
# print(link_in)
res = []
for url in link_in:
    # url = f'https://parsinger.ru/html/mouse/3/3_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    b = soup.find_all('p', class_='article')
    for name in b:
        res.append(int(name.text.replace('Артикул: ','')))
print(sum(res))