from datetime import datetime
#initialization of constructor with year, month and day
mydt_obj = datetime(2020, 4, 28)
print(mydt_obj)
print("------------------------")

#initialization of constructor with year, month , day and time parameters
mydt_obj = datetime(2020, 4, 28,10,45,30,124536)
print(mydt_obj)
print("------------------------")

#getting datetime object attributes
print("year is:", mydt_obj.year)
print("month is:", mydt_obj.month)
print("hour is:", mydt_obj.hour)
print("minute is:", mydt_obj.minute)
print("second is:", mydt_obj.second)
print("millisecond is:", mydt_obj.microsecond)
print("timestamp is:", mydt_obj.timestamp())
print("------------------------")

#creating date time object with today's date
mytodaysDate = datetime.today()
print(mytodaysDate)
print("------------------------")

#creating date time object with current time and date
myDate_with_currenttime = datetime.now()
print(myDate_with_currenttime)
print("------------------------")

#creating date time object with current UTC time
myDate_with_UTC = datetime.utcnow()
print(myDate_with_UTC)
