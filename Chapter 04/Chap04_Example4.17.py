def outer(mynum):
    def inner(a1):
        return mynum ** a1
    return inner

obj1 = outer(6)
obj2 = outer(5)
print(obj1(2))
print(obj2(3))
