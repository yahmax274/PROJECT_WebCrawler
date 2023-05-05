#將檔案依檔名開頭分類
import os
import shutil

# 定義資料夾的名稱與路徑
folder_names = set()
directory = r"C:\Users\User\Desktop\氣象資料"

# 遍歷資料夾中的所有檔案
for filename in os.listdir(directory):
    # 取得檔案名稱的前6個字元，即資料夾的名稱
    folder_name = filename[:6]
    folder_names.add(folder_name)

    # 檢查資料夾是否存在，不存在就建立
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # 將檔案移動至對應的資料夾
    source_path = os.path.join(directory, filename)
    destination_path = os.path.join(folder_path, filename)
    shutil.move(source_path, destination_path)

# 印出資料夾名稱
print("資料夾名稱：", folder_names)