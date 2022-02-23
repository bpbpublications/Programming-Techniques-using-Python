#bytearray data type
x1 = [1,2,3,5]
a1 = bytearray(x1)
print(a1) # -- BA1
print(type(a1)) # -- BA2
for i in a1:
    print(i) # -- BA3
a1[0] = 23
for i in a1:
    print(i) # -- BA4
    
str = "python"
# encoding the string with unicode 8 and 16 
ar1 = bytearray(str, 'utf-8') 
ar2 = bytearray(str, 'utf-16') 
print(ar1) # -- BA5
print(ar2) # -- BA6

# array size
size1 = 3
a2 = bytearray(size1)
print(a2) # -- BA7

l1 = [21, 12, 17, 8] 
# iterable as source 
a3 = bytearray(l1) 
print(a3)   # -- BA8
print("Count of bytes:", len(a3))   # -- BA9

a4 = bytearray() 
print(a4)  # -- BA10