class Myfather:
    def __init__(self):
        print("I am a Father class constructor")
    def mydisplay_father(self):
        print("I am a Father class instance method")

class MySon(Myfather):
    def __init__(self):
        print("I am a Son class constructor")
    def mydisplay_son(self):
        print("I am a Son class instance method")

class MyGrandSon(MySon):
    def __init__(self):
        print("I am a Grand Son class constructor")
    def mydisplay_Grandson(self):
        print("I am a Grand Son class instance method")

myobj = MyGrandSon() # L1
myobj.mydisplay_Grandson() # L2
myobj.mydisplay_son() # L3
myobj.mydisplay_father() # L4