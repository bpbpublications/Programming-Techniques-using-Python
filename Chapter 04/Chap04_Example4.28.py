# M1
def mul1(a1):
    return lambda b1:b1*a1
myresult = mul1(3)
print(myresult(7))

#M-2
mul = lambda a = 3: (lambda b: a*b)
myres = mul()
print(myres)
print(myres(7))
