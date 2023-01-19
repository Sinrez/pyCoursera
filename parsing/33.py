from parsing.selenium import webdriver
from parsing.selenium import By
import time

url = "https://parsinger.ru/selenium/1/1.html"
#1123581321345589144233377610987
input_values = ['Конь',
                'Петрович',
                'Лошадкин',
                '21',
                'Мск',
                'конь@yandex.ru',
                ]
with webdriver.Chrome() as browser:
    browser.get(url)
    inputs = browser.find_elements(By.CLASS_NAME, value='form')
    for form, value in zip(inputs, input_values):
        form.send_keys(value)
    browser.find_element(By.ID, 'btn').click()
    time.sleep(10)