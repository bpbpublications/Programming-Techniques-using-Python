# file creation
myfile1 = open("truncate.txt", "w")

# writing data to the file
myfile1.write("Python is a user-friendly language for beginners")

# file truncating to 30 bytes
myfile1.truncate(30)

# file is getting closed
myfile1.close()

# file reading and displaying the text
myfile2 = open("truncate.txt", "r")
print(myfile2.read())

# closing the file
myfile2.close()
