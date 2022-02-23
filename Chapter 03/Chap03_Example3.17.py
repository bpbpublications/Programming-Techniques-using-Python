num = int(input('Enter the number: '))
count = 1
for my_row in range(1,num + 1):
    for my_col in range(1,my_row+1):
        print(count,end = ' ')
        count +=1
    print()
