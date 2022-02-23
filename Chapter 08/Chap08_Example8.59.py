import sys


class Demo:
    def __init__(self):
        print("Initializing the object")


myobj1 = Demo()
myobj2 = myobj1
myobj3 = myobj2
myobj4 = myobj3
print(sys.getrefcount(
    myobj1))  # If we pass any object reference, for that object there are total how many references are there
