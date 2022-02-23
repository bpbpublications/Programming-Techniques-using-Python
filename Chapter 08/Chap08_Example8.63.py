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

class MyGrandSon(MySon):
    def __init__(self):
        super().__init__()
        print("I am a Grand Son class constructor")
    def mydisplay_Grandson(self):
        print("I am a Grand Son class instance method")

myobj = MyGrandSon()
print('*'*25)
myobj.mydisplay_Grandson()
myobj.mydisplay_son()
myobj.mydisplay_father()