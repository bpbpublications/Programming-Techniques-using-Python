try:
    print("inside try")
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except ValueError:
    print("inside ValueError")
print("Between 2 except blocks")
except ZeroDivisionError:
    print("inside ZeroDivisonError")
