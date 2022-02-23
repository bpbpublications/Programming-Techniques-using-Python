try:
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except ValueError as msg1:
    print("The input is not valid")
except:
    print("Default except block")
