try:
    myfile1=open("E:\\python_progs\\demochange\\mydir2\\pic1.jpg","rb")
    myfile2=open("E:\\python_progs\\demochange\\mydir2\\newpic1.jpg","wb")
    bytes=myfile1.read()
    myfile2.write(bytes)
    print("A new Image is available having name as: newpic1.jpg")
finally:
    myfile1.close()
    myfile2.close()
