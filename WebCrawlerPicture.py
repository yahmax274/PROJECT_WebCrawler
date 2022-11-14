import requests
import re
from bs4 import BeautifulSoup
import json
import random
import time
# resp = requests.get('https://www.starbucks.com.tw/home/index.jspx?r=57')
resp = requests.get('https://www.netflix.com/tw/browse/genre/839338')

soup = BeautifulSoup(resp.text, 'html.parser')
test = open("WebCrawler/Picture/test.txt","w",encoding='UTF-8')
a=[]

delay_choices = [8, 5, 10, 6, 20, 11]  #延遲的秒數
delay = random.choice(delay_choices)

# 找出所有 .jpg 結尾的圖片
imgs = soup.find_all('img')
sel_jpg = soup.select("div.Post_content_NKEl9 div div div img.GalleryImage_image_3lGzO")
q=0
for img in imgs:
    if 'src' in img.attrs:
        if img['src'].endswith('.jpg'):
            q+=1
            a.append(img['src'])
            print("第",q,"張:",img["src"])
            test.write((img['src'])+"\n")
            pic=requests.get(img['src'])
            img2 = pic.content
            pic_out = open("WebCrawler/Picture/"+str(q)+".png",'wb')
            pic_out.write(img2)
            pic_out.close()
            time.sleep(delay)

# 利用 regex 找出所有 .jpg 結尾的圖片
for img in soup.find_all('img', {'src': re.compile('.jpg')}):
    q+=1
    a.append(img['src'])
    print("第",q,"張:",img["src"])
    test.write((img['src'])+"\n")
    pic=requests.get(img['src'])
    img2 = pic.content
    pic_out = open("WebCrawler/Picture/"+str(q)+".png",'wb')
    pic_out.write(img2)
    pic_out.close()
    time.sleep(delay)

test.close()