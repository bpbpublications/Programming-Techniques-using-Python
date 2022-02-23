def mysum(mymarks):
    assert len(mymarks) != 0, "Empty list"
    return sum(mymarks)

myl1 = [1,2,3,4,5,6]
print("Sum of list myl1 is:",mysum(myl1))

myl2 = []
print("Sum of  list myl2 is:",mysum(myl2))
