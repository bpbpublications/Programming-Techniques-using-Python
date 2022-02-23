mys1 = {1,2,3,4}
mys2 = {3,4,5,6}
mys1.difference_update(mys2)
print(mys1) # DU1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'v','w','x','z'}
mys3.difference_update(mys4)
print(mys3) # DU2
mys4.difference_update(mys5)
print(mys4) # DU3
