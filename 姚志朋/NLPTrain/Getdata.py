#隨機獲取200筆留言
import os
import glob
import random

# 設定隨機抓取資料數
data_number = 100

# 設定路徑
neg_reviews_path = r'C:\Users\User\Desktop\專題程式\NLPLab-master\Crawler\CrawlerToBooking\negativeReviews'
pos_reviews_path = r'C:\Users\User\Desktop\專題程式\NLPLab-master\Crawler\CrawlerToBooking\positiveReviews'

# 讀取負面評論
neg_lines = []
txt_files = [os.path.join(neg_reviews_path, f) for f in os.listdir(neg_reviews_path) if f.endswith('.txt')]
random_files = random.sample(txt_files, data_number)
for file_path in random_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read() 
        file_content = file_content.strip()
        neg_lines.append(file_content)

# 讀取正面評論
pos_lines = []
txt_files = [os.path.join(pos_reviews_path, f) for f in os.listdir(pos_reviews_path) if f.endswith('.txt')]
random_files = random.sample(txt_files, data_number)
for file_path in random_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read() 
        file_content = file_content.strip()
        pos_lines.append(file_content)

# 初始化 train_rows 列表
train_rows = []

# 迭代每一行
for line in pos_lines:
    # 去除空格和換行符號
    line = line.strip()

    # 初始化 label 列表
    label = [1, 0, 0]

    # 添加到 train_rows 列表中
    train_rows.append([label, line])

for line in neg_lines:
    # 去除空格和換行符號
    line = line.strip()

    # 初始化 label 列表
    label = [0, 0, 1]

    # 添加到 train_rows 列表中
    train_rows.append([label, line])

# print(train_rows)