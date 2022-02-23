myemp = {'Name': 'Michael','Age':39}
print(myemp.get('Name')) # G1
print(myemp.get('Age')) # G2

print(myemp.get('MobileNumber')) # G3
print(myemp.get('MobileNumber',9876543210)) # G4
print(myemp.get('Age',34)) # G5
