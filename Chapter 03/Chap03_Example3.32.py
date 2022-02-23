try:
    print("inside try block")
    try:
        num1= int(input(" Enter the first number: "))
        num2= int(input(" Enter the second number: "))
        total = num1 / num2
        print("The division is ", total)
    except ValueError:
        print("Inside ValueError")
    finally:
        print("Inside finally block")
except ZeroDivisionError:
    print("Outside except block with ZeroDivision Error")
finally:
    print("Outside finally block")