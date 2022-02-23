class displayname:
    def __init__(self, myname):
        self.myname = myname

    def mydisplay(self):
        print(f"My name is: {self.myname}")


myobj = displayname('Ram')
myobj()
