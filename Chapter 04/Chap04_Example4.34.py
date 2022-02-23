def myadd(b): # -- L1
    b += 2 # -- L2
    print(b) # -- L3
    return b # -- L4

a = 2 # -- L6
res = myadd(a) # -- L7
print(a) # -- L8
print(res) # -- L9
