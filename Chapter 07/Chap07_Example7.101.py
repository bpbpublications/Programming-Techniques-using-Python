mys1 = {1,2,3,4}
mys2 = {3,4,5,6}
mys1.intersection_update(mys2)
print(mys1) # IU1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'v','w','x','z'}
mys3.intersection_update(mys4)
print(mys3) # IU2
mys4.intersection_update(mys5)
print(mys4) # IU3
