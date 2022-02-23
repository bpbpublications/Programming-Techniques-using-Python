def myhash(myfunc):
    def myinner(*args, **kwargs):
        print("#" * 25)
        myfunc(*args, **kwargs)
        print("#" * 25)
    return myinner

def myattherate(myfunc):
    def inner1(*args, **kwargs):
        print("@" * 25)
        myfunc(*args, **kwargs)
        print("@" * 25)
    return inner1

@myattherate
@myhash
def myprint(mymsg):
    print(mymsg)
myprint("Welcome to decorator chaining")