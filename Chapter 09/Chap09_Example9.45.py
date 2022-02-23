#getting ValueError in date as it is outside range
from datetime import date

mydate_obj = date(year = 2020,month=4,day =32)
print("The given date : ",mydate_obj)
