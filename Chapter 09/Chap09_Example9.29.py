import csv
myfile1=open("mycsvfile1.csv",'r')
myfile1=csv.reader(myfile1) #returns csv reader object
print(type(myfile1))
mydata=list(myfile1)
print(mydata) # list of list returning
for myrow in mydata: # iterating each element as list
    for mycol in myrow:# iterating each element of list
        print(mycol,'\t',end='')
    print()
