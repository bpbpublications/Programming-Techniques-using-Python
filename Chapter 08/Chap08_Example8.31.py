class Demo:
    a1 = 1
    def __init__(self):
        Demo.a1=2 # modifying SV using class name

    @classmethod
    def mymethod1(cls):
        cls.a1=4 # modifying SV using cls variable

    @classmethod
    def mymethod2(cls):
        Demo.a1=5 # modifying SV using class name

    @staticmethod
    def mymethod3():
        Demo.a1=6 # modifying SV using class name

myobj=Demo()
print(Demo.a1)
print(myobj.a1)
print("----------------")
myobj.mymethod1()
print(Demo.a1)
print(myobj.a1)
print("----------------")
myobj.mymethod2()
print(Demo.a1)
print(myobj.a1)
print("----------------")
myobj.mymethod3()
print(Demo.a1)
print(myobj.a1)
print("----------------")
Demo.a1=7 # modifying SV outside the class using class name
print(Demo.a1)
print(myobj.a1)