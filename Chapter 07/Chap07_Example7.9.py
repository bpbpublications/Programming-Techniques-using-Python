import array as ar # I1
my_number = ar.array('i',[11,19,38,-49,-14]) # I2
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # I3
print()
print("-----------------")
my_number.insert(1,-28) # I4
my_number.insert(4,32) # I5
print("New array")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # I6
