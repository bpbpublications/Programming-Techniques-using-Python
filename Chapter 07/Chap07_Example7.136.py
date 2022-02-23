#code without dictionary comprehension
cube_dict = dict()
for mynum in range(1,6):
    cube_dict[mynum] = mynum**3
print(cube_dict)

#code with dictionary comprehension
my_cube_dict_comp = {mynum: mynum**3 for mynum in range(1, 6)}
print(my_cube_dict_comp)
