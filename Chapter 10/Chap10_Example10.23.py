from threading import *
from time import sleep
def mymsgprint():
    for i in range(1,11):
        print(f"Taking order from Table {i} and service completed for Table {i}")
        sleep(1)

mychildt1 = Thread(target = mymsgprint)
mychildt1.start()
sleep(7)
print("Restaurant Closed !")
