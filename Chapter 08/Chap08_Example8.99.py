class M1:
    def __init__(self):
        print("I am a Parent class constructor")


class M2(M1):
    def __init__(self):
        print("I am a Child class constructor")


myobj = M2()
