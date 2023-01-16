from selenium import webdriver
from selenium.webdriver.common.by import By
import time

head_url = "https://parsinger.ru/methods/5/index.html"
options = webdriver.ChromeOptions()
options.headless = True
path = "https://parsinger.ru/methods/5/"


def get_cookie(driver, url):
    driver.get(url)
    cookie = driver.get_cookies()[0]
    age = time.strftime('%Y-%m-%d', time.localtime(cookie['expiry']))
    return age, url


with webdriver.Chrome(options=options) as browser:
    browser.get(head_url)

    urls = browser.find_elements(By.CLASS_NAME, value='urls')
    urls = [url.find_element(By.TAG_NAME, value='a') for url in urls]
    urls = [url.get_attribute('href') for url in urls]

    cookies = []
    for url in urls:
        cookies.append(
            get_cookie(browser, url)
        )

    _, max_age_cookie_url = max(cookies, key=lambda x: x[0])
    browser.get(max_age_cookie_url)

    result = browser.find_element(By.ID, value='result').text
    print(result)