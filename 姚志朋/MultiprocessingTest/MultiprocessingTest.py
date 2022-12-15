# import multiprocessing as mp

# def task(num):
#   print('This is cpu core: ', num)

# if __name__=='__main__':
#   cpu_count = mp.cpu_count()
#   print("cpu_count: ", cpu_count)
#   process_list = []
#   for i in range(cpu_count):
#     process_list.append(mp.Process(target = task, args = (i,)))
#     process_list[i].start()

#   for i in range(cpu_count):
#     process_list[i].join()
########--------########--------########--------########
# import threading
# import time
 
# def main(url, num):
#     print('開始執行', url)
#     time.sleep(2)
#     print('結束', num)
 
# url_list1 = ['www.yahoo.com.tw, www.google.com']
# url_list2 = ['www.yahoo.com.tw, www.google.com']
# url_list3 = ['www.yahoo.com.tw, www.google.com']
 
# # 定義線程
# t_list = []
 
# t1 = threading.Thread(target=main, args=(url_list1, 1))
# t_list.append(t1)
# t2 = threading.Thread(target=main, args=(url_list2, 2))
# t_list.append(t2)
# t3 = threading.Thread(target=main, args=(url_list3, 3))
# t_list.append(t3)
 
# # 開始工作
# for t in t_list:
#     t.start()
 
# # 調整多程順序
# for t in t_list:
#     t.join()
########--------########--------########--------########
# import multiprocessing as mp
# import time
 
 
# def main(url, num):
#     print('開始執行', url)
#     time.sleep(2)
#     print('結束', num)
 
 
# url_list1 = ['www.yahoo.com.tw, www.google.com']
# url_list2 = ['www.yahoo.com.tw, www.google.com']
# url_list3 = ['www.yahoo.com.tw, www.google.com']
 
# # 定義線程
# p_list = []
# p1 = mp.Process(target=main, args=(url_list1, 2))
# p_list.append(p1)
 
# p2 = mp.Process(target=main, args=(url_list2, 2))
# p_list.append(p2)
 
# p3 = mp.Process(target=main, args=(url_list3, 2))
# p_list.append(p3)
 

# if __name__ == '__main__':
#       # 開始工作
#   for p in p_list:
#       p.start()
  
#   # 調整多程順序
#   for p in p_list:
#       p.join()
########--------########--------########--------########
from bs4 import BeautifulSoup
import concurrent.futures
import requests
import time
 
 
def scrape(urls):
    response = requests.get(urls)
 
    soup = BeautifulSoup(response.content, "lxml")
 
    # 爬取文章標題
    titles = soup.find_all("h3", {"class": "post_title"})
 
    for title in titles:
        print(title.getText().strip())
 
    time.sleep(2)
 
 
base_url = "https://www.inside.com.tw/tag/AI"
urls = [f"{base_url}?page={page}" for page in range(1, 6)]  # 1~5頁的網址清單
 
start_time = time.time()  # 開始時間
print(urls)
# 同時建立及啟用10個執行緒
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scrape, urls)

end_time = time.time()
print(f"{end_time - start_time} 秒爬取 {len(urls)} 頁的文章")
