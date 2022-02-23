def myfunc():
    print("Inside function")


if __name__ == '__main__':
    print("Program Execution is direct")
    print("The value of __name__ is", __name__)
    myfunc()

else:
    print("Program execution is indirectly as a module from some other program")
    print("The value of __name__ is", __name__)
