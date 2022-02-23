myl1 = []
num = int(input("Enter the number of elements: "))

for loop in range(num):
      myl1.append(input(f"Enter element at index {loop} : "))
      
print(myl1)
print(type(myl1))
myt1 = tuple(myl1)
print(myt1)
print(type(myt1))

print("The elements of tuple object are: ")
for loop in myt1:
      print(loop)