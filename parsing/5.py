import requests as re

for i in range(1,162):
    request = re.get(url=f'http://parsinger.ru/img_download/img/ready/{i}.png')
    with open(str(i)+'image.jpeg', 'wb') as file:
        file.write(request.content)