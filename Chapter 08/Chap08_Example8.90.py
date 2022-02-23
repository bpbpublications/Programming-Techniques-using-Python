class Mycylinder:
    def __init__(self, myweight):
        self.myweight = myweight

    def __add__(self, other):
        return self.myweight + other.myweight


myobj1 = Mycylinder(9)
myobj2 = Mycylinder(14)
print(myobj1 + myobj2)
