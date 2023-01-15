from selenium import webdriver

with webdriver.Chrome() as webdriver:
    # webdriver.get('https://ya.ru/')
    webdriver.get('https:/mail.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение
