from threading import *
from time import sleep
def display(num1,num2):
    print(f"{current_thread().name} thread started")
    sleep(1)
    mul = num1 * num2
    print(f"{current_thread().name} executing display function with value {mul}")

myt1 = Thread(target = display, name= "MyChildThread1",args = (10,20))
myt2 = Thread(target = display, name= "MyChildThread2",args = (30,40))
myt3 = Thread(target = display, name= "MyChildThread3",args = (50,60))
print("The total number of active threads before child thread start are: ", active_count())
myt1.start()
myt2.start()
myt3.start()
print("The total number of active threads after child thread start are: ", active_count())
sleep(4)
print("Now, the total number of active threads are: ", active_count())
