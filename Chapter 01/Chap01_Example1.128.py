x = [1,2,3,4]
b1 = bytes(x)
print(b1) # --- BY1
print(type(b1)) # --- BY2
print(b1[1]) # --- BY3
print(b1[-3]) # --- BY4
for i in b1:
    print(i) # --- BY5

size1 = 3
arr1 = bytes(size1)
print(arr1)# --- BY6

st1 = "Python is interesting."
# string with encoding 'utf-8'
arr2 = bytes(st1, 'utf-8')
print(arr2)# --- BY7