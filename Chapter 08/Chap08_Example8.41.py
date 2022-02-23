a1 = 100


class Demo:
    a1 = 200

    def mymethod1(self):
        print(a1)
        print(self.a1)
        print(Demo.a1)


myobj = Demo()
myobj.mymethod1()
