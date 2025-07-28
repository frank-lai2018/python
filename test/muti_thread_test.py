# 線程模塊  import threading
# 線程類Thread 參數:
# group：
#   用於指定線程所屬的線程組，在大多數常見應用場景中，通常不需要特別設置，預設值為 None。
# target：
#   表示執行緒要執行的目標任務，一般都是可呼叫物件（例如函數），執行緒啟動後會執行這個目標任務。
# args：
#   以元組的形式給予執行任務傳遞參數。例如，如果目標任務函數需要兩個參數，就可以將這兩個參數組成一個元組傳遞給 args。
# *args：
#   這裡的表述可能存在一定混淆，在 Thread 類別的參數定義中，通常使用 args 來傳遞位置參數（以元組形式），而 *args 這種寫法更多是在函數定義中用於接收任意數量的位置參數。在 Thread 類別的上下文裡，理解為可以透過 args 傳遞多個參數給目標任務函數。
# kwargs：
#   以字典的方式給予執行任務傳遞參數，適用於需要傳遞關鍵字參數給目標任務函數的情況。
# name：
#   用於為線程命名，方便在偵錯和日誌記錄等場景中識別不同的線程。


import threading
import time

# t1 = time.time()


# def worker(num):
#     """Thread run word"""
#     print(f'Thread {num} start')
#     time.sleep(2)  # 模擬耗時操作
#     print(f'Thread {num} end')


# # 創建
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()  # 啟動


# # 等待所有Thread完成
# for t in threads:
#     t.join()

# t2 = time.time()
# print("執行時間:", t2 - t1)

# print("所有Thread執行完畢")


# 1.2 资源竞争
a = 0
b = 100000
# 循环一次就给全局变量a+1


def add():
    for i in range(b):
        global a
        a += 1
    print("第一次:", a)


def add2():
    for i in range(b):
        global a
        a += 1
    print("第二次:", a)


# add()      # 第一次: 1000000
# add2()     # 第二次: 2000000
if __name__ == "__main__":
    first = threading.Thread(target=add)
    second = threading.Thread(target=add2)
    first.start()
    second.start()


# 2.線程同步
# 2.1兩種方式： join 與互斥鎖
# 2.2 互斥鎖
# 2.2.1 acquire() 加鎖
# 2.2.2 release() 解鎖
# 兩個方法必須成對出現，否則容易形成死鎖
# 死鎖: 一直等待對方釋放鎖的情景
# 死鎖會造成應用程式停止回應，不再處理其他任務

a = 0
b = 1000000
# 1.建立互斥鎖
lock = threading.Lock()
# 循環一次就給全域變數a+1


def add():
    lock.acquire()  # 上鎖
    for i in range(b):
        global a
        a += 1
        print("第一次:", a)
    lock.release()  # 解鎖


def add2():
    lock.acquire()  # 上鎖
    for i in range(b):
        global a
        a += 1
        print("第二次:", a)
    lock.release()  # 解鎖


# add() # 第一次: 1000000
# add2() # 第二次: 2000000
if __name__ == "__main__":
    first = threading.Thread(target=add)
    second = threading.Thread(target=add2)
    first.start()
    # first.join() # 等待第一個子執行緒執行完成以後，程式碼再繼續往下執行，開始執行第二個子執行緒
    second.start()
# 注意，互斥鎖是多個執行緒一起去搶，搶到鎖的執行緒先執行。
