from threading import *

def displaymsg():
    print("Child Thread")

myt1 = Thread(target = displaymsg)
myt1.start()
print(f"{current_thread().getName()} unique id is: {current_thread().ident}" )
print(f"{myt1.getName()} unique id is: {myt1.ident}" )
