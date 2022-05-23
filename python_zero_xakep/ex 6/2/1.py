# Ищем вебсайты и веб-админки в указанном диапазоне IP
import sys
sys.path.append('modules/')
import requests
import ipranges
import webbrowser
import os

a = '37.151.22.1'
b = '37.151.22.25'

f = open('result/scanlog.html', 'w', encoding = 'UTF-8')
code = '<h3>Результаты сканирования IP диапазона: </h3>'
f.write(code)

for x in ipranges.rangeIPv4 (a, b):
    print('Проверяем: ' + str(x))
    try:
        s = requests.get("http://" + x, timeout=1)
        status = s.status_code
        # Статус 200 указывает что сервер ответил веб страничкой
        if status == 200:
            print("НАЙДЕНА ВЕБ_СТРАНИЦА: http://" + x)
            css = 'display: block; color: black; font-weight: bold; padding: 10px; margin: 10px; border-radius: 10px; background: YellowGreen;'
            code = '<a style="' + css + '" href="http://' + x + '" target="_blank">' + x + '</a>'
            f.write(code)
    except:
        pass
    
f.close()

webbrowser.open('file://' + os.path.realpath('result/scanlog.html'))
    
        
