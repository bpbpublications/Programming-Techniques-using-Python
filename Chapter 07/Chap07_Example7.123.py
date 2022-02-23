d1 = dict()
print(d1)  # DI1
print(type(d1))

d2 = dict({1:'a',2:'b',3:'c'})
print(d2) # DI2

d3 = dict([(1,"python"),(2,"is"),(3,"awesome")])
print(d3) # DI3

d4 = dict(((1,"python"),(2,"is"),(3,"awesome")))
print(d4) # DI4

d5 = dict({(1,"python"),(2,"is"),(3,"awesome")})
print(d5) # DI5

d6 = dict({[1,"python"],[2,"is"],[3,"awesome"]})
print(d6) # DI6