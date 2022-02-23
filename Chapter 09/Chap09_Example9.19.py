with open('readinput.txt') as myfile1:
    mydata = myfile1.read()
    print(mydata) # W1
    print("-----------")
    print('File closed status: ?', myfile1.closed) # W2
print("-----------")
print('Again checking for file closed status ?', myfile1.closed) # W3
