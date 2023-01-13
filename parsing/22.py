import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
arr_of_values = [float(x.text) for x in soup.find_all('td')]
unique = list(set(arr_of_values))
print(sum(unique))