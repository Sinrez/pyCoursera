import requests
import fake_useragent
# from fake_useragent import UserAgent
from bs4 import BeautifulSoup

storage_number = 1
link = f'https://www.banki.ru/services/responses/list/?rate[]=1&rate[]=2&is_countable=on&page='

responce = requests.get(f'{link}{storage_number}&isMobile=0').text
soup = BeautifulSoup(responce, "html.parser")
block = soup.find('div', id="responses-list-app")

# resp_bank =
resp_comment = block.findAll('div', class_="responses__item__message")



print(resp_comment)
# print(result_link)
