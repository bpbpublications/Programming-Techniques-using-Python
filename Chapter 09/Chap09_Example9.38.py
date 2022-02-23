from time import *

#printing localtime
mystruct_time = localtime()
print(type(mystruct_time))
print(mystruct_time)
print("Year is: ",mystruct_time.tm_year)
print("Month is: ",mystruct_time.tm_mon)
print("Date is: ",mystruct_time.tm_mday)
print("Hour is: ",mystruct_time.tm_hour)
print("Min is: ",mystruct_time.tm_min)
print("Second is: ",mystruct_time.tm_sec)
print(mystruct_time.tm_wday)
print(mystruct_time.tm_yday)
print("--------------------")
#printing UTC
mystruct_time1 = gmtime()
print(type(mystruct_time1))
print(mystruct_time1)
print("Year is: ",mystruct_time1.tm_year)
print("Month is: ",mystruct_time1.tm_mon)
print("Date is: ",mystruct_time1.tm_mday)
print("Hour is: ",mystruct_time1.tm_hour)
print("Min is: ",mystruct_time1.tm_min)
print("Second is: ",mystruct_time1.tm_sec)
print(mystruct_time1.tm_wday)
print(mystruct_time1.tm_yday)

print(f"The difference between localtime and UTC time is {mystruct_time.tm_hour - mystruct_time1.tm_hour} hrs and {mystruct_time.tm_min-mystruct_time1.tm_min} mins")
