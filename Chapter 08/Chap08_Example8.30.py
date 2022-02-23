class Demo:
    a1 = 1
    b1 = 2
    c1 = 3
    d1 = 4

    def __init__(self):
        print(self.a1)  # access SV inside constructor using self
        print(Demo.a1)  # access SV inside constructor using classname

    def mymethod1(self):
        print(self.b1)  # access SV inside instance method using self
        print(Demo.b1)  # access SV inside instance method using classname

    @classmethod
    def mymethod2(cls):
        print(cls.c1)  # access SV inside class method using cls
        print(Demo.c1)  # access SV inside class method using classname

    @staticmethod
    def mymethod3():
        print(Demo.d1)  # access SV inside static method using classname


myobj1 = Demo()
print("------------")
myobj1.mymethod1()
print("------------")
myobj1.mymethod2()
print("------------")
myobj1.mymethod3()
print("------------")
print(Demo.a1)  # access SV outside class using classname
print(myobj1.b1)  # access SV outside class using object reference
