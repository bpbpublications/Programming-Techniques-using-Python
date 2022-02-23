#importing queue module
import queue

# creating queue object
myqueue_obj = queue.Queue()

# enqueueing data in Queue object
myqueue_obj.put('P')
myqueue_obj.put('Y')
myqueue_obj.put('T')
myqueue_obj.put('H')
myqueue_obj.put('O')
myqueue_obj.put('N')

# Queue values retrieving
for i in range(myqueue_obj.qsize()):
   print(myqueue_obj.get())
print("--------")
