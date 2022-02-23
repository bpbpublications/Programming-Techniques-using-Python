class Student:
    def __init__(self):
        self.name = 'Mohan'
        self.age = 10
        self.country = 'India'
        self.contact = 9876543210
    
    def myshow(self):
        print("The name is: ", self.name)
        print("The age is: ", self.age)
        print("The country is: ", self.country)
        print("The contact number is: ", self.contact)

myobj1 = Student()
myobj2 = Student()
myobj1.name = 'Rohan'
myobj1.country = 'USA'
myobj1.myshow()
print("----------------")
myobj2.myshow()