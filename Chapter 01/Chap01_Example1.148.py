#range
r1 = range(5)
print(type(r1)) # -- RA0
for i in r1:
    print(i) # -- RA1
print(r1[4]) # -- RA2
print(r1[-5]) # -- RA3
print(r1[1:3]) # -- RA4

r2 = range(15,20)
for i in r2:
    print(i) # -- RA5

r3 = range(10,20,2)
for i in r3:
    print(i) # -- RA6

l1 = list(r3)
print(l1) # -- RA7

print(list(range(2, -14, -2))) # -- RA8
print(list(range(2, 14, -2))) # -- RA9