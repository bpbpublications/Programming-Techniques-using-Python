def outside_func(str1):
    def inner_func():
        print(str1 + "Inner Function")
    print("Inside Outer Function")
    inner_func()

outside_func("Hello ")
