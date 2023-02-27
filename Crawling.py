#동영상 url 추출 
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

chrome_options = webdriver.ChromeOptions()
URL = 'https://www.youtube.com/results?search_query=%ED%99%94%EC%9E%AC'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)
time.sleep(3)

for i in range(0, 5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

titles = driver.find_elements(By.CSS_SELECTOR, '#video-title')
print(titles)


wb = Workbook()
ws = wb.create_sheet('화재영상')
wb.remove_sheet(wb['Sheet'])

for title in titles:
    print(title.get_attribute('href'))
    ws.append([title.get_attribute('href')])

wb.save('D:\화재영상\화재영상url.xlsx')
wb.close()