from datetime import time
mytime = time()
print("mytime =", mytime)
print(type(mytime))

# arguments: hour, minute and second
mytime1 = time(10, 30, 59)
print("mytime1 =", mytime1)
print("---------------------------")
# arguments:hour, minute and second
mytime2 = time(hour = 10, minute = 30, second = 59)
print("mytime2 =", mytime2)
print("---------------------------")
# arguments:hour, minute, second, microsecond
mytime3 = time(10, 30, 59, 123459)
print("mytime3 =", mytime3)
#displaying hour
print("Hour is: ", mytime3.hour)
#displaying min
print("Min is: ", mytime3.minute)
#displaying sec
print("Sec is: ", mytime3.second)
#displaying microsec
print("Sec is: ", mytime3.microsecond)

print("---------------------------")

#creating a time object using splat operator
mytime4 = (13,31,54,654321)
mytimeobj = time(*mytime4)
print(mytimeobj)
