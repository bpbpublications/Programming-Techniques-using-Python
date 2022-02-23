class M1:
    def __init__(self):
        self.num2 = 40
    def mymethod1(self):
        print("Instance method")
    @classmethod
    def mymethod2(cls):
        print("Class method")
    @staticmethod
    def mymethod3():
        print("Static method")

class M2(M1):
    def __init__(self):
        super().__init__()
        super().mymethod1()
        super().mymethod2()
        super().mymethod3()
        
myobj = M2()