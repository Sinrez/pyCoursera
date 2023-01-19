from parsing.selenium import webdriver
from parsing.selenium import By

url = "https://parsinger.ru/methods/1/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    while True:
        browser.refresh()
        value = browser.find_element(By.ID, value='result').text

        try:
            value = int(value)
            break
        except ValueError:
            continue
print(value)