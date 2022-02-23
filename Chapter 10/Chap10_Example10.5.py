from threading import *
class MyChildClass(Thread):
    def run(self):
        for i in range(1,9):
            print(f'{current_thread().getName()} is executing at count of {i}')
myt1=MyChildClass()
myt1.start()
for i in range(1,9):
    print(f'{current_thread().getName()} is executing at count of {i}')
