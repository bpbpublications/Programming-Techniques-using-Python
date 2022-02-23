try:
    myfile1 = open("mywrite2.txt",'x')
    num1 = myfile1.write("Python is awesome.Beginners are welcome here")
    print("The number of characters written in first line are: ", num1)
    print("Opened a file exclusively for write operation")
finally:
    myfile1.close()
