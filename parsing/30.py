from parsing.selenium import webdriver
from parsing.selenium import By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button").click()