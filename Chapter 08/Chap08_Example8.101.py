class Myemployee:
    def __init__(self,myname,myage):
        self.myname = myname
        self.myage = myage
myemp = Myemployee('Raj',34)
print(myemp.myname)
print(myemp.myage)
myemp.myname = 'Rohan'
print(myemp.myname)
