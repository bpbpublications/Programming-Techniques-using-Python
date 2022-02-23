def outside_func():
    def inner_func():
        print("Inside Inner Function")
    print("Inside Outer Function")
    inner_func()

outside_func()
