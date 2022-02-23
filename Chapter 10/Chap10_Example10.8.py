from threading import *
def my_msgprint():
    print("Default name of child thread", current_thread().name)
    current_thread().name = 'NewChildThread'
    print("New name of child thread", current_thread().name)

myt1 = Thread(target = my_msgprint)
myt1.start()
print("Default name of Main thread", current_thread().name)
current_thread().name = 'NewMainThread'
print("New name of Main thread", current_thread().name)
