import requests as re

url1 = 'https://parsinger.ru/task/1'
for i in range(1,501):
    response = re.get(url=url1+'/'+str(i)+'.html')
    print(response.url)
    print(response.status_code )
    if response.status_code == 200:
        print(response.url)
        break
