def myfunc_len(element):
    return len(element)

myt1 = ('Banana','Apple','Litchi','Watermelon','Mango')
myt2 = sorted(myt1, key = myfunc_len,reverse = False)
print(myt2)
print(type(myt2))
myt3 = tuple(myt2)
print(myt3)
print(type(myt3))
