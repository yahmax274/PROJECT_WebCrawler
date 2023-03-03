import torch
import time
# 檢查系統上可用的 GPU 數量
print(torch.cuda.device_count(), "GPU(s) available")

# 列出每個 GPU 的名稱
for i in range(torch.cuda.device_count()):
    print("GPU", i, ":", torch.cuda.get_device_name(i))

# 獲取當前使用的 GPU 的 ID
print("Current device:", torch.cuda.current_device())

######################################################################

# 創建兩個 1000x1000 的隨機張量
x = torch.randn(1000, 1000)
y = torch.randn(1000, 1000)

# 設置 CPU 計算時間
start = time.time()
# 執行矩陣乘法
z = torch.matmul(x, y)
# 計算 CPU 計算時間
cpu_time = time.time() - start

# 檢查是否有可用的 GPU 來進行 PyTorch 的計算
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 設置 GPU 計算時間
start = time.time()
# 執行矩陣乘法，並將結果移到 GPU 上
x_gpu = x.to(device)
y_gpu = y.to(device)
z_gpu = torch.matmul(x_gpu, y_gpu)
# 將結果移到 CPU 上
z = z_gpu.cpu()
# 計算 GPU 計算時間
gpu_time = time.time() - start

# 輸出結果
print(f"CPU 計算時間: {cpu_time:.5f} 秒")
print(f"GPU 計算時間: {gpu_time:.5f} 秒")
print(f"GPU 加速倍數: {cpu_time / gpu_time:.2f}x")