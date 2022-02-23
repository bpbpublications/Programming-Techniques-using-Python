#code without list comprehension
myl1 = []
for loop in range(11):
    if loop %2 == 0:
        myl1.append(loop **3)
    else:
        myl1.append(loop**2)
print(myl1)

#code with list comprehension
lic1 = [loop **3  if loop %2 == 0 else loop**2 for loop in range(11)]
print(lic1)
