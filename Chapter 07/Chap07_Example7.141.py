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

mynum = my_generator_function() # G0
print(type(mynum)) # G1
print(next(mynum)) # G2
print(next(mynum)) # G3
print(next(mynum)) # G4
print(next(mynum)) # G5
print(next(mynum)) # G6