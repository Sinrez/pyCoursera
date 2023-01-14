from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/selenium/3/3.html"
result = 0
options = webdriver.ChromeOptions()
options.add_argument("--headless")
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    numbers = browser.find_elements(By.TAG_NAME, 'p')
    numbers = [number.text for i, number in enumerate(numbers) if i % 3 == 1]
    assert len(numbers) == 100, "Количество не равно 100"
    for number in numbers:
        result += int(number)

print(result)