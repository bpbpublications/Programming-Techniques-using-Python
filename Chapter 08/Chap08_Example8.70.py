class Mymother(object):
    def __init__(self):
        self.num1 = 10
        print("I am a Mother class constructor")
    def mydisplay_mother(self):
        print("I am a Mother class instance method")

class MyDaughter(Mymother):
    def mydisplay_Daughter(self):
        print("I am a Daughter class instance method")
        
myobj = MyDaughter()
print(myobj.num1)
myobj.mydisplay_Daughter()
myobj.mydisplay_mother()