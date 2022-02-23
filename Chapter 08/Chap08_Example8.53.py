class Employee:
    def __init__(self,myname):
        self.myname = myname
        self.dt = self.Details()
    
    def mydisplay(self):
        print("The employee name is: ", self.myname)
        print('*'*25)
        self.dt.mydisplay1()
    
    class Details:
        def __init__(self):
            self.staffno = 600001
            self.mydepartment = 'ABC Department'
            self.myage = 32
        
        def mydisplay1(self):
            print('The staff number is {}'.format(self.staffno))
            print('The department is {}'.format(self.mydepartment))
            print('The age is {}'.format(self.myage))

#M-1
myobj=Employee('Saurabh') # L1
myobj.mydisplay() # L2
print('@'*25)
#M-2
myinner_obj=myobj.dt
print(type(myinner_obj)) # L3
myinner_obj.mydisplay1() # L4