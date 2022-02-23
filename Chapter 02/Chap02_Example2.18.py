s1 = "HELLO BEGINNERS"
print(s1.casefold()) # -- CF1
s2 = "Hello Beginners"
print(s2.casefold()) # -- CF2

if s1.casefold() == s2.casefold(): # -- CF3
    print("Both the strings are same after conversion")
else:
    print("Both the strings are different after conversion ")
