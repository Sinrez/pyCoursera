import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/table/3/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
arr_of_values = [float(x.text) for x in soup.find_all('b')]
print(sum(arr_of_values))