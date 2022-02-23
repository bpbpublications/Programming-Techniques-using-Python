from threading import *


def mymsgprint():
    mychildthread2 = Thread(target=disp2)  # DL2
    print("Second Child thread name is", mychildthread2.getName(), end='')
    if mychildthread2.daemon:
        print(" and is a daemon thread and it's parent name is", mychildt1.getName())
    else:
        print(" and is a non-daemon thread and its parent name is", mychildt1.getName())
    mychildthread2.start()


def disp2():
    print("Display2 function")


mythreadobj = current_thread()
print("The main thread name is", mythreadobj.getName(), end='')
if mythreadobj.daemon:
    print(" and is a daemon thread.")
else:
    print(" and is a non-daemon thread.")

mychildt1 = Thread(target=mymsgprint)
mychildt1.daemon = True  # DL1
print("Child thread name is", mychildt1.getName(), end='')
if mychildt1.daemon:
    print(" and is a daemon thread.")
else:
    print(" and is a non-daemon thread.")
mychildt1.start()
mychildt1.join()  # to make main thread idle and wait for child threads to complete.
print("Main Thread Completed!")
