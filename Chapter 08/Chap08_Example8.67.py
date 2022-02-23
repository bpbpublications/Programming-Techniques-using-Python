class Myfather(object):
    def __init__(self):
        super().__init__()
        print("I am a Father class constructor")
    def mydisplay_father(self):
        print("I am a Father class instance method")

class Mymother(object):
    def __init__(self):
        super().__init__()
        print("I am a Mother class constructor")
    def mydisplay_mother(self):
        print("I am a Mother class instance method")

class MyDaughter(Myfather,Mymother):
    def __init__(self):
        super().__init__() # calling parent class constructor.
        print("I am a Daughter class constructor")
    def mydisplay_Daughter(self):
        print("I am a Daughter class instance method")
        
myobj = MyDaughter()