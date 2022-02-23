class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mydisplay(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")


myobj1 = Person('Saurabh', 32)
myobj2 = Person('Nilesh', 40)
myobj1.mydisplay()
myobj2.mydisplay()
