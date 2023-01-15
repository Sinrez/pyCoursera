from selenium import webdriver

res = 0
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        res += int(cookie['value'])
print(res)