class Employee:
    def __init__(self,myname, staffno, myage):
        self.myname = myname # instance variables
        self.staffno = staffno # instance variables
        self.myage = myage # instance variables
    
    #instance method
    def mydisplay(self):
        print("The name is: ", self.myname)
        print("The staff number is: ", self.staffno)
        print("The age is: ", self.myage)

class Demo:
    # static method: since there is no decorator 
		#and there is no self keyword. So not an instance method
    def myupdate(myemp):
        myemp.staffno += 10
        myemp.mydisplay()

myemp1 = Employee('Priyanka',600001, 28)
Demo.myupdate(myemp1) 
# passing en employee object to myupdate method