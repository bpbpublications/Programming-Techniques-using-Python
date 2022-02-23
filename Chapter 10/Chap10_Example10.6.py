from threading import *
class MyClass():
    def my_msgprint(self):
        for i in range(1,7):
            print(f'{current_thread().getName()} is executing at count of {i}')

myobj1 = MyClass()
myt1 = Thread(target = myobj1.my_msgprint)
myt1.start()
for i in range(1,7):
    print(f'{current_thread().getName()} is executing at count of {i}')
