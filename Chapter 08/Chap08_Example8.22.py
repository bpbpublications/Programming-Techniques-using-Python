class Student:
    def __init__(self):
        self.name = 'Sunita'
        self.age= 12
    
    def myhobby(self):
        self.hobby = 'dancing' # accessing instance variable
              
myobj1 = Student()
print("Before accessing instance variable from outside class")
myobj1.myhobby()
print(myobj1.__dict__)
myobj1.telephonenum = 9876543210
myobj1.myhobby()
print("After accessing instance variable from outside class")
print(myobj1.__dict__)