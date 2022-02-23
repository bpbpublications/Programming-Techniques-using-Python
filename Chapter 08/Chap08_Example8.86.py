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
    def myhoot(self):
        print("Hoot....Hoot..")

def myfunc(object):
    #Pythonic code: EAFP
    if hasattr(object, 'mytalk'):
        object.mytalk()
    elif hasattr(object, 'myhoot'):
        object.myhoot()

#M-1
myobj = Dog()
myfunc(myobj)
myobj1 = Crows()
myfunc(myobj1)
myobj2 = Duck()
myfunc(myobj2)
myobj3 = Owl()
myfunc(myobj3)

print("*"*25)

#M-2
myl1 = [Dog(),Crows(),Duck(),Owl()]
for object1 in myl1:
    myfunc(object1)