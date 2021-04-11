import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

user = UserAgent().data_browsers['chrome'][0]

header = {'User-Agent': user, 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

# print(header)

link = "https://browser-info.ru/"
responce = requests.get(link, headers = header).text
# soup = BeautifulSoup(responce, features="xml")

soup = BeautifulSoup(responce, "html.parser")
block = soup.find('div', id="tool_padding")

#check_js
check_js = block.find('div', id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

#check_flash
check_flash = block.find('div', id="flash_version")
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

#check user_agent
user_agent = block.find('div', id="user_agent").text
us_agent= f'user_agent: {user_agent}'

print(us_agent)
print(result_js)
print(result_flash)
