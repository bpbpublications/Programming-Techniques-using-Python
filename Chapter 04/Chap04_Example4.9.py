def my_details(name,age):
    print(f'My name is {name} and age is {age} ')

def my_details1(name,age = 31):
    print(f'My name is {name} and age is {age} ')

my_details('Mukesh',31) # D1
my_details1(name = 'Mukesh') # D2
my_details1('Ramesh',32) # D3
