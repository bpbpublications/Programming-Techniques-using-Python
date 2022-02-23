myemp = {
      'Name': 'Steve',
      'Age':58,
      'Sex': 'Male'}
print(myemp)# K1
print(myemp.keys())# K2
myrem = myemp.popitem()
print(myrem, 'is removed')# K3
print(myemp.keys())# K4
print(list(myemp.keys()))# K5
for key in myemp.keys(): # K6
      print(key)
