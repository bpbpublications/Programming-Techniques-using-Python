class Human:
    def __init__(self,myname,myage):
        self.myname = myname
        self.myage = myage
    
    def mydisplay(self):
        print("The name is: ", self.myname)
        print("The age is: ", self.myage)

class Mystudent(Human):
    def __init__(self,myname,myage, mycity, myhobby):
        super().__init__(myname, myage)
        self.mycity = mycity
        self.myhobby = myhobby
    
    def mydisplay(self):
        super().mydisplay()
        print("The city is: ", self.mycity)
        print("The hobby is: ", self.myhobby)

class Myemployee(Human):
    def __init__(self,myname,myage, mystaffno, mycontactno):
        super().__init__(myname, myage)
        self.mystaffno = mystaffno
        self.mycontactno = mycontactno
    
    def mydisplay(self):
        super().mydisplay()
        print("The staff number is: ", self.mystaffno)
        print("The contact number is: ", self.mycontactno)

myst = Mystudent('Ram',16,'Hyderabad','Studying')
myemp = Myemployee('Surendra',54,60001,9406121337)
myst.mydisplay()
print("*"*25)
myemp.mydisplay()