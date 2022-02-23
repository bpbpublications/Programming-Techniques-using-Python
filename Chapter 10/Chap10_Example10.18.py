from threading import Thread
daemonchk = False
def disp():
    if daemonchk:
        print('Display function only if it is daemon thread')
    else:
        print("Non-daemon thread")

threadobj = Thread(target = disp)
print("Before setting thread as daemon: ", threadobj.isDaemon())
if threadobj.isDaemon():
    daemonchk = True
threadobj.start()
threadobj.setDaemon(True)
