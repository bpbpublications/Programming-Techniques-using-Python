#code without list comprehension
myl1 = []
for a in range(4,6):
    for b in range(3,5):
        myl1.append(a*b)
print(myl1)

#code with list comprehension
lic1 = [a*b for a in range(4,6) for b in range(3,5)]
print(lic1)
