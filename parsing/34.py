from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/3/3.html"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
result = 0
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    numbers = browser.find_elements(By.TAG_NAME, 'p')
    numbers = [number.text for number in numbers]
    for number in numbers:
        result += int(number)
print(result)