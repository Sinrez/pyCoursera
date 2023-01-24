from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import datetime as dt

def get_coureses(ind_buy, ind_sell):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),options=op)
    url = 'https://alfabank.ru/currency/'
    driver.get(url)
    sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    values = soup.find_all(class_='a2m0z y2m0z H2m0z eG2mw SG2mw')
    driver.close()
    buy_res = float(values[ind_buy].text.strip().replace(' ₽', '').replace(',', '.'))
    sale_res = float(values[ind_sell].text.strip().replace(' ₽', '').replace(',', '.'))
    spread = sale_res - buy_res
    now = str(dt.datetime.today()).split()[0]
    return buy_res, sale_res, spread, now

if __name__ == '__main__':
    print(get_coureses(0,1))   #usd
    print(get_coureses(2, 3))  # eur
    print(get_coureses(4, 5))  # cny