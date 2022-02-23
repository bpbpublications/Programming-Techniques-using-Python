from time import *

my_local_time = localtime() # get struct_time
print(my_local_time)

my_format_time= strftime("%m/%d/%Y, %H:%M:%S", my_local_time)
print(my_format_time)
