class MyOuter:
    def __init__(self):
        print("outer class object is created")
     
    class MyInner:
        def __init__(self):
            print("inner class object is created")
        def mymethod1(self):
            print("It is an inner class method")

#M-1
myobj=MyOuter() # creating an outer class object
myinner_obj=myobj.MyInner() # creating an inner class object
myinner_obj.mymethod1() # calling inner class method
print('*'*25)

#M-2
myinner_obj1=MyOuter().MyInner()
myinner_obj.mymethod1()
print('*'*25)

#M-3
MyOuter().MyInner().mymethod1()