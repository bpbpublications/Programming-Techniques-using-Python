#lambda and map()
l1 = [1,2,3,4,5]

def square(x):
    return x**2
print(map(square,l1)) # M1
print(list(map(square,l1))) # M2
print(tuple(map(square,l1))) # M3

var1 = lambda x: x**2
print(list(map(var1,l1))) # M4
print(tuple(map(var1,l1))) # M5

#adding 2 lists
l2 = [3,4,5,6]
l3 = [2,2,2,2]

print(list(map(lambda x,y: x+y,l2,l3))) # M6

#adding list and tuple
l2 = [3,4,5,6]
l3 = (2,2,2,2)
print(list(map(lambda x,y: x+y,l2,l3))) # M7
