myemp = {
      'Name': 'Alestair',
      'Age':58,
      'Sex': 'Male'}
print(myemp) # PI1
myrem = myemp.popitem()
print(myrem, 'is removed') # PI2
myrem = myemp.popitem()
print(myrem, 'is removed') # PI3
myrem = myemp.popitem()
print(myrem, 'is removed') # PI4
print(myemp) # PI5
print(myemp.popitem())# PI6