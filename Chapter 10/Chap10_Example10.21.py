from threading import *
def mymsgprint():
    print("Display function ")
mythreadobj = current_thread()
print("The main thread name is",mythreadobj.getName(), end = '')
if mythreadobj.daemon:
    print(" and is a daemon thread.")
else:
    print(" and is a non-daemon thread.")

mychildt1 = Thread(target = mymsgprint)
print("Child thread name is",mychildt1.getName(), end = '')
if mychildt1.daemon:
    print(" and is a daemon thread.")
else:
    print(" and is a non-daemon thread.")
mychildt1.start()
