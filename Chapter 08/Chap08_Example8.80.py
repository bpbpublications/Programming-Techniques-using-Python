class M1:
    num1 = 20  # static variable

    def __init__(self):
        self.num2 = 40


class M2(M1):
    def mymethod1(self):
        print(self.num2)


myobj = M2()
myobj.mymethod1()
