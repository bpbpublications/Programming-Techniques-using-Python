class Demo:
    a1=1 # declare SV within the class directly but 
		#from outside of any method
    def __init__(self):
        Demo.b1=2 
				# declare SV inside constructor by using class name
    def mym1(self):
        Demo.c1=3
				# declare SV inside instance method by using class name
        
    @classmethod
    def mym2(cls):
        cls.d1=4
				# declare SV inside classmethod by using cls variable
        Demo.d2=5
				# declare SV inside classmethod by using class name
    
    @staticmethod
    def mym3():
        Demo.e1=6
				# declare SV inside static method by using class name

print(Demo.__dict__)
print("----------------")
myobj=Demo()
print(Demo.__dict__)
print("----------------")
myobj.mym1()
print(Demo.__dict__)
print("----------------")
Demo.mym2()
print(Demo.__dict__)
print("----------------")
Demo.mym3()
print(Demo.__dict__)
print("----------------")
Demo.f1=60
# declare SV from outside of a class by using class name
print(Demo.__dict__) 