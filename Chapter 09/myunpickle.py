import pickle, student
myfile1=open("mypick_umpickle1.dat","rb")
print("Student Details:")
while True:
    try:
        myobj=pickle.load(myfile1)
        myobj.mydisplay()
    except EOFError:
        print("All students Completed")
        break
myfile1.close() 
