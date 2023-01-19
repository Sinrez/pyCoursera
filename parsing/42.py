from parsing.selenium import webdriver

res = 0
with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        if int(cookie['name'][cookie['name'].rfind('_')+1:]) % 2 == 0:
            res += int(cookie['value'])
print(res)