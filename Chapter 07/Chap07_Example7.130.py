myemp = {
      'Name': 'Angela',
      'Age':30,
      'Sex': 'Female',
      'Profession': 'Doctor'}
print(myemp)# V1
print(myemp.values())# V2
myrem = myemp.pop('Sex')
print(myrem, 'is removed')# V3
print(myemp.values())# V4
print(tuple(myemp.values()))# V5
for value in myemp.values():
      print(value)# V6
