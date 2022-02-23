try:
    myfile1 = open('mydemowrite1.txt','r')
    mydata = myfile1.readlines()
    print(mydata) # RL1
    for loop in mydata:
        print(loop, end='')  # RL2
finally:
    myfile1.close()
