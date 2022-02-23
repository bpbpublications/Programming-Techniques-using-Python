class Demo:
    def __init__(self):
        print('No arguments')

    def __init__(self, num1):
        print('Single argument')

    def __init__(self, num1, num2):
        print('Two arguments')


mobj = Demo(1, 2)
mobj = Demo(1)
