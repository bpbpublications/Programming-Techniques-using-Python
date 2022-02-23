# set declaration
myfruits = {"Apple", "Banana", "Grapes", "Litchi", "Mango"}
mynums = {1, 2, 3, 4, 5}

# Set printing before removing
print("Before remove() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)

# Removing the elements from the sets
elerem = myfruits.remove('Apple')
elerem = myfruits.remove('Litchi')
elerem = myfruits.remove('Mango')

elerem = mynums.remove(1)
elerem = mynums.remove(3)
elerem = mynums.remove(4)

print("After remove() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)