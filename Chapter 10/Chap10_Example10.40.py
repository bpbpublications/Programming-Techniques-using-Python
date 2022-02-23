from threading import *
from queue import Queue
from time import sleep
import random


def myproducer():
    for i in range(5):
        item = random.randint(1, 100)
        print(f"Item No. {i} produced by producer is: ", item)
        myqueue_obj.put(item)
        print("Notification given by the producer")
        sleep(1)


def myconsumer():
    print("Waiting for updation by consumer")
    for i in range(5):
        sleep(1)
        print(f"The item no. {i} consumed by the consumer is: ", myqueue_obj.get())


myqueue_obj = Queue()
myt1 = Thread(target=myproducer)
myt2 = Thread(target=myconsumer)
myt1.start()
