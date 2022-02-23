def mychk_name(method):
    def inner(refname):
        if refname.myname == 'Saurabh':
            print("Hey! I am Saurabh")
        else:
            method(refname)
    return inner

class displayname:
    def __init__(self,myname):
        self.myname = myname
    
    @mychk_name
    def mydisplay(self):
        print(f"My name is: {self.myname}")

myusername = input("Enter the name: ")
myobj = displayname(myusername)
myobj.mydisplay()