from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
div = str(soup.find_all('p', class_='price')).replace('<p class="price">','')\
    .replace('руб</p>,','').replace(' руб</p>','').replace('[','').replace(']','').split()
res = list(map(int, div))
print(sum(res))