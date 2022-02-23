from datetime import datetime

mydate_string = "28 April, 2020"

print("My date string is:", mydate_string)
print("type of date string is:", type(mydate_string))
print("------------------------")
#format code: %d formats to day as a zero padded decimal number
#format code: %B:formats to Month Name in full
#format code: %Y: formats to Year in 4 digits
mydate_object = datetime.strptime(mydate_string, "%d %B, %Y")

print("date object is: ", mydate_object)
print("type of date object is:", type(mydate_object))
print("------------------------")

dt_string = "28/04/2020 02:37:39"
# Considering date format dd/mm/yyyy format
# month will be in 0 padded decimal
mydt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", mydt_object1)
