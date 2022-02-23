class Student:
    def __init__(self):
        self.name = 'Mohan'
        self.age = 10
        self.country = 'India'
    
    def mydelete(self):
        del self.age

myobj1 = Student()
print("Before deleting: ")
print(myobj1.__dict__)
del myobj1.country # deleting outside of the class
print("After deleting outside of the class: ")
print(myobj1.__dict__)
print("After deleting from inside of the class")
myobj1.mydelete()
print(myobj1.__dict__)