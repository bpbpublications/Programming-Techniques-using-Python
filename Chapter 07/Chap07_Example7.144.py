def my_Pow_Three(max = 0):
    num = 0
    while num <= max:
        yield 3 ** num
        num += 1

mynum = my_Pow_Three(5)
for loop in mynum:
      print(loop)
