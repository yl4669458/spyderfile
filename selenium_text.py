from selenium import webdriver
from bs4 import BeautifulSoup
import time 

driver = webdriver.Chrome()
driver.get('https://xueersi.com')
driver.maximize_window()
xuersi_f_page = BeautifulSoup(driver.page_source, 'lxml')
time.sleep(2)
driver.get(xuersi_f_page.find('a', class_='link-btn')['href'])
time.sleep(10)
driver.quit()
