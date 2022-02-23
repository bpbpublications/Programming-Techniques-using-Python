#set declaration
myfruits = {"Apple", "Banana", "Grapes", "Litchi", "Mango"}
mynums = {1, 2, 3, 4, 5}

# Set printing before discarding
print("Before discard() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)

# Discarding the elements from the sets
elerem = myfruits.discard('Banana')
elerem = myfruits.discard('Litchi')
elerem = myfruits.discard('Grapes')

elerem = mynums.discard(2)
elerem = mynums.discard(3)
elerem = mynums.discard(5)

print("After discard() method...")
print("fruits: ", myfruits)
print("numbers: ", mynums)