#code without set comprehension
mys1 = set()
for loop in range(11):
    if loop %2 == 0:
        mys1.add(loop **3)
print(mys1)

#code with set comprehension
mys2 = {loop **3 for loop in range(11) if loop %2 == 0}
print(mys2)
