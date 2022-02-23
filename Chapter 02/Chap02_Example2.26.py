#format_map

str1 = {'a':'Saurabh', 'b':'Chandrakar'} 
print("{a}'s last name is {b}".format_map(str1)) # -- FM1

# Input dictionary 
identity = { 'name':['Ram', 'Shyam'], 
               'profession':['Lawyer', 'Carpenter'], 
               'Telephone_num':[40, 41] } 
                       

print('{name[0]} is a {profession[0]} and his telephone number is'
      ' is {Telephone_num[0]} years old.'.format_map(identity)) # -- FM2
        
print('{name[1]} is a {profession[1]} and his telephone number is'
      ' is {Telephone_num[1]} years old.'.format_map(identity))  # -- FM3

class Pixel(dict):
    def __missing__(self, key):
      return key

print('({a}, {b})'.format_map(Pixel(a='10'))) # -- FM4
print('({a}, {b})'.format_map(Pixel(b='12'))) # -- FM5
print('({a}, {b})'.format_map(Pixel(a='6', b ='12'))) # -- FM6