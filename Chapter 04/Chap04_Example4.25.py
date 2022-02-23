def outer():
    a1 = 20
    b1 = 40

    def inner():
        # nonlocal binding
        nonlocal a1
        a1 = 50  # will update
        b1 = 60  # will not update,
        # it will be considered as a local variable

    inner()
    print("a1 : ", a1)
    print("b1 : ", b1)


# main code
# calling the function i.e. outer()
outer()
