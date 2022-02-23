from threading import Thread, Event
from time import sleep


def func1():
    sleep(2)  # Initially sleep for 2 secs
    myeventobj.set()  # E2
    print("func1 sleeping for 3 secs....")
    sleep(3)  # E3
    myeventobj.clear()  # E4


def func2():
    print("Initially myeventobj is: ", myeventobj.isSet())  # E1
    myeventobj.wait()
    if myeventobj.isSet():  # E5
        print("True when myeventobj.set() is called from func1 .i.e. Internal flag is set")
    print("func2 sleeping for 4 secs....")
    sleep(4)  # E6
    if myeventobj.isSet() == False:  # E7
        print("False when myeventobj.clear() is called from func1.i.e. Internal flag is reset")


myeventobj = Event()
myt1 = Thread(target=func1)
myt2 = Thread(target=func2)
myt1.start()
myt2.start()
myt1.join()
myt2.join()
print("Main Thread Completed")
