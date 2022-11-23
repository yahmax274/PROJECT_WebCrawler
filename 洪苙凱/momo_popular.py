# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:51:32 2022

@author: CYC_Lab
"""
import requests
import json
import pandas as pd
import re
import numpy as np
import time
import random
from bs4 import BeautifulSoup
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver import Chrome
import os 
import openpyxl
import xlwt
from tqdm import tqdm
from tqdm import trange
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

class popular():
    def __init__(self):
        self.url = 'https://www.momoshop.com.tw/main/Main.jsp'
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                'Content-Type': 'application/json'}
        self.resp = requests.get(url = self.url, headers = self.headers)
        self.resp.encoding = 'utf-8'
        self.html = BeautifulSoup(self.resp.text, 'html.parser')
        self.fixed_app = 'momo熱銷排行榜'

        self.today = datetime.datetime.now()
        self.fixed_DATA_DATE = str(self.today.year) + str(self.today.month) + str(self.today.day)

        self.pma = ['生活家電', '3C資訊', '生活用品', '保健樂活', '家居餐廚', '美妝保養', '流行精品', '團購美食', '戶外休閒', '電視購物', '暢銷書榜', '週期配送', '出清專區']

    def deal_href(self, href):
        url = 'https://www.momoshop.com.tw/' + href
        
        while 1:
            try:
                soup = requests.get(url = url, headers = self.headers)
                break
            except:
                print('before', url)
                url = href
                print('after', url)
                time.sleep(3)
                # raise Exception

        soup.encoding = 'utf-8'
        soup_html = BeautifulSoup(soup.text, 'html.parser')

        try:
            t = soup_html.find('a', class_ = 'webBrandLink').text # 品牌名稱
        except:
            t = 'null'

        sale_price = 'null'
        disc_price = 'null'
        disc2_price = 'null'
        try:
            price = soup_html.find_all('ul', class_ = 'prdPrice')[0].text
            price = price.replace('賣貴通報', '')
            price = price.split('\n')
            price.pop(0)
            price.pop(-1)

            for i in range(len(price)):
                try:
                    loc = price[i].index('市售價')
                    # for o in len(price):
                    sale_price = price[i][loc + 3 : -2]
                    sale_price= sale_price.replace(",","")
                    print(sale_price)
                except:
                    try:
                        loc = price[i].index('促銷價')
                        disc_price = price[i][loc + 3 :  -2]
                        disc_price= disc_price.replace(",","")
                        print(disc_price)
                    except:
                        try:
                            loc = price[i].index('折扣後價格')
                            disc2_price = price[i][loc + 5 : -2]
                            disc2_price= disc2_price.replace(",","")
                            print(disc2_price)
                        except:
                            pass
        except:
            pass

        return t, sale_price, disc_price, disc2_price

    def main(self):
        words = ['APP|pma|rank|item_brand|item_name|sale_price|disc_price|disc2_price|status|DATA_DATE']
        record = []

        app_list = []
        item_brand_list = []
        item_name_list = []
        sale_price_list = []
        disc_price_list = []
        disc2_price_list = []
        status_list = []


        for i in tqdm(range(2, 15)): # 總共13個類別
            for j in range(1, 8): # 總共7個排名
                item_name = self.html.find('p', id = 'bt_0_255_01_e' + '{}'.format(i) + '{}'.format(j) + '3').text
                disc_price = self.html.find('b', id = 'bt_0_255_01_p' + '{}'.format(i) + '{}'.format(j)).text
                
                if disc_price == '熱銷一空':
                    sale_price = self.html.find('b', id = 'bt_0_255_01_e' + '{}'.format(i) + '{}'.format(j) + '4').text
                    disc_price = 'null'
                    disc2_price = 'null'
                    item_brand = 'null'
                    status = '熱銷一空'
                else:
                    status = 'normal'
                    href = self.html.find('a', id = 'bt_0_255_01_e' + '{}'.format(i) + '{}'.format(j) + '1')['href']
                    item_brand, sale_price, disc_price, disc2_price = self.deal_href(href)
         
                # ------------------------------- 紀錄 -------------------------------
                app_list.append(str(self.fixed_app + '|' + str(self.pma[i-2]) + '|' + str(j)))
                item_brand_list.append(item_brand)
                item_name_list.append(item_name)
                sale_price_list.append(sale_price)
                disc_price_list.append(disc_price)
                disc2_price_list.append(disc2_price)
                status_list.append(status)
                break
            break
        
        date = [self.fixed_DATA_DATE for i in range(len(app_list))]
        final = list(zip(app_list, item_brand_list, item_name_list, sale_price_list, disc_price_list, disc2_price_list, status_list, date))
        for j in final:
            temp = "|".join(str(i) for i in j)
            record.append(temp)
            #record.append('111111111111111111111111111111111111111111111111111111,111111111111111111你好')
            #print(record)

        raw_data = {words[0]:record} 
        df_record = pd.DataFrame(raw_data,columns = words)
        df_record.to_csv('C:/Users/likai/Desktop/專題/Web Crawler/popular01.csv',encoding='utf-8-Sig', index = False)

if __name__ == '__main__':    
    test = popular()
    test.main()
__name__ == '__main__'
