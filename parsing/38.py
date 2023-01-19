from parsing.selenium import webdriver
from parsing.selenium import By
import time

# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/6/6.html')
#     g = browser.find_element(By.TAG_NAME, 'option').text
#     print(g)

url = "http://parsinger.ru/selenium/7/7.html"
with webdriver.Chrome() as browser:
    browser.get(url)

    values = browser.find_elements(By.TAG_NAME, value='option')
    addition = sum(int(value.text) for value in values)

    browser.find_element(By.ID, value='input_result').send_keys(addition)

    browser.find_element(By.ID, value='sendbutton').click()
    time.sleep(5)