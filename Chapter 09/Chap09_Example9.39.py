from time import *

mytime = (2020, 4, 27, 12, 13, 39, 0, 118, 0)
mymk_time = mktime(mytime)
print("The number of seconds passed since epoch is: ", mymk_time)

print("The struct time is ",localtime(mymk_time)) # getting struct time
