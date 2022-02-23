class Student:
    def __init__(self):
        self.name = 'Mohan'
        self.age = 10
        self.country = 'India'
        self.contact = 9876543210

myobj1 = Student()
myobj2 = Student()
del myobj1.contact
print(myobj1.__dict__)
print(myobj2.__dict__)
