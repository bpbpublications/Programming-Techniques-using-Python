class MyPassenger:
    def __init__(self,myname,myreservation):
        self.myname=myname # instance variable
        self.myreservation=myreservation # instance variable
        
    def mydisplay(self): # instance method
        print('Hi',self.myname)
				# accessing instance variable inside instance method
        print('Your reservation is: ',self.myreservation)
				# accessing instance variable inside instance method
        
    def myseat(self):
        if self.myreservation == 'IAC':
            print('Your seat is at first AC')
        elif self.myreservation == 'IIAC':
            print('Your seat is at second AC')
        elif self.myreservation == 'IIIAC':
            print('Your seat is at third AC')
        elif self.myreservation == 'S1' or self.myreservation == 'S2'or self.myreservation == 'S3' or self.myreservation == 'S4' or self.myreservation == 'S5' or self.myreservation == 'S6' or self.myreservation == 'S7' or self.myreservation == 'S8' or self.myreservation == 'S9' or self.myreservation == 'S10' :
            print('Your seat is at Sleeper')
        else:
            print('You entered the wrong seat abbreviation')
            
mynum=int(input('Enter number of Passengers:'))
count = 1
while count <=mynum:
    name=input('Enter Name:')
    reservation=input('Enter the Seat Abbreviation:')
    myobj= MyPassenger(name,reservation)
    myobj.mydisplay() 
		# instance method call without argument
    myobj.myseat() 
		# instance method call without argument
    print('@'*25) 
    count +=1