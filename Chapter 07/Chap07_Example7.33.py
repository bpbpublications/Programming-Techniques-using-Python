myl1 = [11,12,13,14,11,15,16,11]
myl1.remove(11) # RM1
print(myl1)
if 17 in myl1: # RM2
    print(f"The element 17 is present in the list and is removed from the list", myl1.remove(17))
else:
    print("The element 17 is absent from the list")

try:
    myl1.remove(18) # RM3
except ValueError:
    print("ValueError: list.remove(x): x not in list")
