try:
    myfile1 = open("mywrite1.txt",'w')
    num1 = myfile1.writelines(("Python\n","is\n","awesome\n"))
    print("Data written successfully from tuple")
finally:
    myfile1.close()
