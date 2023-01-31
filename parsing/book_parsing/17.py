from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='drivers/chromedriver',options=chrome_options)
driver.get('https://github.com/')
driver.implicitly_wait(1)
print(driver.get_cookies())