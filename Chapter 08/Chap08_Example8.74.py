class A1:
    def mymethod1(self):
        print("It is an instance method of A1 class")

class B1(A1):
    def mymethod1(self):
        print("It is an instance method of B1 class")

class C1(B1):
    def mymethod1(self):
        print("It is an instance method of C1 class")

class D1(C1):
    pass

class E1(D1):
    def mymethod1(self):
        super().mymethod1()

myobj = E1()
myobj.mymethod1()