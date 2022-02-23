from threading import *
mythreadobj = current_thread()
print(mythreadobj.getName()) # L1
print(mythreadobj.isDaemon()) # L2
print(mythreadobj.daemon) # L3
