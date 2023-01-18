from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
url = 'https://alfabank.ru/currency/'
driver.get(url)
# sleep(0.6)

# try:
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     values = soup.find_all(class_='a2swtV x2swtV e23Qzr Q23Qzr')
#     euro_sell = values[4].text.strip()[:-2].replace(',', '.')
#     euro_buy = values[5].text.strip()[:-2].replace(',', '.')
# except:
#     sleep(1)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     values = soup.find_all(class_='a2swtV x2swtV e23Qzr Q23Qzr')
#     # euro_sell = values[4].text.strip()[:-2].replace(',', '.')
#     # euro_buy = values[5].text.strip()[:-2].replace(',', '.')
# sleep(0.2)
# button = driver.find_elements_by_xpath('/html/body/div[1]/div/div[5]/div/div/div/div/div[1]/div[1]/button[2]')[0]
# driver.execute_script('arguments[0].click();', button)
sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
driver.close()
dollar_sell = int(values[0].text.strip().replace(' ₽',''))
dollar_buy = int(values[1].text.strip().replace(' ₽',''))
# print()
# print()
# print(dollar_sell, dollar_buy)
print(values)