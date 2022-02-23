#importing queue module
import queue

# creating Priority queue object
myqueue_obj = queue.PriorityQueue()
print(type(myqueue_obj))

# enqueueing some value in Priority Queue object
myqueue_obj.put((5,'P'))
myqueue_obj.put((3,'Y'))
myqueue_obj.put((1,'T'))
myqueue_obj.put((2,'H'))
myqueue_obj.put((4,'O'))
myqueue_obj.put((6,'N'))
print(myqueue_obj.qsize())

# Retrieving values 
for i in range(myqueue_obj.qsize()):
    print(myqueue_obj.get())
