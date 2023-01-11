from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
shema = 'http://parsinger.ru/html/'
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

print(pagen)