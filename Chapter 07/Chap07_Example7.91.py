mys1 = {'10',20,30}
myl1 = [1,2,3,4]
mys1.update(myl1)
print(mys1) # U1
mys1.update(myl1,range(1,4))
print(mys1) # U2
mys2 = {100,200}
mys1.update(mys2)
print(mys1) #U3
myt1 = (100,)
mys1.update(myt1)
print(mys1) #U4
