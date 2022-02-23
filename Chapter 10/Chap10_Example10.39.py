from threading import Condition, Thread
from time import sleep
import random

mylist = []


def my_producer():
    mycond_obj.acquire()  # C1
    print("Items producing starts!!!!")  # C2
    for i in range(1, 6):
        myitem = random.randint(1, 80)
        mylist.append(myitem)  # C3
        print(f"Producer producing item no. {myitem}")  # C4
        sleep(1)
    print("Notification given to consumer")
    mycond_obj.notify()  # C5
    mycond_obj.release()  # C6


def my_consumer():
    mycond_obj.acquire()  # C7
    print("Waiting for update by the consumer")
    mycond_obj.wait()  # C8
    print("Notification received from producer and item is getting consumed")
    for itemnum in mylist:
        print(itemnum, end=' ')  # C9
    mycond_obj.release()  # C10
    print()


mycond_obj = Condition()
myt1 = Thread(target=my_consumer)
myt2 = Thread(target=my_producer)
myt1.start()
myt2.start()
myt1.join()
myt2.join()
print("Main Thread")
