try:
    myfile1 = open("mywrite1.txt",'w')
    num1 = myfile1.write("Python\n")
    print("The number of characters written in first line including \\n are: ", num1)
    num2 = myfile1.write('is\n')
    print("The number of characters written in second line including \\n are: ", num2)
    num3 = myfile1.write('awesome\n')
    print("The number of characters written in third line including \\n are: ", num3)
    print("The total of characters written in 1st, 2nd and 3rd line are: ", num1+num2+num3)
    print("Data written successfully")
finally:
    myfile1.close()
