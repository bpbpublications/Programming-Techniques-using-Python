try:
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except (ArithmeticError,ValueError) as msg1:
    print(f"The type of exception is {type(msg1)}")
    print(f"The exception class name is {msg1.__class__.__name__}")
    print("The input is not valid")
