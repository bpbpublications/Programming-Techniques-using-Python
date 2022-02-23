# set declaration
myfruits = {"Apple", "Banana", "Grapes", "Litchi", "Mango"}
mynums = {1, 2, 3, 4, 5}

# Set printing before removing
print("Before pop() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)

# Elements getting popped from the set
elerem = myfruits.pop()
print(elerem, "is removed from fruits")
elerem = myfruits.pop()
print(elerem, "is removed from fruits")
elerem = myfruits.pop()
print(elerem, "is removed from fruits")

elerem = mynums.pop()
print(elerem, "is removed from numbers")
elerem = mynums.pop()
print(elerem, "is removed from numbers")
elerem = mynums.pop()
print(elerem, "is removed from numbers")

print("After pop() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)