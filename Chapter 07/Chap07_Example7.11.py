import array as ar #R1
my_number = ar.array('i',[11,19,38,19,-49,-14])# R2
print("Original array before remove: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # R3
print()
print("-----------------")
my_number.remove(19) # R4
print("New array after remove: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # R5

my_number.remove(59) # R6
