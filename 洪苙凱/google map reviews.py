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
input.send_keys("台北101") #輸入關鍵字
input.send_keys(Keys.ENTER)
time.sleep(5)
op1 = driver.find_element(By.CLASS_NAME,"hfpxzc").click()
time.sleep(5)
rew_bt = driver.find_element(By.XPATH,"//div[@role='button']").click()
time.sleep(5)
check = []
reviews = []
count = 0
reviews_set = 99999 #設定爬取筆數
while len(reviews) < reviews_set :#筆數為(n*10)+1
    review_win = driver.find_element(By.XPATH,"//*[@id='QA0Szd']/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",review_win)#捲動視窗到底
    time.sleep(2)
    try:  
        exp_bts = driver.find_elements(By.XPATH,"//button[@aria-label='顯示更多']")
        for exp_bt in exp_bts:
            driver.execute_script("arguments[0].click();", exp_bt)
    except:
        pass
    reviews = driver.find_elements(By.CLASS_NAME,"wiI7pd")
    check.append(len(reviews))
    print(check[-1])
    if len(check)>=2 and check[-1] == check[-2]:
        count = count+1
        if count == 20:
            break
    else:
        count = 0 
for review in reviews[:reviews_set]:
    reviews_list.append(review.text)
        
driver.quit()
#匯出檔案
import pandas as pd
raw_data = {"reviews": reviews_list}
df = pd.DataFrame(raw_data,columns=["reviews"])
df.to_csv("reviews.csv",encoding='utf-8-Sig',index=False)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"爬取 {len(reviews_list)} 筆評論，總共花費 {elapsed_time} 秒")