from threading import *
mysemaphore_obj = BoundedSemaphore(2)
mysemaphore_obj.acquire()
mysemaphore_obj.acquire()
mysemaphore_obj.release()
mysemaphore_obj.release()
mysemaphore_obj.release()
mysemaphore_obj.release()
