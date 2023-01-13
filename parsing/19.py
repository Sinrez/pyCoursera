from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/1/index.html')
soup = BeautifulSoup(response.text, 'html.parser')
data = [float(i.find('td').text) for i in soup.find_all('tr')[1:]]

print(sum(data))