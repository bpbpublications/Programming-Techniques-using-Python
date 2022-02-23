class Demo:
    def __init__(self, *args):
        print('It is a constructor where we can pass any number of arguments based on the need')

mobj = Demo() # No arguments
mobj = Demo(1) # 1 argument
mobj = Demo(1,2) # 2 arguments
mobj = Demo(1,2,3) # 3 arguments
mobj = Demo(1,2,3,4) # 4 arguments
mobj = Demo(1,2,3,4,5) # 5 arguments
