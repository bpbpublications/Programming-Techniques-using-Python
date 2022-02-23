try:
    print("inside try")
    num1= int(input(" Enter the first number: "))
    num2= int(input(" Enter the second number: "))
    total = num1 / num2
    print("The division is ", total)
else:
    print("inside else part")
except:
    print("inside except block")
finally:
    print("inside finalaly part")