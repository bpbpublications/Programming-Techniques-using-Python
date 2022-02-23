myemp = {
      'Name': 'Angela',
      'Age':30,
      'Sex': 'Female',
      'Profession': 'Doctor'}
print(myemp.items())# I1
print(type(myemp.items()))# I2
for key, value in myemp.items():
      print(key, '-----',value)# I3
