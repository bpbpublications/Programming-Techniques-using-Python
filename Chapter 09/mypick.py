import pickle, student
myfile1=open("mypick_umpickle1.dat","wb")
mynum=int(input("Enter The number of Students:"))
for i in range(mynum):
    myname=input("Enter Employee Name:")
    myage=int(input("Enter Employee Age:"))
    myrollno=int(input("Enter Roll No:"))
    myhometown=input("Enter Employee HomeTown:")
    mystu1=student.Student(myname,myage,myrollno,myhometown)
    pickle.dump(mystu1,myfile1)
print("Student Objects pickled successfully") 
