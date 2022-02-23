mys1 = {1,2,3,4}
mys2 = {1,2,3,4,5,6}
print(mys1.issubset(mys2)) # ISUB1

mys3 = {'a','b','c','d'}
mys4 = {'d','w','f','g'}
mys5 = {'a','b', 'c', 'd','v','w','x','z'}
print(mys3.issubset(mys4)) # ISUB2
print(mys4.issubset(mys5)) # ISUB3
print(mys3.issubset(mys5)) # ISUB4
