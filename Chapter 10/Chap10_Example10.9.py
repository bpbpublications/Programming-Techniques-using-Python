import time
from threading import *


class my_class_poori():
    def my_func_poori(self):
        self.heat_oil()
        self.make_dough()
        self.make_slices()
        self.fry()
        self.delicious_poori()

    def heat_oil(self):
        print("Heating the oil")
        time.sleep(1)

    def make_dough(self):
        print("Making the dough")
        time.sleep(1)

    def make_slices(self):
        print("Making the slices")
        time.sleep(1)

    def fry(self):
        print("Frying process started")
        time.sleep(1)

    def delicious_poori(self):
        print("Delicious poori is ready to eat!")
        time.sleep(1)


myobj = my_class_poori()
mythread_obj = Thread(target=myobj.my_func_poori)
mythread_obj.start()
