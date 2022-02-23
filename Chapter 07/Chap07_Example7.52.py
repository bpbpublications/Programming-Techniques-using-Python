#code without list comprehension
myl1 = []
for loop in range(11):
    myl1.append(loop **3)
print(myl1)

#code with list comprehension
lic1 = [loop **3 for loop in range(11)]
print(lic1)
