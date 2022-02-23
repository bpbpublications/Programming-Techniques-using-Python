class Demo:
    def __init__(self):  # taking only one argument
        print("I am a constructor")

    def method1(self):
        print("I am method 1")


myd1 = Demo()  # will be executing the constructor automatically at the time of object creation
Demo()  # will be executing the constructor automatically at the time of object creation
myd3 = Demo()  # will be executing the constructor automatically at the time of object creation
myd3.method1()  # will be executing the instance method
