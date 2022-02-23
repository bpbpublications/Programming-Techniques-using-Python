def myfunc_len(element):
    return len(element)

myl1 = ['Banana','Apple','Litchi','Watermelon','Mango']
myl1.sort(reverse = False, key = myfunc_len)
print(myl1)
