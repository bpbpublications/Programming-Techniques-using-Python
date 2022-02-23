l1 = [1,2,3]
iter1 = iter(l1)
while True:
    try:
        # Get next element using iterator object
        print(next(iter1))
    except StopIteration:
        break
