my_num = int(input('Enter the number of rows: '))
for a in range(0,my_num):
    for b in range(0,my_num-a-1):
        print(end = " ")
    for c in range(0,a+1):
        print('*',end = " ")
    print()
