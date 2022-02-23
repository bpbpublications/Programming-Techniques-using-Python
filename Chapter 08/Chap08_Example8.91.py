class Demo:
    def mymethod1(self,num1):
        print("Second method with one argument")
    def mymethod1(self,num1,num2):
        print("Third method with two arguments")

myobj = Demo()
myobj.mymethod1(2,3) # L1
myobj.mymethod1(2) # L2
