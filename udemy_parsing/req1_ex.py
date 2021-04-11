import requests

link = 'https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2'
resp = requests.get(link).text
print(resp)