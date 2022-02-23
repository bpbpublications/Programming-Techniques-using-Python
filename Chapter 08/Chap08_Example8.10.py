def mydecorator(myfunc):
    def func1(myname):
        if myname=="Jordan":
            print("Hello",myname,"!Your functionality is extended!")
        else:
            myfunc(myname)
    return func1

def greet(myname):
    print("HI!",myname,"!Welcome to learning decorators!") 

mydecor = mydecorator(greet)
greet('Tom') # non execution of decorator function
greet('Latham') # non execution of decorator function
mydecor('Michael') # execution of decorator function
mydecor('Jordan') # execution of decorator function