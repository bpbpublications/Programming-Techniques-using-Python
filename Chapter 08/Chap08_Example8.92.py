class Demo:
    def mymul(self,mynum1=None,mynum2=None,mynum3=None):
        if mynum1!=None and mynum2!= None and mynum3!= None:
            print(f'The Product of {mynum1},{mynum2} and {mynum3} are:',mynum1*mynum2*mynum3)
        elif mynum1!=None and mynum2!= None:
            print(f'The Product of {mynum1} and {mynum2}:',mynum1*mynum2)
        else:
            print(f'Please provide either 2 or 3 arguments')

myobj=Demo()
myobj.mymul(10,20,30)
myobj.mymul(10,20)
myobj.mymul(10)
