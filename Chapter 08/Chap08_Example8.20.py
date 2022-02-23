class Student:
    def __init__(self):
        self.name = 'Sunita'
        self.age= 12
        self.hobby = 'dancing'
myobj1 = Student()
print(myobj1.__dict__) # the above object will contain all the attributes defined for object itself where attribute name will be mapped to its value.
