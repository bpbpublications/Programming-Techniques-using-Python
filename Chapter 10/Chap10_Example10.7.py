from threading import *
def my_msgprint():
    print("Default name of child thread", current_thread().getName())
    current_thread().setName('NewChildThread')
    print("New name of child thread", current_thread().getName())

myt1 = Thread(target = my_msgprint)
myt1.start()
print("Default name of Main thread", current_thread().getName())
current_thread().setName('NewMainThread')
print("New name of Main thread", current_thread().getName())
