def func1(**kwargs):
    print(kwargs) # F1
    print(type(kwargs)) # F2
    for my_key,my_value in kwargs.items():
        print(f"{my_key}:{my_value}") # F3

def func2(name1,**kwargs):
    print(kwargs) # F4
    print(name1) # F5
    print(type(kwargs)) # F6
    for my_key,my_value in kwargs.items():
        print(f"{my_key}:{my_value}") # F7

def func3(**kwargs):
    for my_key,my_value in kwargs.items():
        print(f"{my_key}:{my_value}") # F9

func1(fname = "Saurabh",lname = "chandrakar", phone_number = 9876543210) # F10
func2(1,fname = "Priyanka",lname = "chandrakar", phone_number = 8987676543) # F11

#dictionary unpacking
d1 = dict(name ='Saurabh',age = 31)
func3(**d1) # F12
