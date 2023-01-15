

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/6/6.html"
number = ((12434107696 * 3) * 2) + 1
options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome() as browser:
    browser.get(url)

    values = browser.find_elements(By.TAG_NAME, value='option')
    for value in values:
        curr_num = int(value.text)
        if curr_num == number:
            value.click()
            break

    browser.find_element(By.ID, value='sendbutton').click()
    result = browser.find_element(By.ID, value='result').text
    print(result)