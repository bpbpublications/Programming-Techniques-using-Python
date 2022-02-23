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

Employee('Raj',24,600001, 'Engineer Trainee')
#displaying the attributes
print(Employee('Raj',24,600001, 'Engineer Trainee').name)
print(Employee('Raj',24,600001, 'Engineer Trainee').age)
print(Employee('Raj',24,600001, 'Engineer Trainee').staffnumber)
print(Employee('Raj',24,600001, 'Engineer Trainee').designation)

#displaying the method
Employee('Raj',24,600001, 'Engineer Trainee').display()

print("------------------------")
#displaying the attributes
print(Employee('Shyam',36,600002, 'Senior Manager').name)
print(Employee('Shyam',36,600002, 'Senior Manager').age)
print(Employee('Shyam',36,600002, 'Senior Manager').staffnumber)
print(Employee('Shyam',36,600002, 'Senior Manager').designation)

#displaying the method
Employee('Shyam',36,600002, 'Senior Manager').display()