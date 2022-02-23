#nested conditional operators
x = 1 if 2<3 else 4 if 5<6 else 7 # -- NC1
print(x)

y = 1 if 2>3 else 4 if 5>6 else 7 # -- NC2
print(y)

a = 8
b = 5
c = 7
x = a if a>b and a >c else b if b>c else c # -- NC3
print(x)

a = 2
b = 3
c = 1
y = a if a<b and a <c else b if b <c else c # -- NC4
print(y)