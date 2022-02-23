class Uppercase_decorator:
    def __init__(self, myfunc):
        self.myfunc = myfunc

    def __call__(self):
        mystr1 = self.myfunc()
        return mystr1.upper()


# adding class decorator to the function mygreet
@Uppercase_decorator
def mygreet():
    return "good evening"


print(mygreet())
