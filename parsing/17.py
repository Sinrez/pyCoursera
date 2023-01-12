import requests
from bs4 import BeautifulSoup

res = 0
count = []
price = []
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        # b = soup.find_all('span', {'id':{'in_stock','price'}})
        b_c = soup.find_all('span', {'id': {'in_stock'}})
        b_p = soup.find_all('span', {'id': {'price'}})
        # print(b_p)
        cn = int(str(b_p).replace('[<span id="price">', '').replace(' руб</span>]', ''))
        pr = int(str(b_c).replace('[<span id="in_stock">В наличии: ','').replace('</span>]','').replace('[<span id="in_stock" name="count">В наличии: ',''))
        res += cn * pr
print(res)
