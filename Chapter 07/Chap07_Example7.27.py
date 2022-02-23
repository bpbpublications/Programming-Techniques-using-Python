myl1 = [10,11,14,17,19,20,14,35,14]
print(myl1.index(14)) # IN1
myl2 = ['c','o','r','o','n','a','w','a','r','r','i','o','r','s']
search_element = input("Enter the element to be searched: ")
if search_element in myl2:
    print(f"The first occurrence of {search_element} is present at index no. ", myl2.index(search_element))
else:
    print(f"The element {search_element} is not present")# IN2
