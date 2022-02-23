import array as ar # F1
myarray = ar.array("i", [] ) # F2
myarrlen = int(input("Kindly enter the array length: ")) # F3
for loop in range(myarrlen):
    myarray.append(int(input("Enter element number: "))) # F4

for loop in range(len(myarray)):
    print(myarray[loop]) # F5
