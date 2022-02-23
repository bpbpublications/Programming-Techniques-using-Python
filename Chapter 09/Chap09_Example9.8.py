try:
    myfile1 = open("mydemofile.txt", "w")
    myfile2 = open("mydemofile1.txt", "r")
    print("mydemofile readable status is:", myfile1.readable()) # R1
    print("mydemofile1 readable status is:", myfile2.readable()) # R2
finally:
    myfile1.close()
    myfile2.close()
