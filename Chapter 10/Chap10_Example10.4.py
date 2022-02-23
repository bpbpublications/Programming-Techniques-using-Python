from threading import *
def my_msgprint(i):
    for loop in range(1,i):
        print(f"{current_thread().getName()} thread running count is {loop}")

mthread = Thread(target = my_msgprint, name = 'MyChildThread', args = (5,))
mthread.start()

for i in range(1,5):
    print(f"Main thread running count is {i}")
