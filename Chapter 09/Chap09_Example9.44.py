from datetime import date

mydate_obj = date(year = 2020,month=4,day =27)
print("The given date : ",mydate_obj)

# printing object type
print(type(mydate_obj))

mydate_obj = date(2020,4,27)
print("The given date : ",mydate_obj)
print("The Min Date is: ",mydate_obj.min)
print("The Max Date is: ",mydate_obj.max)
print("The Year is: ",mydate_obj.year)
print("The Month is: ",mydate_obj.month)
print("The Day is: ",mydate_obj.day)
