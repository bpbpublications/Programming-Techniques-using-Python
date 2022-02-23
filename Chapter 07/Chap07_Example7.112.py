#code without set comprehension
mys1 = set()
for loop in range(11):
    if loop %2 == 0:
        mys1.add(loop **3)
    else:
        mys1.add(loop**2)
print(mys1)

#code with set comprehension
mys2 = {loop **3  if loop %2 == 0 else loop**2 for loop in range(11)}
print(mys2)
