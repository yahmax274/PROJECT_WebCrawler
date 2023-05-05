##讀取檔案並匯出成csv
import os
import glob
import csv
from datetime import datetime

##檔案路徑
data_path= r'C:\Users\User\Desktop\專題程式\CWD\氣象資料\466880'

##匯出檔名
output_filename = 'output.csv'
#判斷檔案是否存在
if os.path.exists(output_filename):
    os.remove(output_filename)
with open(output_filename, 'a', newline='', encoding='big5') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(["日期", "累積雨量", "最高溫", "最低溫","天氣狀態"])
#篩選指定時間
date_string = "2020-01-01T23:50:00+08:00"
dt = datetime.fromisoformat(date_string)
selected_time = dt.time()

data=[]
txt_files = glob.glob(os.path.join(data_path, '*.txt'))
for txt_file in txt_files:
    with open(txt_file,mode='r', encoding='big5') as f:
        reader = csv.reader(f, delimiter=',')
        with open(output_filename, 'a', newline='', encoding='big5') as out_file:
            writer = csv.writer(out_file, delimiter=',')
            for row in reader:
                date_string = row[4]
                dt = datetime.fromisoformat(date_string)
                date_part = dt.date()
                time_part = dt.time()
                if time_part == selected_time:
                    row_data = [date_part]
                    for val in [float(row[11]),float(row[19]),float(row[21])]: 
                        if val <-80:
                            row_data.append('N/A')
                        else:
                            row_data.append(val)
                    if row[25]!="-99":
                        row_data.append(row[25])
                    else:
                        row_data.append('N/A')
                    writer.writerow(row_data)
# 11日累積雨量，單位 公釐
# 19本日最高溫，單位 攝氏
# 21本日最低溫，單位 攝氏
print("Finish")
