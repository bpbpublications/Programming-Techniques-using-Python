class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Inside the constructor: "+ str(id(self)))

print(id(Employee('Priyanka',28)))
