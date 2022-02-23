t1 = (1,2,3,4,5)
t2 = ('Hello',True)
mys1 = t1[0:3] # MT1
mys2 = t1[3:] # MT2
myt1 = mys1 + t2 + mys2 # MT3
print(myt1) # MT4
print(type(myt1)) # MT5
print(id(t1)) # MT6
print(id(myt1)) # MT7
