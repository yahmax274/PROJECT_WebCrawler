# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import requests 
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()
# time.sleep(2)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# reviews = soup.find_all('span', class_='section-review-text')
# if len(reviews) > 100:
#     break

# # 打印評論
# for review in reviews:
#     print(review.text)
###------######------###
import os
import re
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com.tw/maps/place/%E4%B8%81%E4%B8%81%E9%80%A3%E9%8E%96%E8%97%A5%E5%B1%80+%E6%B2%99%E9%B9%BF%E5%BA%97/@24.2549278,120.5733707,16z/data=!4m7!3m6!1s0x3469148ca2a276af:0xd51627921703a6d0!8m2!3d24.2537616!4d120.5675652!9m1!1b1?hl=zh-TW&authuser=0")
# 點擊查看所有評論
# 原本的 class name 中存在空格：'allxGeDnJMl__button allxGeDnJMl__button-text'，會讓程式抓不到
# 所以空格的部分要改成「.」才能成功抓取
review_click =driver.find_elements(By.CLASS_NAME,"allxGeDnJMl__button.allxGeDnJMl__button-text")
# 評論分頁下滑
# pane=driver.find_element(By.XPATH,"//*[@id="pane"]/div/div[1]/div/div/div[2]")
# driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 點擊返回店家頁面
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'geoUxComponentsAppbarButtonWrapper')))
BacktoStore_btn = driver.find_elements(By.CLASS_NAME,'geoUxComponentsAppbarButtonWrapper')[0]
BacktoStore_btn.click()

# 點擊返回搜尋結果
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'section-back-to-list-button.blue-link.noprint')))
back_btn = driver.find_elements(By.CLASS_NAME,'section-back-to-list-button.blue-link.noprint')[0]
back_btn.click()