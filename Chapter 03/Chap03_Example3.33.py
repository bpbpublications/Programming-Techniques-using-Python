try:
    print("inside try")
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
except:
    print("inside except block")
else:
    print("inside else part")
finally:
    print("inside finally part")
