#Method-1
for a in range(0,6):
    my_num = 65
    for b in range(0,a+1):
        my_alpha = chr(my_num)
        print(my_alpha,end = " ")
        my_num += 1
    print()

#Method-2
from string import ascii_uppercase
for i in range(1, 7):
    print(" ".join(ascii_uppercase[:i]))
