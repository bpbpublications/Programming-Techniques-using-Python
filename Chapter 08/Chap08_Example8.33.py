class Demo:
    a1 = 1
    def __init__(self):
        del Demo.a1

print("Before object creation static variable a1 is present")
print(Demo.__dict__)
print("---------------------------")
myobj = Demo()
print("After object creation static variable a1 is absent")
print(Demo.__dict__)
