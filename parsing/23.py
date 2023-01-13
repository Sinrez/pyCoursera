import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find_all('tr')
headers = [x.text for x in rows[0].find_all('th')]
values = [0 for i in range(len(headers))]

for row in rows[1:]:
    heads = [float(x.text) for x in row.find_all('td')]
    for i in range(len(values)):
        values[i] += heads[i]
values = [round(x, 3) for x in values]
result = dict(zip(headers, values))
print(result)