from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='drivers/chromedriver',options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
pageSource = driver.page_source
bs = BeautifulSoup(pageSource, 'html.parser')
print(bs.find(id='content').get_text())
# print(driver.find_element_by_id('content').text)
# print(driver.find_element(By.NAME, "content"))

driver.close()
