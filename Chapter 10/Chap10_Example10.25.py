from threading import *
from time import sleep


class Restaurant:
    def __init__(self, myobj):
        self.myobj = myobj

    def myOrder_serve_food(self):
        for i in range(5):
            print(self.myobj, i)
            sleep(1)


r1 = Restaurant("Take order from customer")
r2 = Restaurant("Serve order to customer")
myt1 = Thread(target=r1.myOrder_serve_food)
myt2 = Thread(target=r2.myOrder_serve_food)
myt1.start()
myt2.start()
