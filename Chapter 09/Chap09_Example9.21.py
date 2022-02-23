mydata="Hello! I am studying tell method."
myfile1=open("mydemofile2.txt","w")
myfile1.write(mydata)  # S0
myfile1.close()
with open("mydemofile2.txt","r+") as myfile1:
    mytext=myfile1.read()
    print(mytext) # S1
    print("Current Cursor Position: ",myfile1.tell()) # S2
    myfile1.seek(21) # S3
    print("Current Cursor Position: ",myfile1.tell()) # S4
    myfile1.write("seek method") # S5
    myfile1.seek(0)  # S6
    mytext=myfile1.read() # S7
    print("Data After modifying at position 21 is :")
    print(mytext) # S8
