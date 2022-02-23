import array as ar # E1
my_number = ar.array('i',[11,19,38,19,-49,-14]) # E2
appendarr = ar.array('i',[100,200,-300]) # E3
print("Original array before extend : ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # E4
print()
print("-----------------")
my_number.extend(appendarr) # E5
print("New array after extend: ", end = " ")
for loop in range(len(my_number)):
    print(my_number[loop], end = ' ') # E6