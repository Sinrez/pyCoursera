import requests
lines = 0
with open ('dataset_3378_2.txt', 'r') as site:  # автоматом считываем ссылку из файла
    site = site.read()\
        .strip()
    filo = requests.get(site)
    for i in filo.text.splitlines():
        lines += 1
    print(lines)