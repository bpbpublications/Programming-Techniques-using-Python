from threading import *
from time import sleep
mysemaphore_obj=Semaphore(2) # S0
print(mysemaphore_obj)  # S1
def runs():
    mysemaphore_obj.acquire()
    print("Acquired by " + current_thread().name + " and counter value is: " + str(mysemaphore_obj._value)) # S2
    for i in range(3):
        if i == 0:
            print(f"{current_thread().name} hits 6")
        elif i == 1:
            print(f"{current_thread().name} hits 4")
        else:
            print(f"{current_thread().name} is out")
        sleep(1)
    mysemaphore_obj.release()
    print("Released by " + current_thread().name + " and counter value is: " + str(mysemaphore_obj._value)) # S3

mythread1=Thread(target=runs,name ="Saurabh")
mythread2=Thread(target=runs,name="Divya")
mythread3=Thread(target=runs,name="Aditya")
mythread4=Thread(target=runs,name="Vineet")
mythread5=Thread(target=runs,name="Suman")
mythread1.start()
mythread2.start()
mythread3.start()
mythread4.start()
mythread5.start()
mythread1.join()
mythread2.join()
mythread3.join()
mythread4.join()
mythread5.join()
print("Main Thread completion")
