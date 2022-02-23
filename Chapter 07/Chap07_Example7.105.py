mys1 = {1,2,3,4}
mys2 = {3,4,5,6}
mys1.symmetric_difference_update(mys2)
print(mys1) # SU1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'v','w','x','z'}
mys3.symmetric_difference_update(mys4)
print(mys3) # SU2
mys4.symmetric_difference_update(mys5)
print(mys4) # SU3