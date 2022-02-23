#importing queue module
import queue

# creating queue object
myqueue_obj = queue.LifoQueue()

# enqueueing some value in Queue object
myqueue_obj.put('P')
myqueue_obj.put('Y')
myqueue_obj.put('T')
myqueue_obj.put('H')
myqueue_obj.put('O')
myqueue_obj.put('N')

# Queue values retrieving
while not myqueue_obj.empty():
   print(myqueue_obj.get())
