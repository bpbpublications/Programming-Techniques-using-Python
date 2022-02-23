try:
    myfile1 = open("mydemofile.txt", "w")
    myfile2 = open("mydemofile1.txt", "w", errors = 'ignore')
    print("mydemofile unicode error handler is:", myfile1.errors) # ER1
    print("mydemofile1 unicode error handler is:", myfile2.errors) # ER2
finally:
    myfile1.close()
    myfile2.close()
