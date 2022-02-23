class Myfather:
    def __init__(self):
        print("I am a Father class constructor")
    def mydisplay_father(self):
        print("I am a Father class instance method")

class MySon(Myfather):
    def __init__(self):
        super().__init__()
        print("I am a Son class constructor")
    def mydisplay_son(self):
        print("I am a Son class instance method")

class MyDaughter(Myfather):
    def __init__(self):
        super().__init__()
        print("I am a Daughter class constructor")
    def mydisplay_Daughter(self):
        print("I am a Daughter class instance method")

myobj = MyDaughter()
print('*'*25)
myobj.mydisplay_Daughter()
myobj.mydisplay_father()
print('*'*25)
myobj1 = MySon()
print('*'*25)
myobj1.mydisplay_son()
myobj1.mydisplay_father()