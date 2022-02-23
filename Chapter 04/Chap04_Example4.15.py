def outer(a):
    b = 3
    b += a
    def inner(c):
        b = 6
        print(c**b)
    print(b)
    inner(3)
outer(1)
