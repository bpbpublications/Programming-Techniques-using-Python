from threading import *
def my_msgprint():
    print("The above line is executed by: ", current_thread().getName())

print("Main Thread creating child object")
mthread = Thread(target = my_msgprint) # L1
print("Main Thread starting child thread")
mthread.start()# L2
