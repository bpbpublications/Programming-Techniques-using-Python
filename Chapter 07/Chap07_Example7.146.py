myl1=[x*x for x in range(10000000000000)]
while True:
      print(myl1[0]) # M1

mygen=(x*x for x in range(1000000))
while True:
      print(next(mygen)) # M2
