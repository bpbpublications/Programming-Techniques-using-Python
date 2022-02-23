import array as ar #P1
my_number = ar.array('i',[11,19,38,-49,-14])# P2
print("Original array before pop: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # P3
print()
print("-----------------")
my_number.pop() # P4
print("New array after pop: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # P5
print()
print("------------------")
print(my_number.pop(-2)) # P6