import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = browser.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)