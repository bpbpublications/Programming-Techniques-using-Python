class Employee:
    companyname = 'ABC' # class variable
    def __init__(self, myname, staffno):
        self.myname = myname
        self.staffno = staffno

myobj1 = Employee('Ram',60001)
myobj2 = Employee('Shyam',60002)
print(myobj1.myname, myobj1.staffno, Employee.companyname)
print(myobj2.myname, myobj2.staffno, Employee.companyname)
