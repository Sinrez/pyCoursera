import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('tr')
acc = 0
for row in rows[1:]:
    orange = float(row.find('td', class_='orange').text)
    blue = float(row.find_all('td')[-1].text)
    acc += orange * blue
print(acc)