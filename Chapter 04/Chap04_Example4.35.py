def mylist(l1):
    print('b', l1, id(l1))
    l1.append(40)
    print('c', l1, id(l1))

l1 = [10,20,30]
print('a', l1, id(l1))
mylist(l1)
print('d', l1, id(l1))
