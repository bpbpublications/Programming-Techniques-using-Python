# when the size is omitted
try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.read() # R1
    print(mydata)
finally:
    myfile1.close()
print("---------------------")

# when the size is -1
try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.read(-1) # R2
    print(mydata)
finally:
    myfile1.close()
print("---------------------")

# reading first 12 characters only from the file
try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.read(12) # R3
    print(mydata)
finally:
    myfile1.close()
