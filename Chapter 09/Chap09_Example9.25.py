#creating a file
myfile1 = open("demo1234.txt", "w")

# displaying the file name
print("File name is: ", myfile1.name)

# checking whether file is connected to end device or not
myret = myfile1.isatty()

print("Return value : ", myret)

# file is getting closed
myfile1.close()
