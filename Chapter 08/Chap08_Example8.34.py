class Demo:
    a1 = 1
    def mymethod1(self):
        Demo.b1 = 10
        del Demo.a1

print("Before object creation static variable a1 is present")
print(Demo.__dict__)
print("---------------------------")
myobj = Demo()
myobj.mymethod1()
print("After object creation static variable a1 is absent and only b1 is present")
print(Demo.__dict__)
