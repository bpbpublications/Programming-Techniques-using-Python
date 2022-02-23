class Student:
    def __init__(self):
        self.name = 'Chaya'
        self.age= 13
    
    def myshow(self):
        print(self.name) 
				# accessing instance variables within the class by using self
        print(self.age)
        
myobj1 = Student()
myobj1.myshow()
print(myobj1.name) 
# accessing instance variables outside of the 
#class by using object reference
print(myobj1.age)