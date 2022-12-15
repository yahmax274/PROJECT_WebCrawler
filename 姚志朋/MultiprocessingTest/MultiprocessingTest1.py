import multiprocessing as mp

# def task(a, b):
#   print('Task in the Process.')
#   print(a, b)

# if __name__=='__main__': # must put thread in the main
#   p1 = mp.Process(target=task, args=(1,2))
#   p1.start()
#   p1.join()
#####----------------#####
# def task(num):
#   print('This is Process: ', num)

# if __name__=='__main__':
#   num_process = 5
#   process_list = []
#   for i in range(num_process):
#     process_list.append(mp.Process(target = task, args = (i,)))
#     process_list[i].start()

#   for i in range(num_process):
#     process_list[i].join()
#####----------------#####
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
#####----------------#####
def job(x):
    return x*x

# def multicore():
#     pool = mp.Pool()
#     res = pool.map(job, range(10))
#     print(res)
    
# if __name__ == '__main__':
#     multicore()
#####----------------#####
def multicore():
    pool = mp.Pool(processes=3) # 定義CPU核數量為3
    res = pool.map(job, range(10))
    print(res)
# def multicore():
#     pool = mp.Pool() 
#     res = pool.map(job, range(10))
#     print(res)
#     res = pool.apply_async(job, (2,))
#     # 用get獲得結果
#     print(res.get())
#####----------------#####
# def multicore():
#     pool = mp.Pool() 
#     res = pool.map(job, range(10))
#     print(res)
#     res = pool.apply_async(job, (2,))
#     # 用get獲得結果
#     print(res.get())
#     # 迭代器，i=0時apply一次，i=1時apply一次等等
#     multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
#     # 從迭代器中取出
#     print([res.get() for res in multi_res])
if __name__ == '__main__':
    multicore()
