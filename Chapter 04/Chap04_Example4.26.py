def factorial(a):
    if a == 1:
        return 1
    else:
        return (a * factorial(a-1))

num = 7
print("The factorial of", num, "is", factorial(num))
