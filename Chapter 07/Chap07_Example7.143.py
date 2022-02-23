class my_Pow_Three:
    def __init__(self, mymax = 0):
        self.mymax = mymax

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num > self.mymax:
            raise StopIteration

        myresult = 3 ** self.num
        self.num += 1
        return myresult
  
num1 = my_Pow_Three(5)
for loop in num1:
      print(loop)