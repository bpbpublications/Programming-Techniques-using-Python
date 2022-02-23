from threading import Thread
def disp():
    print('Display function')

threadobj = Thread(target = disp) # D0
print("Before setting thread as daemon: ", threadobj.isDaemon())# D1
threadobj.setDaemon(True)# D2
print("After setting thread as daemon: ", threadobj.isDaemon())# D3
