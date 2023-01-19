from parsing.selenium import webdriver
from parsing.selenium import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(link.text)