from threading import *
mylockobj = Lock()
print("Lock acquired by main thread")
mylockobj.acquire()
print("Lock again is trying to acquire by main thread")
mylockobj.acquire()
