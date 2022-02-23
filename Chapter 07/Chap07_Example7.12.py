import array as ar #IN1
my_number = ar.array('i',[11,19,38,19,-49,-14])# IN2
print("Original array ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # IN3
print()
print("-----------------")
print(my_number.index(19)) # IN4
print(my_number.index(59)) # IN5
