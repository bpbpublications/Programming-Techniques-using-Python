try:
    print("inside try")
    print(1/0)
except:
    try:
        num1= int(input(" Enter the first number: "))
        num2= int(input(" Enter the second number: "))
        total = num1 / num2
        print("The division is ", total)
    except ValueError:
        print("inside ValueError")
    else:
        print("inside else")
    finally:
        print("inside finally block")