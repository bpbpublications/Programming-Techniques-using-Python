import array as ar
employee_staffnum = ar.array("I", [201, 202, 203, 204, 205] )
myarr_len = len(employee_staffnum) # will return the number of elements.

#before appending an array
for loop in range(myarr_len):
    print(f"{loop}th element is:", employee_staffnum[loop], end = ' ')
print()
print("-------------------------")
employee_staffnum.append(206)
myarr_len = len(employee_staffnum) 
# will return the number of elements after append
#after appending an array
for loop in range(myarr_len):
    print(f"{loop}th element is:", employee_staffnum[loop], end = ' ')