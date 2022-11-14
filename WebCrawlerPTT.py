import csv
from math import fabs
import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
web= requests.get('https://www.ptt.cc/bbs/Gossiping/M.1663386448.A.F5A.html', cookies={'over18':'1'})
print(web.text)

#將原始碼做整理
soup = BeautifulSoup(web.text, 'html.parser')

#使用find_all()找尋特定目標
articles = soup.find_all('div', 'push')
print(articles)
# #寫入檔案中
# with open('Marugame.txt','w') as f:
#     for article in articles:
#         #去除掉冒號和左右的空白
#         messages = article.find('span','f3 push-content').getText().replace(':','').strip()
#         print(messages)
#         f.write(messages + "\n")

# #轉成csv

# df = pd . read_csv ( "Marugame.txt" ,encoding = 'ansi', delimiter = "\t" )
# df . to_csv ( "Marugame.csv"  ,encoding = 'ansi', index = False )