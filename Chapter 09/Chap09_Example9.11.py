try:
    myfile1 = open("mywrite1.txt",'a')
    num1 = myfile1.write("Beginners are welcome here\n")
    print("The number of characters written in last line including \\n are: ", num1)
    print("Data appended successfully in the file")
finally:
    myfile1.close()
