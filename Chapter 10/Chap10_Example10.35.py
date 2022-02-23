from threading import *
mylockobj = RLock()
print("Lock acquired by main thread")
mylockobj.acquire()# RL1
print(mylockobj)# RL2
print("Lock again is trying to acquire by main thread")
mylockobj.acquire()# RL3
print(mylockobj)# RL4
mylockobj.release()
mylockobj.release()
