import requests
import json
import os
os.chdir(os.path.dirname(__file__))
url_list = []
date_list = []
star_list = []
review_list = []
f = open("雞南山步道url.txt","r+")
for url in f.readlines():
    url = url.strip()
    url_list.append(url)


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
for url in url_list:
        text = requests.get(url,headers=headers).text
        pretext = ')]}\'' # 取代特殊字元
        text = text.replace(pretext,' ') # 把字串讀取成json
        soup = json.loads(text)
        for i in range(10):
            try:
                ymd = [""]
                ymd = soup[2][i][14][0][21][6][7][0:3]
                date = str(ymd[0])+"/"+str(ymd[1])+"/"+str(ymd[2])
                star = soup[2][i][4]
                review = soup[2][i][3]
                if review == None:
                    pass
                else:
                    date_list.append(date)
                    star_list.append(star)
                    review_list.append(review)
            except:
                pass


#匯出檔案
import pandas as pd
raw_data = {"日期": date_list,"星數":star_list,"評論":  review_list}
df = pd.DataFrame(raw_data,columns=["日期","星數","評論"])
df.to_csv( "雞南山步道_reviews.csv",encoding='utf-8-Sig',index=False)
