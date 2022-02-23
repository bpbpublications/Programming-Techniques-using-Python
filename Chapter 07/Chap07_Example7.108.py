mys1 = {1,2,3,4}
mys2 = {1,2,3,4,5,6}
print(mys2.issuperset(mys1)) # ISUP1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'a','b', 'c', 'd','v','w','x','z'}
print(mys3.issuperset(mys4)) # ISUP2
print(mys4.issuperset(mys5)) # ISUP3
print(mys5.issuperset(mys3)) # ISUP4