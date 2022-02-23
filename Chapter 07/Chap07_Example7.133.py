myemp = {
      'Name': 'Priyanka',
      'Age':27,
      'Sex': 'Female',
      'Profession': 'Scientist'}
print(myemp) # SD1
myage = myemp.setdefault('Age')
print(myage) # SD2
mysalary = myemp.setdefault('salary', 100000)
print(myemp) # SD3
print(mysalary) # SD4
mynumber = myemp.setdefault('mobilenumber')
print(myemp) # SD5
print(mynumber) # SD6