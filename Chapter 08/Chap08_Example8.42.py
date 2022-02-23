a1 = 100


class Demo:
    a1 = 200

    def mymethod1(self):
        a1 = 300
        print(a1)


myobj = Demo()
myobj.mymethod1()
