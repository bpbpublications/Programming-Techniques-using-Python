class Employee:
    def __init__(shelf, name, age):
        shelf.name = name
        shelf.age = age
        print("Inside the constructor: "+ str(id(shelf)))

print(id(Employee('Priyanka',28)))
