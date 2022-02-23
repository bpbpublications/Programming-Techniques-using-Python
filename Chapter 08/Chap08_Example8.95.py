class Demo:
    def __init__(self, num1=None, num2=None,num3 = None):
        print('It is a constructor where we can pass 0, 1, 2 or 3 arguments based on the need')

mobj = Demo() # No arguments
mobj = Demo(1) # 1 argument
mobj = Demo(1,2) # 2 arguments
mobj = Demo(1,2,3) # 3 arguments
