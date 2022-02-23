# Case- I: Code using without array

employee1 = 60001
employee2 = 60002
employee3 = 60003
employee4 = 60004
employee5 = 60005

print(employee1)
print(employee2)
print(employee3)
print(employee4)
print(employee5)


# Case - II: Code using with array

import array as ar
employee_staffnum = ar.array("I", [60001, 60002, 60003, 60004, 60005] )
for loop in employee_staffnum:
    print(loop)