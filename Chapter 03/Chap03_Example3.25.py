try:
    print("st1")
    print(2/0)
    print("st-3")
except Exception as e:
    print(f"The type of exception is {type(e)}") # E1
    print(f"The type of exception is {e.__class__}") # E2
    print(f"The exception class name is {e.__class__.__name__}") # E3
    print(f"The exception description is {e}") # E4
