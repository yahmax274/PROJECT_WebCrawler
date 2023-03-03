#步驟一，開google maps
#步驟二，輸入搜尋內容
#步驟三，抓取所有內文連結
#步驟四，以此連結抓取各別評論
#步驟五，匯出

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests 
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
###------######------###google搜尋
# driver.get("https://www.google.com.tw/?hl=zh_TW") 
# element.send_keys("國立自然科學博物館")
# element = driver.find_element(By.CLASS_NAME,"gLFyf")
# button = driver.find_element(By.CLASS_NAME,"gNO89b")
###------######------###
driver.get("https://www.google.com.tw/maps")
element = driver.find_element(By.ID,"searchboxinput")
element.send_keys("國立自然科學博物館")
time.sleep(1)
button=driver.find_element(By.ID,"searchbox-searchbutton")
button.click()
time.sleep(5)
##下拉到底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
href_list=[]
hrefs = driver.find_elements(By.CLASS_NAME,"hfpxzc")
for href in hrefs:
    href = href.get_attribute("href")
    href_list.append(href)
print(len(href_list))
# 關閉瀏覽器視窗
driver.close() 
for link in href_list:
    url = link
    driver.get(url)
