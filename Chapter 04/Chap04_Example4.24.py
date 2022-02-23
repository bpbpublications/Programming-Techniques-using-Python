num1 = 1
def display():
    num1 = 2
    print("local variable: ", num1)
    num2 = globals()['num1']
    print(num2)
    num2 = 3
    print(num2)
display()
print('global variable: ', num1)
