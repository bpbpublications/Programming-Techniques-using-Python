class Student:
    def __init__(self):
        self.name = 'Sunita'
        self.age = 12

    def myhobby(self):
        self.hobby = 'dancing'  # accessing instance variable


myobj1 = Student()
print("Before calling hobby method")
print(myobj1.__dict__)
myobj1.myhobby()
print("After calling hobby method")
print(myobj1.__dict__)
