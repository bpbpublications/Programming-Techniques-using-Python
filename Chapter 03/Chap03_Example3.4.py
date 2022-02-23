my_age = float(input("Enter the age: "))
if my_age > 0 and my_age < 1.5:
    print("The age is of infant")
elif my_age >=1.5 and my_age <12:
    print("The age is of children")
elif my_age >=12 and my_age <17:
    print("The age is of Teenager")
elif my_age >=17 and my_age <30:
    print("The age is of adult")
elif my_age >=30 and my_age <46:
    print("Middle aged person")
else:
    print("The age is of elder person")
