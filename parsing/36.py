from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/selenium/4/4.html"
options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    boxes = browser.find_elements(By.CLASS_NAME, value='check')
    for box in boxes:
        box.click()

    browser.find_element(By.CLASS_NAME, value='btn').click()
    result = browser.find_element(By.ID, value='result').text
    print(result)