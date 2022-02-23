myemp = {
      'Name': 'Kripki',
      'Age':29,
      'Sex': 'Male',
      'Profession': 'Scientist'}

mydict_copy = myemp.copy()
print(myemp) # C1
print(mydict_copy) # C2
print("After clearing the dictionary which was copied from 
the original using copy method")
mydict_copy.clear()
print(mydict_copy) # C3
print(myemp) # C4

myanothercopy = myemp
print(myanothercopy) # C5
print("After clearing the new dictionary which
was copied from the original using = operator")
myanothercopy.clear()
print(myanothercopy) # C6
print(myemp) # C7