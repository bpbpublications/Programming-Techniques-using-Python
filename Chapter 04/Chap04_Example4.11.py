def mymul(*my_num):
    myresult = my_num[0]*my_num[1]*my_num[2]
    return myresult

def mymul2(first, *my_num):
    myresult = first*my_num[0]*my_num[1]
    return myresult

def mymul3(*my_num):
    myresult = 1
    for loop in my_num:
        myresult *= loop
    return myresult

print(mymul(2,3,4)) # V1
print(mymul(2,3,4,5)) # V2
print(mymul2(2,3,4)) # V3
print(mymul2(2,3,4,5)) # V4
print(mymul3(2,3,4,5)) # V5
