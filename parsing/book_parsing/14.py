# page has been fully loaded:
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='drivers/chromedriver',options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
       element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
finally:
        # print(driver.find_element_by_id('content').text)
        pageSource = driver.page_source
        bs = BeautifulSoup(pageSource, 'html.parser')
        print(bs.find(id='content').get_text())
        driver.close()