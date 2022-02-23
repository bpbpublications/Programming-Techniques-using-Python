#code without dictionary comprehension
mydict_age = {'Ankt': 31, 'Saurabh': 32, 'Nilesh': 40, 'Mr. Ben': 50}
cube_dict = dict()
for mynum in mydict_age:
      if mydict_age[mynum]>35:
           cube_dict[mynum] = 'old'
      else:
           cube_dict[mynum] = 'young' 
print(cube_dict)

#code with dictionary comprehension
new_dict = {key: 'old' if value > 35 else 'young'
    for (key, value) in mydict_age.items()}
print(new_dict)