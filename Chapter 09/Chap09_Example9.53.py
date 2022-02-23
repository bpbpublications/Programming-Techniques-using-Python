from datetime import *
mytimestamp = 1588050930.124536
mydate_time = datetime.fromtimestamp(mytimestamp)

print("The date time object:", mydate_time)
print("----------------------")

mydt = mydate_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 1:", mydt)
print("----------------------")

#format code: %b formats to abbreviated month name
mydt = mydate_time.strftime("%d %b, %Y")
print("Output 2:", mydt)
print("----------------------")

#format code: %B formats to Full month name
mydt = mydate_time.strftime("%d %B, %Y")
print("Output 3:", mydt)
print("----------------------")

# format code: %I formats to 12-hour clock as a zero-padded decimal number.
# format code: %p formats to Locale's AM or PM
mydt = mydate_time.strftime("%I%p")
print("Output 4:", mydt)
