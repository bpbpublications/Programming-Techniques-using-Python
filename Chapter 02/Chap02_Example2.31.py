n1 = "123"
print(n1.isdigit()) # -- ID1
n2 = "345 2"
print(n2.isdigit()) # -- ID2
n3 = "345 2b"
print(n3.isdigit()) # -- ID3
n4 = "\u0035"
print(n4.isdigit()) # -- ID4
n5 = "\u00BC"
print(n5)
print(n5.isdigit()) # -- ID5
n6 = "\u00B2343"
print(n6)
print(n6.isdigit()) # -- ID6
n7 = "8.9"
print(n7.isdigit()) # -- ID7
n8 = "123-456-975"
print(n8.isdigit()) # -- ID8