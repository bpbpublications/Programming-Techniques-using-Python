from time import *

mylocal_time = ctime(1587988490.7900558) # epoch time is passed in seconds
print("The corresponding date and time is: ",mylocal_time)

mylocal_time = ctime() # epoch time is not passed
print("The current date and time is: ",mylocal_time)
