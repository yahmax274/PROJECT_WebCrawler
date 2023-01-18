# from macpath import split
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.common.by import By
import time 
import random
start = time.time() # 開始測量執行時間
driver = webdriver.Chrome()
driver.get("https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O1K5FBOqsvN&n=1")
time.sleep
# 外層內容
product_list =[]
products = driver.find_elements(By.CLASS_NAME,"product_Area")
for product in products:
    product = product.find_elements(By.CLASS_NAME,"box1")
    product_list.append(len(product))
dates = driver.find_elements(By.CLASS_NAME,'period')
date_list =[]
k=0
for i in dates:
    if i.find_element(By.TAG_NAME,'span') != None:
        date = i.find_element(By.TAG_NAME,'span').text
        date = date.split("~")
        year = datetime.now().strftime('%Y/')
        year = str(year)
        if date !=[""]:
            date = year + date[0]
            for j in range(product_list[k]):
                date_list.append(date)
            k = k+1
brands = driver.find_elements(By.ID,"gdsBrand_1")
brand_list = []
for i in brands:
    if i != None:
        brand= i.text
        if " 買1送1" in brand:
            brand = brand.replace(" 買1送1","")
        brand_list.append(brand)
brands2 = driver.find_elements(By.ID,"gdsName_1")
brand2_list = []
for i in brands2:
    if i != None:
        brand2 = i.text
        brand2_list.append(brand2)
discounts = driver.find_elements(By.ID,"discAmt_1")
discount_list =[]
for i in discounts:
    if i != None:
       discount = i.text
       discount_list.append(discount)
lasts = driver.find_elements(By.ID,"gdsStock_1")
last_list =[]
for i in lasts:
    if i != None:
       last = i.text
       if len(last)>3:
            last = last.replace(",","")      
    last = last+"組"
    last_list.append(last)
now_list =[]
now = datetime.now().strftime('%Y/%m/%d %H:%M')
now = str(now)
now_list =[now]*sum(product_list)
# 內文連結
link_list = []
links = driver.find_elements(By.ID,"gdsHref_1")
for link in links:
    if link != None:
        link = link.get_attribute("href")
        link_list.append(link)
driver.quit()
# 內層內容
type_list = []
price_list = []
for link in link_list:
    url = link
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    re = requests.get(url,headers=headers)
    soup = BeautifulSoup(re.text,"html.parser")
    #type
    types = soup.find_all("div",{"id":"bt_2_layout_NAV"})
    if types ==[]:
        type = "null|null|null|null"
        type_list.append(type)
    else:
        for type in types:
            type = type.text
            type = type.replace(" ","")
            type = type.split("\n")
            type = type[3:]
            if type == []:
                continue
            else:
                for i in range(4):  
                    if type[i] == "":
                        type[i] ="null"
                type = type[0]+"|"+type[1]+"|"+type[2]+"|"+type[3]
                #print(type)
                type_list.append(type)
    #price
    prices = soup.find_all("ul",class_ = "prdPrice")
    if prices ==[]:
        price = "null|null|null"
        price_list.append(price)
    else:
        for price in prices:
            price = price.text
            price = price.replace(" ","")
            price = price.split("\n")
            price = [i.strip() for i in price if i.strip()!=""]
            price_1 =""
            price_2 =""
            price_3 =""
            for i in range(len(price)):
                if price_1 =="null" or price_1 =="":
                    if "市售價" in price[i]:
                        price_1 = price[i]
                        price_1 = price_1[3:]
                        price_1 = price_1.replace("元","")   
                        price_1 = price_1.replace(",","")
                    else:
                        price_1 = "null"
                if price_2 =="null" or price_2 =="":
                    if "促銷價" in price[i]:
                        price_2 = price[i]
                        price_2 = price_2[3:]
                        price_2 = price_2.replace("元","")
                        price_2 = price_2.replace("賣貴通報","")
                        price_2 = price_2.replace("下單再折","")
                        price_2 = price_2.replace(",","")
                    else:
                        price_2 = "null"  
                if price_3 =="null" or price_3 =="":
                    if "折扣後價格" in price[i]:
                        price_3 = price[i]
                        price_3 = price_3[5:]
                        price_3 = price_3.replace("元賣貴通報","")
                        price_3 = price_3.replace(",","") 
                    else:
                        price_3 = "null"  
            price = price_1+"|"+price_2+"|"+price_3
            price_list.append(price)
#匯出csv檔
import pandas as pd
all_list = []
for i in range(len(brand2_list)):
    all = date_list[i]+"|"+brand2_list[i]+"|"+price_list[i]+"|"+discount_list[i]+"|"+last_list[i]+"|"+type_list[i]+"|"+brand_list[i]+"|"+now_list[i]
    all_list.append(all)
raw_data ={"rush_time|item_name|market_price|sale_price|discount_price|discount|stock|big|mid|small|category|brand|date": all_list}
df = pd.DataFrame(raw_data,columns=["rush_time|item_name|market_price|sale_price|discount_price|discount|stock|big|mid|small|category|brand|date"])
df.to_csv("momo.csv",encoding='utf-8-Sig',index=False)
end = time.time() # 結束測量執行時間
print("執行時間為 %f 秒" % (end - start))
