import array as ar #S1
my_number = ar.array('i',[11,19,38,19,-49,-14])# S2
print("Original array ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # S3
print()
print("-----------------")
arr1 = my_number[1:4] # S4
for loop in arr1:
    print(loop, end = ' ')
print()
print("-----------------")
arr1 = my_number[:4] # S5
for loop in arr1:
    print(loop, end = ' ')
print()
print("-----------------")
arr1 = my_number[2:] # S6
for loop in arr1:
    print(loop, end = ' ')
print()
print("-----------------")
arr1 = my_number[-3:] # S7
for loop in arr1:
    print(loop, end = ' ')
print()
print("-----------------")
arr1 = my_number[-5:-2] # S8
for loop in arr1:
    print(loop, end = ' ')