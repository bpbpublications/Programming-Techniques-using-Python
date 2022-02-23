myt1 = ('a','b','c')
myval = 1
myd1 = dict.fromkeys(myt1,myval)# FK1
print(myd1)# FK2
myd1 = dict.fromkeys(myt1)# FK3
print(myd1)# FK4
mys1 = {'a','b','c'}
myval = [100]
myd2 = dict.fromkeys(mys1,myval)# FK5
print(myd2)# FK6
myval.append(10)# FK7
print(myd2)# FK8