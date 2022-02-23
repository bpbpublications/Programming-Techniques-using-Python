class Employee:
    ''' This is an employee class '''
    def __init__(self,name,age,staffnumber,designation):
        self.name = name
        self.age = age
        self.staffnumber = staffnumber
        self.designation = designation
    
    def display(self):
        print(f"The name is: {self.name}")
        print(f"The age is: {self.age}")
        print(f"The staff number is: {self.staffnumber}")
        print(f"The designation is: {self.designation}")

myobj1 = Employee('Raj',24,600001, 'Engineer Trainee')
#displaying the attributes
print(myobj1.name)
print(myobj1.age)
print(myobj1.staffnumber)
print(myobj1.designation)

#displaying the method
myobj1.display()

myobj2 = Employee('Shyam',36,600002, 'Senior Manager')
print("------------------------")
#displaying the attributes
print(myobj2.name)
print(myobj2.age)
print(myobj2.staffnumber)
print(myobj2.designation)

#displaying the method
myobj2.display()

print(id(myobj1))
print(id(myobj2))