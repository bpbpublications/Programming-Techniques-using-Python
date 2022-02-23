#M1
l1 = [0,1,2,5,7,9,12,16,19,21,24,28,31]
def iseven_odd(num):
    if num %2 != 0:
        return True
    else:
        return False
print(list(filter(iseven_odd, l1)))

#M2
print(list(filter(lambda num: num % 2 != 0, l1)))
