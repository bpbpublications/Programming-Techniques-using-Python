# datetime class is imported from datetime module
from datetime import datetime
 # date time object with current date and time
my_current_date_time = datetime.now()

#format code: %Y formats to year
myyear = my_current_date_time.strftime("%Y")
print("The year is:", myyear)

#format code: %m formats to month as a zero padded decimal number
mymonth = my_current_date_time.strftime("%m")
print("The month is:", mymonth)

#format code: %d formats to day as a zero padded decimal number
myday = my_current_date_time.strftime("%d")
print("The day is:", myday)

#format code: %H %M %S formats to hour, minute and second as a zero padded decimal number
mytime = my_current_date_time.strftime("%H:%M:%S")
print("The time is:", mytime)

mydate_time = my_current_date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("The date and time is:",mydate_time)
