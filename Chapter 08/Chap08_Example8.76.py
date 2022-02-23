class A1:
    def __init__(self):
        print("I am A1 class constructor")
    def mymethod1(self):
        print("It is an instance method of A1 class")

class B1(A1):
    def __init__(self):
        print("I am B1 class constructor")
    def mymethod1(self):
        print("It is an instance method of B1 class")

class C1(B1):
    def mymethod1(self):
        print("It is an instance method of C1 class")

class D1(C1):
    def mymethod1(self):
        print("It is an instance method of D1 class")

class E1(D1):
    def mymethod1(self):
        A1.__init__(self)# calling A1 class constructor
        
myobj = E1() # L1
myobj.mymethod1() # L2