# Parent class 
class MyEngineer: 
     
     # making protected data members 
     _myname = None
     _myrollno = None
     _mybranch = None
     
     # a constructor 
     def __init__(self, myname, myrollno, mybranch):   
          self._myname = myname 
          self._myrollno = myrollno 
          self._mybranch = mybranch 
     
     def _mydisplay(self): 
  
          # accessing protected data members 
          print("The Roll No. is : ", self._myrollno) 
          print("The Branch is: ", self._mybranch) 

#child class
class Display(MyEngineer): 

       # a constructor 
       def __init__(self, myname, myrollno, mybranch):  
                MyEngineer.__init__(self, myname, myrollno, mybranch)  

       def mydisplayDetails(self): 

                 # accessing protected data members of Parent class  
                print("The name is: ", self._myname)  

                 # accessing protected member functions of Parent class  
                self._mydisplay() 

# creating objects of the child class         
myobj = Display("ABC", 620178, "ECE")  
myobj.mydisplayDetails() 