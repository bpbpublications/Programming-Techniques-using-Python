from time import *

my_time_string = "27 Apr, 2020"

myresult = strptime(my_time_string, "%d %b, %Y")
print(myresult)

my_time_string = "27 April, 2020"

myresult = strptime(my_time_string, "%d %B, %Y")
print(myresult)
