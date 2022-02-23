import array as ar
my_number = ar.array('i',[11,19,38,19,-49,-14])
print("Original array before reverse : ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ')# RV1
print()
print("-----------------")
my_number.reverse()# RV2
print("New array after reverse: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # RV3
