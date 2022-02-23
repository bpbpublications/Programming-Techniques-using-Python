try:
    myfile1 = open("mydemofile.txt", "w")
    myfile2 = open("mydemofile1.txt", "w", encoding = 'utf-16')
    print("mydemofile encoding format is:", myfile1.encoding) # E1
    print("mydemofile1 encoding format is:", myfile2.encoding) # E2
finally:
    myfile1.close()
    myfile2.close()
