def f1(a):
    def g1(b):
        def h1(c):
            def i1(d):
                def j1(e):
                    print(a, b, c, d, e)

                return j1  # return to function i1

            return i1  # return to function h1

        return h1  # return to function g1

    return g1  # return to function f1


f1(21)(22)(23)(24)(25)
