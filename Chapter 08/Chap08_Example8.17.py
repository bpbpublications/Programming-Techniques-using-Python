class displayname:
    def __init__(self, myname):
        self.myname = myname

    def __call__(self):
        print(f"My name is: {self.myname}")


myobj = displayname('Ram')
myobj()
