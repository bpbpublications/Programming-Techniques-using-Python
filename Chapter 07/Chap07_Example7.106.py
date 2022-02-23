mys1 = {1,2,3,4}
mys2 = {3,4,5,6}
print(mys1.isdisjoint(mys2)) # ID1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'v','w','x','z'}
print(mys3.isdisjoint(mys4)) # ID2
print(mys4.isdisjoint(mys5)) # ID3
print(mys3.isdisjoint(mys5)) # ID4