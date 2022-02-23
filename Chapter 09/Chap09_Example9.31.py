from zipfile import *
myfile1=ZipFile("E:\\python_progs\\zip\\myfiles.zip",'r',ZIP_STORED)
myfilename=myfile1.namelist()
for myfile in myfilename:
    print("File Name is : ",myfile)
    print("The Contents of this file are:")
    myf1=open(myfile,'r')
    print(myf1.read())
    print() 
    print("------------------")
