from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import os

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),options=op)
url = 'https://alfabank.ru/currency/'
driver.get(url)
sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
driver.close()
dollar_buy = float(values[0].text.strip().replace(' ₽', '').replace(',', '.'))
dollar_sell = float(values[1].text.strip().replace(' ₽', '').replace(',', '.'))
euro_buy = float(values[2].text.strip().replace(' ₽', '').replace(',', '.'))
euro_sell = float(values[3].text.strip().replace(' ₽', '').replace(',', '.'))
cny_buy = float(values[4].text.strip().replace(' ₽', '').replace(',', '.'))
cny_sell = float(values[5].text.strip().replace(' ₽', '').replace(',', '.'))
print(dollar_sell, dollar_buy)
print(euro_sell, euro_buy)
print(cny_sell, cny_buy)
# print(values)
