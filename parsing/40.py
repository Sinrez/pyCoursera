from pprint import pprint
from parsing.selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    pprint(cookies)