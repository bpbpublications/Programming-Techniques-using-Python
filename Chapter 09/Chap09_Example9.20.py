with open('readinput.txt') as myfile1:
    print(myfile1.tell()) # T1
    print("-----------")
    print(myfile1.read(4)) # T2
    print(myfile1.tell()) # T3
    print("-----------")
    print(myfile1.read()) # T4
    print(myfile1.tell()) # T5
