def my_generator_function():
    num = 1
    print('Printing first')
    yield num

    num += 1
    print('Printing second')
    yield num

    num += 1
    print('Printing third')
    yield num
    
    num += 1
    print('Printing at last')
    yield num

mynum = my_generator_function()

for loop in mynum:
      print(loop)