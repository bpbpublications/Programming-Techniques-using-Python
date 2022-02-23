class Demo:
    def mymethod1(self):
        mynum1 = 10
        print("The local variable mynum1 value is", mynum1)

    def mymethod2(self):
        mynum2 = 120
        print(mynum1)
        print("The local variable mynum2 value is", mynum2)


myobj = Demo()
myobj.mymethod1()
myobj.mymethod2()
