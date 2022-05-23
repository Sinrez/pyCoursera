# Ищем наличие у сайта адресов похожих на админку
import requests
import webbrowser

f = open('data/admins.txt','r', encoding = 'UTF-8')
admins = f.read().split('\n')
f.close()

url = input('Введите домен сайта без https://')
for admin in admins:
    adminurl = 'https://'+url+"/"+admin
    status = requests.get(adminurl, timeout = 2).status_code
    if status == 200:
        print('Найдено что-то похожее на админку: ', adminurl)
        x = input('Открыть в браузере? Введите Y или N: ')
        if x.lower() == 'y':
            webbrowser.open(adminurl)
        break
else:
    print('Админка не найдена')
