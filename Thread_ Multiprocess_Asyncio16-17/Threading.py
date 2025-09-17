import threading
import time


# def simple_worker(time_to_sleep):
#     print('before')
#     time.sleep(time_to_sleep)
#     print('after')

lock = threading.Lock()
count = 0


def lock_hogger(time_to_sleep=0.001):
    global count
    # lock.acquire()
    # print('Lock acquired!')
    time.sleep(time_to_sleep)
    print('after function')
    # lock.release()
    # print('Woke up, releasing lock')
    count += 1


t = [threading.Thread(target=lock_hogger) for i in range(1000)]
[i.start() for i in t]
[i.join() for i in t]
print(count)




