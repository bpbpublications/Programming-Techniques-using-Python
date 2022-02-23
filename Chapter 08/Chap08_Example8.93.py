class Demo:
    def mymul(self,*vars):
        mytotal=1
        for loop in vars:
            mytotal *= loop
        print('The Product of arguments is :',mytotal)

myobj=Demo()
myobj.mymul(10,20,30)
myobj.mymul(10,20)
myobj.mymul(10)
myobj.mymul()
myobj.mymul(10,20,30,40)
