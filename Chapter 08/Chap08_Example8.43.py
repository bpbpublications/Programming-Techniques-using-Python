class Demo:
    def mymethod1(self):
        global a1
        a1 = 300
        print(a1)

    def mymethod2(self):
        print(a1)


myobj = Demo()
myobj.mymethod1()
myobj.mymethod2()
