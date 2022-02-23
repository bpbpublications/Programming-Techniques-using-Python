try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.readline()
    print(mydata)# RE1
finally:
    myfile1.close()
print("-------------")
try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.readline(-1)
    print(mydata, end='') # RE2
finally:
    myfile1.close()
print("-------------")
try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.readline(5)
    print(mydata, end='') # RE3
finally:
    myfile1.close()
