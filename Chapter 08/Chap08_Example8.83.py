class Dog:
    def mytalk(self):
        print("Bark....Bark..")

class Crows:
    def mytalk(self):
        print("Caw....Caw..")

class Duck:
    def mytalk(self):
        print("Quack....Quack..")

class Owl:
    def mytalk(self):
        print("Hoot....Hoot..")

def myquack(object):
    #non-Pythonic code
    if isinstance(object,Duck):
        object.mytalk()
    else:
        print(type(object))
        print("The object must be duck to perform the talk")

myobj = Duck()
myquack(myobj)
myobj1 = Owl()
myquack(myobj1)