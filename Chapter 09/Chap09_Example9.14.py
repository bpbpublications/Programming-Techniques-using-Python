try:
    myfile1 = open("mywrite1.txt",'a')
    num1 = myfile1.writelines(["Beginners ","are ","welcome ","here"])
    print("Data written successfully from list")
finally:
    myfile1.close()
