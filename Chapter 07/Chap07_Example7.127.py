myemp = {
      'Name': 'Priyanka',
      'Age':39,
      'Sex': 'Female'}

print("data of employee dictionary...")
print(myemp)  # P1

myrem = myemp.pop('Name')
print(myrem, ' is removed.')  # P2

myrem = myemp.pop('Age')
print(myrem, ' is removed.')  # P3

print("data of employee dictionary after removing Name and Age...")
print(myemp)  # P4

myrem = myemp.pop('LandlineNumber', 'Landline Number does not exist.')
print(myrem)  # P5

myrem = myemp.pop('LandlineNumber')
print(myrem)  # P6