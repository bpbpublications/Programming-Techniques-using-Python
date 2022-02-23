class Demo:
    a1 = 1
    @classmethod
    def mymethod1(cls):
        cls.c1 = 20
        del Demo.a1

print("Only static variable a1 is present")
print(Demo.__dict__)
print("---------------------------")
Demo.mymethod1()
print("static variable a1 is absent and only c1 is present")
print(Demo.__dict__)
