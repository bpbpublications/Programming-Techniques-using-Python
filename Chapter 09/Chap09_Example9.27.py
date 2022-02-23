import csv
with open("mycsvfile1.csv","w") as myfile1:
    mywrite=csv.writer(myfile1) # CS1
    print(type(mywrite)) # CS2
    mywrite.writerow(["ROLLNO","NAME","AGE","CONTACT"]) # CS3
    while True:
        myroll_no=input("Enter Student Roll No:") # CS4
        myname=input("Enter Student Name:") # CS5
        myage=input("Enter Student Age:") # CS6
        mycontactno=input("Enter Student contact number:") # CS7
        mywrite.writerow([myroll_no,myname,myage,mycontactno]) # CS8
        check = input("Do you want to enter one more student data: (Yes|No): ") # CS9
        if check.upper() == 'NO': # CS10
            break
print("Total Students data written to csv file successfully")
