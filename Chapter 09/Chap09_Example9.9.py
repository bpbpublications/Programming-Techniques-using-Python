try:
    myfile1 = open("mydemofile.txt", "w")
    myfile2 = open("mydemofile1.txt", "r")
    print("mydemofile writable status is:", myfile1.writable()) # W1
    print("mydemofile1 writable status is:", myfile2.writable()) # W2
finally:
    myfile1.close()
    myfile2.close()
