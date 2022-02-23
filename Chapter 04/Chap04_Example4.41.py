def f1(w):
    def g1(x, y, z):
        print(w, x, y, z)

    return g1  # as in f1 it return g1 this is currying


my_f1 = f1(11)
my_f1(12, 13, 14)
