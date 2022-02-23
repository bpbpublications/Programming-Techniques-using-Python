try:
    myfile1 = open("mydemofile.txt", "w")
    myfile2 = open("mydemofile.txt", "r")
    myfile3 = open("mydemofile.txt", "a")

    print("mydemofile mode is:", myfile1.mode) # M1
    print("mydemofile mode is:", myfile2.mode) # M2
    print("mydemofile mode is:", myfile3.mode) # M3
finally:
    myfile1.close()
    myfile2.close()
    myfile3.close()
