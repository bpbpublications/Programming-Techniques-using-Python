def mydecorator(myfunc):
    def func1(myname):
        if myname=="Michael":
            print("Hello",myname,"!Your functionality is extended!")
        else:
            myfunc(myname)
    return func1

def greet(myname):
    print("HI!",myname,"!Welcome to learning decorators!") 

greet = mydecorator(greet)
greet('Tom')
greet('Latham')
greet('Michael')