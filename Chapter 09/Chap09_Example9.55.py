from datetime import timedelta, date, datetime
my_todaysdate = date.today()
print(my_todaysdate)
my_inc_day = timedelta(days=1)
print(my_inc_day)
print("Tomorrow's date is: ", my_todaysdate+my_inc_day)
print("Yesterday's date is: ", my_todaysdate-my_inc_day)
print("-------------------------------------")

#mydelta atributes
print(timedelta.max)
print(timedelta.min)
print(timedelta.resolution)
print("-------------------------------------")

#printing time duration in seconds
print('Number of seconds in 30 days month is:', timedelta(days=30).total_seconds())
print("-------------------------------------")

#difference between 2 dates
myt1 = date(year = 2020, month = 4, day = 28)
myt2 = date(year = 2018, month = 12, day = 23)
myt3 = myt1 - myt2
print("myt3 =", myt3)
print("-------------------------------------")

#difference between 2 dates and time
myt4 = datetime(year = 2020, month = 4, day = 28, hour = 17, minute = 19, second = 30)
myt5 = datetime(year = 2018, month = 5, day = 10, hour = 15, minute = 55, second = 17)
myt6 = myt4 - myt5
print("myt6 =", myt6)
print("type of myt3 =", type(myt3))
print("type of myt6 =", type(myt6))
print("-------------------------------------")

#difference between 2 timedelta objects
myt1 = timedelta(weeks = 3, days = 6, hours = 2, seconds = 30)
myt2 = timedelta(days = 4, hours = 1, minutes = 5, seconds = 58)
myt3 = myt1 - myt2
print("myt3 =", myt3)
print("-------------------------------------")

#printing negative timedelta
myt1 = timedelta(seconds = 23)
myt2 = timedelta(seconds = 59)
myt3 = myt1 - myt2
print("myt3 =", myt3)
print("myt3 =", abs(myt3))
