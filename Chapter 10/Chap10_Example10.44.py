from threading import *
from time import sleep
def mygreeting():
    obj_lock.acquire()
    try:
        for i in range(2):
            print(f"Hello! {current_thread().getName()}, {i} time")
            sleep(1)
    finally:
        obj_lock.release()

obj_lock = Lock()
myt1 = Thread(target = mygreeting, name ='Chikki')
myt2 = Thread(target = mygreeting, name ='Ankit')
myt3 = Thread(target = mygreeting, name ='Ashwin')
myt1.start()
myt2.start()
myt3.start()
myt1.join()
myt2.join()
myt3.join()
print("Main Thread Completed")
