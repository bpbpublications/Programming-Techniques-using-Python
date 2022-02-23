from collections import namedtuple
emp=namedtuple('employee', 'name age staffnumber')
myemp = emp(name = 'Suresh',age = 31, staffnumber = 60001)
print(myemp)
print(myemp.name)
print(myemp.age)
print(myemp.staffnumber)
