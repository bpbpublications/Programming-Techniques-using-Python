class Employee:
    def setName(self,myname): # Mutator method
        self.myname=myname
        
    def getName(self): # Accessor method
        return self.myname
    
    def setStaffNumber(self,StaffNumber): # Mutator method
        self.StaffNumber=StaffNumber
    
    def getStaffNumber(self): # Accessor method
        return self.StaffNumber

mynum=int(input('Enter number of employees:'))
for loop in range(mynum):
    myobj=Employee()
    
    myname=input('Enter the Name:')
    myobj.setName(myname)# calling mutator method
    
    mystaffnumber=int(input('Enter the Staff number:'))
    myobj.setStaffNumber(mystaffnumber)
		# calling mutator method
    
    print('Welcome!',myobj.getName())
		# calling accessor method
    print('Your Staff number is:',myobj.getStaffNumber())
		# calling accessor method
    print('*'*25)