try:
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except ValueError:
    print("It is a Value error")
except ZeroDivisionError:
    print("It is a zero division error")
