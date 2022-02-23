import array as ar
employee_staffnum = ar.array("I", [60001, 60002, 60003, 60004, 60005] )
myarr_len = len(employee_staffnum) # will return the number of elements.
for loop in range(myarr_len):
    print(f"{loop}: ",employee_staffnum[loop])
