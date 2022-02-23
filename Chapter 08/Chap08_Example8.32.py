class Demo:
    a1 = 1
    def __init__(self):
        self.b1 = 3
    
    def mymethod1(self):
        self.a1 = 2

myobj1=Demo()
myobj1.mymethod1()
print(Demo.a1)
print(myobj1.a1)
print("-------------")
myobj2=Demo()
myobj3=Demo()
print('myobj2:',myobj2.a1,myobj2.b1)
print('myobj3:',myobj3.a1,myobj3.b1)
myobj2.a1=8
myobj2.b1=9
print('myobj2:',myobj2.a1,myobj2.b1)
print('myobj3:',myobj3.a1,myobj3.b1)
print("-------------")
print(Demo.a1)