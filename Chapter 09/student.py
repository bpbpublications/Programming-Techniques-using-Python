import pickle
class Student:
    def __init__(self,name,age,rollno,hometown):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.hometown=hometown
        
    def mydisplay(self):
        print(self.name,"\t",self.age,"\t",self.rollno,"\t",self.hometown)
