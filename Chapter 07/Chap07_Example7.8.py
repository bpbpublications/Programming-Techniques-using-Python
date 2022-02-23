import array as arr # W1
myarray = arr.array("i", [] ) # W2
myarrlen = int(input("Kindly enter the array length: ")) # W3
ele = 0
while ele < myarrlen:
    myarray.append(int(input("Enter element number: "))) # W4
    ele +=1
i=0
while len(myarray)>i:
    print(myarray[i]) # W5
    i += 1
