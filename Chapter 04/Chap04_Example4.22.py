g1 = 1
def display():
    global g1
    g1 = 2
    print(g1)
    print("inside",id(g1))
display()
print(g1)
print("outside",id(g1))
