class Demo:
    a1 = 1
    @staticmethod
    def mymethod1():
        Demo.d1 = 40
        del Demo.a1

print("Only static variable a1 is present")
print(Demo.__dict__)
print("---------------------------")
Demo.mymethod1()
print("static variable a1 is absent and only d1 is present")
print(Demo.__dict__)
