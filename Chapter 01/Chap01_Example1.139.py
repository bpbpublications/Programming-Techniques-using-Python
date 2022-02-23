#tuple data type
t1 = (5,6,2,1)
print(t1) # -- T1
print(t1[2]) # -- T2
print(t1[-3]) # -- T3
print(t1[1:]) # -- T4
for i in t1:
    print(i) # -- T5

print(len(t1)) # -- T6
t2 = (1,2,3)
t3 = t1+t2
print(t3) # -- T7
t4 = t1 *3
print(t4) # -- T8
print(3 in t1) # -- T9
