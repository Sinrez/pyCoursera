from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/2/2.html"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)