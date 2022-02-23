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
myl1 = enumerate()
# Both Main and all the child threads are active
for everythread in myl1:
    print("The thread name is: ",everythread.name, end= ' ')
    print("and its unique thread is is: ",everythread.ident)
    print()
sleep(5)
myl1 = enumerate()
# Only Main Thread is active
for everythread in myl1:
    print("After sleeping for 5 secs only : ",everythread.name, end= ' ')
    print("is an active thread and its unique thread is is: ",everythread.ident)
    print()
