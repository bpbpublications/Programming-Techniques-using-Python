from functools import reduce
myseq_list = [0,1,2,3,4,7,8,9]
mysum = reduce (lambda a, b: a+b, myseq_list)
print(mysum)
