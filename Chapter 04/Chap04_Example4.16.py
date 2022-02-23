def outer_func(str1):
    var1 = " is awesome"
    def nested_func():
        print(str1 + var1)
    return nested_func

myobj = outer_func('Python')
myobj()
