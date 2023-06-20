from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
os.chdir(os.path.dirname(__file__))
reviews_list = []
driver = webdriver.Chrome()
url = "https://www.google.com.tw/maps/@25.0468863,121.5255809,15z?hl=zh-TW&authuser=0"
start_time = time.time()
driver.get(url)
input = driver.find_element(By.ID,"searchboxinput")
input.clear()
key_word = "台江國家公園"
input.send_keys(key_word) #輸入關鍵字
input.send_keys(Keys.ENTER)
time.sleep(5)
try:
    op1 = driver.find_element(By.CLASS_NAME,"hfpxzc").click()
    time.sleep(5)
except:
    pass
rew_bt = driver.find_element(By.XPATH,"//button[@aria-label='對「台江國家公園」的評論']").click()
time.sleep(2)
try:
    review_win = driver.find_element(By.XPATH,"//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]")
except:
    pass
for i in range(9999999999999999999):    
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",review_win)#捲動視窗到底
    time.sleep(1)
driver.quit()