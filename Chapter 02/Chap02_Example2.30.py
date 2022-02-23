#isdecimal
n1 = "947"
print(n1.isdecimal()) # -- D1
n2 = "947 2"
print(n2.isdecimal()) # -- D2
n3 = "abx123"
print(n3.isdecimal()) # -- D3
n4 = "\u0034"
print(n4.isdecimal()) # -- D4
n5 = "\u0038"
print(n5.isdecimal()) # -- D5
n6 = "\u0041"
print(n6.isdecimal()) # -- D6
n7 = "3.4"
print(n7.isdecimal()) # -- D7
n8 = "#$!@"
print(n8.isdecimal()) # -- D8
