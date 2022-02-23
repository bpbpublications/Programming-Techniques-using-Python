try:
    print("inside try")
except:
    print("inside except")
else:
    print("inside else")
finally:
    try:
        num1= int(input(" Enter the first number: "))
        num2= int(input(" Enter the second number: "))
        total = num1 / num2
        print("The division is ", total)
    except ValueError:
        print("inside ValueError")
    else:
        print("else block")
    finally:
        print("finally block")