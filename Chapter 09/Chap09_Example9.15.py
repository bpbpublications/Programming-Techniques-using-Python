try:
    myfile1 = open("mywrite3.txt",'x')
    num1 = myfile1.writelines({"Python is awesome.","Beginners are welcome here"})
    print("Set Data is written after creating a file exclusively for write operation")
finally:
    myfile1.close()
